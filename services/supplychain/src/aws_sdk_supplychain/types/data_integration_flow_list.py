"""Generated from Smithy shape ``com.amazonaws.supplychain#DataIntegrationFlowList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_supplychain.types.data_integration_flow

DataIntegrationFlowList: TypeAlias = list[
    "aws_sdk_supplychain.types.data_integration_flow.DataIntegrationFlow"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataIntegrationFlowList) -> list:
    import aws_sdk_supplychain.types.data_integration_flow

    out: list = []
    for item in value:
        out.append(aws_sdk_supplychain.types.data_integration_flow.serialize_json(item))
    return out


def deserialize_json(data: list) -> DataIntegrationFlowList:
    import aws_sdk_supplychain.types.data_integration_flow

    out: DataIntegrationFlowList = []
    for item in data:
        out.append(
            aws_sdk_supplychain.types.data_integration_flow.deserialize_json(item)
        )
    return out
