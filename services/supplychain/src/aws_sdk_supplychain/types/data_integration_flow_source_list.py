"""Generated from Smithy shape ``com.amazonaws.supplychain#DataIntegrationFlowSourceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_supplychain.types.data_integration_flow_source

DataIntegrationFlowSourceList: TypeAlias = list[
    "aws_sdk_supplychain.types.data_integration_flow_source.DataIntegrationFlowSource"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataIntegrationFlowSourceList) -> list:
    import aws_sdk_supplychain.types.data_integration_flow_source

    out: list = []
    for item in value:
        out.append(
            aws_sdk_supplychain.types.data_integration_flow_source.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> DataIntegrationFlowSourceList:
    import aws_sdk_supplychain.types.data_integration_flow_source

    out: DataIntegrationFlowSourceList = []
    for item in data:
        out.append(
            aws_sdk_supplychain.types.data_integration_flow_source.deserialize_json(
                item
            )
        )
    return out
