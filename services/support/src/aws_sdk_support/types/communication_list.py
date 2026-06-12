"""Generated from Smithy shape ``com.amazonaws.support#CommunicationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_support.types.communication

CommunicationList: TypeAlias = list["aws_sdk_support.types.communication.Communication"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CommunicationList) -> list:
    import aws_sdk_support.types.communication

    out: list = []
    for item in value:
        out.append(aws_sdk_support.types.communication.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> CommunicationList:
    import aws_sdk_support.types.communication

    out: CommunicationList = []
    for item in data:
        out.append(aws_sdk_support.types.communication.deserialize_aws_json_1_1(item))
    return out
