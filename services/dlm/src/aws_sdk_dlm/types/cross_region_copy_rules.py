"""Generated from Smithy shape ``com.amazonaws.dlm#CrossRegionCopyRules``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dlm.types.cross_region_copy_rule

CrossRegionCopyRules: TypeAlias = list[
    "aws_sdk_dlm.types.cross_region_copy_rule.CrossRegionCopyRule"
]


# --- restJson1 ser/de ---
def serialize_json(value: CrossRegionCopyRules) -> list:
    import aws_sdk_dlm.types.cross_region_copy_rule

    out: list = []
    for item in value:
        out.append(aws_sdk_dlm.types.cross_region_copy_rule.serialize_json(item))
    return out


def deserialize_json(data: list) -> CrossRegionCopyRules:
    import aws_sdk_dlm.types.cross_region_copy_rule

    out: CrossRegionCopyRules = []
    for item in data:
        out.append(aws_sdk_dlm.types.cross_region_copy_rule.deserialize_json(item))
    return out
