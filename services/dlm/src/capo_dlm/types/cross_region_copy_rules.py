"""Generated from Smithy shape ``com.amazonaws.dlm#CrossRegionCopyRules``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_dlm.types.cross_region_copy_rule

CrossRegionCopyRules: TypeAlias = list[
    "capo_dlm.types.cross_region_copy_rule.CrossRegionCopyRule"
]


# --- restJson1 ser/de ---
def serialize_json(value: CrossRegionCopyRules) -> list:
    import capo_dlm.types.cross_region_copy_rule

    out: list = []
    for item in value:
        out.append(capo_dlm.types.cross_region_copy_rule.serialize_json(item))
    return out


def deserialize_json(data: list) -> CrossRegionCopyRules:
    import capo_dlm.types.cross_region_copy_rule

    out: CrossRegionCopyRules = []
    for item in data:
        out.append(capo_dlm.types.cross_region_copy_rule.deserialize_json(item))
    return out
