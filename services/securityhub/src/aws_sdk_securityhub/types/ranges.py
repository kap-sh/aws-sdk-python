"""Generated from Smithy shape ``com.amazonaws.securityhub#Ranges``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.range

Ranges: TypeAlias = list["aws_sdk_securityhub.types.range.Range"]


# --- restJson1 ser/de ---
def serialize_json(value: Ranges) -> list:
    import aws_sdk_securityhub.types.range

    out: list = []
    for item in value:
        out.append(aws_sdk_securityhub.types.range.serialize_json(item))
    return out


def deserialize_json(data: list) -> Ranges:
    import aws_sdk_securityhub.types.range

    out: Ranges = []
    for item in data:
        out.append(aws_sdk_securityhub.types.range.deserialize_json(item))
    return out
