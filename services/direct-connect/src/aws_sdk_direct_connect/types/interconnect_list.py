"""Generated from Smithy shape ``com.amazonaws.directconnect#InterconnectList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_direct_connect.types.interconnect

InterconnectList: TypeAlias = list[
    "aws_sdk_direct_connect.types.interconnect.Interconnect"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InterconnectList) -> list:
    import aws_sdk_direct_connect.types.interconnect

    out: list = []
    for item in value:
        out.append(
            aws_sdk_direct_connect.types.interconnect.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> InterconnectList:
    import aws_sdk_direct_connect.types.interconnect

    out: InterconnectList = []
    for item in data:
        out.append(
            aws_sdk_direct_connect.types.interconnect.deserialize_aws_json_1_1(item)
        )
    return out
