# RePart

RePart helps people and repair shops find reusable smartphone components from damaged devices.

## Run & Operate

- `pnpm --filter @workspace/api-server run dev` — run the API server on its managed workflow
- `pnpm --filter @workspace/repart run dev` — run the web app through its managed workflow
- `pnpm run typecheck` — typecheck all workspace packages
- `pnpm --filter @workspace/api-server run test:matching` — test compatibility rules
- `pnpm run build` — typecheck and build all packages
- `pnpm --filter @workspace/api-spec run codegen` — regenerate API hooks and Zod schemas from the OpenAPI spec
- `pnpm --filter @workspace/db run push` — push development database schema changes
- Required environment: `DATABASE_URL`
- Required session signing secret: `SESSION_SECRET`

The API seeds clearly marked demo devices, components, requests, and compatibility rules when no demo catalog exists. The web app is Arabic-first and uses right-to-left layout.

## Stack

- pnpm workspaces, Node.js 24, TypeScript 5.9
- API: Express 5
- Database: PostgreSQL + Drizzle ORM
- Validation: generated Zod schemas
- API codegen: Orval from the OpenAPI contract
- Web: React, Vite, Wouter, TanStack Query, Tailwind CSS

## Where things live

- `artifacts/repart/` — Arabic RTL web app and user-facing workflows
- `artifacts/api-server/src/routes/repart.ts` — device/request operations, matching results, shop actions, dashboards
- `artifacts/api-server/src/lib/matching-rules.ts` — deterministic compatibility and ranking rules
- `artifacts/api-server/src/lib/repart-seed.ts` — clearly labeled demo records and controlled demo catalog
- `lib/db/src/schema/index.ts` — relational PostgreSQL tables
- `lib/api-spec/openapi.yaml` — source API contract for generated client and validation schemas

## Architecture decisions

- The server matches by explicit compatibility rules and complete device information; a shared device name alone never confirms compatibility.
- User-reported component conditions start unverified. The shop action records a simulated inspection and must not be presented as a physical inspection.
- The demo selector starts a server-side database session for one of the three seeded accounts. API permissions use the account role read from PostgreSQL, not the selected interface label.
- Individuals can manage only their own devices and requests. Repair shops process open marketplace requests; reuse transactions are tied to the shop account that completed them.
- Environmental impact counts completed reuse transactions only. Component weight and avoided emissions are not estimated.
- The Admin view is read-only monitoring. New admin management tools and production sign-in are not included in this phase.

## Product

Register smartphones and component conditions, search repair needs against available parts, review ranked matches, manage simulated shop verification and completed reuse, and view database-backed reuse impact.

## User preferences

- Arabic is the default language and the interface is RTL.
- Keep the English brand name `RePart`.
- Keep the demo-account selector label exactly `وضع العرض`.
- Mark demo records and simulated verification clearly.

## Gotchas

- After changing `lib/api-spec/openapi.yaml`, rerun API codegen before using generated hooks or schemas.
- Push database schema changes with the DB package's `push` command. Demo data is seeded by the API when absent.
- Demo-account switching is disabled when the API runs with `NODE_ENV=production`; real account onboarding/authentication is a separate follow-up.

## Pointers

- See the `pnpm-workspace` skill for workspace structure, TypeScript setup, and package details.
