"""Generated from Smithy shape ``com.amazonaws.omics#InlineSettings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_omics.types.inline_setting

InlineSettings: TypeAlias = list["aws_sdk_omics.types.inline_setting.InlineSetting"]


# --- restJson1 ser/de ---
def serialize_json(value: InlineSettings) -> list:
    import aws_sdk_omics.types.inline_setting

    out: list = []
    for item in value:
        out.append(aws_sdk_omics.types.inline_setting.serialize_json(item))
    return out


def deserialize_json(data: list) -> InlineSettings:
    import aws_sdk_omics.types.inline_setting

    out: InlineSettings = []
    for item in data:
        out.append(aws_sdk_omics.types.inline_setting.deserialize_json(item))
    return out
