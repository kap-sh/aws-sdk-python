"""Generated from Smithy shape ``com.amazonaws.lakeformation#RedshiftServiceIntegrations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lakeformation.types.redshift_scope_union

RedshiftServiceIntegrations: TypeAlias = list[
    "capo_lakeformation.types.redshift_scope_union.RedshiftScopeUnion"
]


# --- restJson1 ser/de ---
def serialize_json(value: RedshiftServiceIntegrations) -> list:
    import capo_lakeformation.types.redshift_scope_union

    out: list = []
    for item in value:
        out.append(capo_lakeformation.types.redshift_scope_union.serialize_json(item))
    return out


def deserialize_json(data: list) -> RedshiftServiceIntegrations:
    import capo_lakeformation.types.redshift_scope_union

    out: RedshiftServiceIntegrations = []
    for item in data:
        out.append(capo_lakeformation.types.redshift_scope_union.deserialize_json(item))
    return out
