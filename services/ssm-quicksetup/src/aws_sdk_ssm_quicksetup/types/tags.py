"""Generated from Smithy shape ``com.amazonaws.ssmquicksetup#Tags``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm_quicksetup.types.tag_entry

Tags: TypeAlias = list["aws_sdk_ssm_quicksetup.types.tag_entry.TagEntry"]


# --- restJson1 ser/de ---
def serialize_json(value: Tags) -> list:
    import aws_sdk_ssm_quicksetup.types.tag_entry

    out: list = []
    for item in value:
        out.append(aws_sdk_ssm_quicksetup.types.tag_entry.serialize_json(item))
    return out


def deserialize_json(data: list) -> Tags:
    import aws_sdk_ssm_quicksetup.types.tag_entry

    out: Tags = []
    for item in data:
        out.append(aws_sdk_ssm_quicksetup.types.tag_entry.deserialize_json(item))
    return out
