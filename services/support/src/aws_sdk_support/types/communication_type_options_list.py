"""Generated from Smithy shape ``com.amazonaws.support#CommunicationTypeOptionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_support.types.communication_type_options

CommunicationTypeOptionsList: TypeAlias = list[
    "aws_sdk_support.types.communication_type_options.CommunicationTypeOptions"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CommunicationTypeOptionsList) -> list:
    import aws_sdk_support.types.communication_type_options

    out: list = []
    for item in value:
        out.append(
            aws_sdk_support.types.communication_type_options.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> CommunicationTypeOptionsList:
    import aws_sdk_support.types.communication_type_options

    out: CommunicationTypeOptionsList = []
    for item in data:
        out.append(
            aws_sdk_support.types.communication_type_options.deserialize_aws_json_1_1(
                item
            )
        )
    return out
