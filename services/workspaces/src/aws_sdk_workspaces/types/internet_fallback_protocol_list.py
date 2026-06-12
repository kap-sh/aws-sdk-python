"""Generated from Smithy shape ``com.amazonaws.workspaces#InternetFallbackProtocolList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.internet_fallback_protocol

InternetFallbackProtocolList: TypeAlias = list[
    "aws_sdk_workspaces.types.internet_fallback_protocol.InternetFallbackProtocol"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InternetFallbackProtocolList) -> list:
    import aws_sdk_workspaces.types.internet_fallback_protocol

    out: list = []
    for item in value:
        out.append(
            aws_sdk_workspaces.types.internet_fallback_protocol.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> InternetFallbackProtocolList:
    import aws_sdk_workspaces.types.internet_fallback_protocol

    out: InternetFallbackProtocolList = []
    for item in data:
        out.append(
            aws_sdk_workspaces.types.internet_fallback_protocol.deserialize_aws_json_1_1(
                item
            )
        )
    return out
