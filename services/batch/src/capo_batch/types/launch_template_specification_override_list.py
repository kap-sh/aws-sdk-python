"""Generated from Smithy shape ``com.amazonaws.batch#LaunchTemplateSpecificationOverrideList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_batch.types.launch_template_specification_override

LaunchTemplateSpecificationOverrideList: TypeAlias = list[
    "capo_batch.types.launch_template_specification_override.LaunchTemplateSpecificationOverride"
]


# --- restJson1 ser/de ---
def serialize_json(value: LaunchTemplateSpecificationOverrideList) -> list:
    import capo_batch.types.launch_template_specification_override

    out: list = []
    for item in value:
        out.append(
            capo_batch.types.launch_template_specification_override.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> LaunchTemplateSpecificationOverrideList:
    import capo_batch.types.launch_template_specification_override

    out: LaunchTemplateSpecificationOverrideList = []
    for item in data:
        out.append(
            capo_batch.types.launch_template_specification_override.deserialize_json(
                item
            )
        )
    return out
