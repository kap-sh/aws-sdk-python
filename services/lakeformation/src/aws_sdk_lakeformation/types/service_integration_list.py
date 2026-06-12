"""Generated from Smithy shape ``com.amazonaws.lakeformation#ServiceIntegrationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.service_integration_union

ServiceIntegrationList: TypeAlias = list[
    "aws_sdk_lakeformation.types.service_integration_union.ServiceIntegrationUnion"
]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceIntegrationList) -> list:
    import aws_sdk_lakeformation.types.service_integration_union

    out: list = []
    for item in value:
        out.append(
            aws_sdk_lakeformation.types.service_integration_union.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ServiceIntegrationList:
    import aws_sdk_lakeformation.types.service_integration_union

    out: ServiceIntegrationList = []
    for item in data:
        out.append(
            aws_sdk_lakeformation.types.service_integration_union.deserialize_json(item)
        )
    return out
