"""Generated from Smithy shape ``com.amazonaws.lakeformation#ServiceIntegrationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lakeformation.types.service_integration_union

ServiceIntegrationList: TypeAlias = list[
    "capo_lakeformation.types.service_integration_union.ServiceIntegrationUnion"
]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceIntegrationList) -> list:
    import capo_lakeformation.types.service_integration_union

    out: list = []
    for item in value:
        out.append(
            capo_lakeformation.types.service_integration_union.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ServiceIntegrationList:
    import capo_lakeformation.types.service_integration_union

    out: ServiceIntegrationList = []
    for item in data:
        out.append(
            capo_lakeformation.types.service_integration_union.deserialize_json(item)
        )
    return out
