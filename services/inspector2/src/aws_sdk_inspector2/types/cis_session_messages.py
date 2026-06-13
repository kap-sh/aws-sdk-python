"""Generated from Smithy shape ``com.amazonaws.inspector2#CisSessionMessages``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.cis_session_message

CisSessionMessages: TypeAlias = list[
    "aws_sdk_inspector2.types.cis_session_message.CisSessionMessage"
]


# --- restJson1 ser/de ---
def serialize_json(value: CisSessionMessages) -> list:
    import aws_sdk_inspector2.types.cis_session_message

    out: list = []
    for item in value:
        out.append(aws_sdk_inspector2.types.cis_session_message.serialize_json(item))
    return out


def deserialize_json(data: list) -> CisSessionMessages:
    import aws_sdk_inspector2.types.cis_session_message

    out: CisSessionMessages = []
    for item in data:
        out.append(aws_sdk_inspector2.types.cis_session_message.deserialize_json(item))
    return out
