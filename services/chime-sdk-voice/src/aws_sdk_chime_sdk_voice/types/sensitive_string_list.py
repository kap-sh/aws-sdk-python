"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#SensitiveStringList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.sensitive_string

SensitiveStringList: TypeAlias = list[
    "aws_sdk_chime_sdk_voice.types.sensitive_string.SensitiveString"
]


# --- restJson1 ser/de ---
def serialize_json(value: SensitiveStringList) -> list:
    return list(value)


def deserialize_json(data: list) -> SensitiveStringList:
    return list(data)
