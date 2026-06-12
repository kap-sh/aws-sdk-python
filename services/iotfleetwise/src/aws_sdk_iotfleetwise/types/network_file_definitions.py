"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#NetworkFileDefinitions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.network_file_definition

NetworkFileDefinitions: TypeAlias = list[
    "aws_sdk_iotfleetwise.types.network_file_definition.NetworkFileDefinition"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: NetworkFileDefinitions) -> list:
    import aws_sdk_iotfleetwise.types.network_file_definition

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iotfleetwise.types.network_file_definition.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> NetworkFileDefinitions:
    import aws_sdk_iotfleetwise.types.network_file_definition

    out: NetworkFileDefinitions = []
    for item in data:
        out.append(
            aws_sdk_iotfleetwise.types.network_file_definition.deserialize_aws_json_1_0(
                item
            )
        )
    return out
