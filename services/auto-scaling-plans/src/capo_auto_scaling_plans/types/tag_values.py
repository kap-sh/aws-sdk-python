"""Generated from Smithy shape ``com.amazonaws.autoscalingplans#TagValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_auto_scaling_plans.types.xml_string_max_len256

TagValues: TypeAlias = list[
    "capo_auto_scaling_plans.types.xml_string_max_len256.XmlStringMaxLen256"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagValues) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> TagValues:
    return list(data)
