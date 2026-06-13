"""Generated from Smithy shape ``com.amazonaws.qconnect#EmailHeaders``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.email_header

EmailHeaders: TypeAlias = list["aws_sdk_qconnect.types.email_header.EmailHeader"]


# --- restJson1 ser/de ---
def serialize_json(value: EmailHeaders) -> list:
    import aws_sdk_qconnect.types.email_header

    out: list = []
    for item in value:
        out.append(aws_sdk_qconnect.types.email_header.serialize_json(item))
    return out


def deserialize_json(data: list) -> EmailHeaders:
    import aws_sdk_qconnect.types.email_header

    out: EmailHeaders = []
    for item in data:
        out.append(aws_sdk_qconnect.types.email_header.deserialize_json(item))
    return out
