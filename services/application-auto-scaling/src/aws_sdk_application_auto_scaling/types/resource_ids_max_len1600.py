"""Generated from Smithy shape ``com.amazonaws.applicationautoscaling#ResourceIdsMaxLen1600``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_application_auto_scaling.types.resource_id_max_len1600

ResourceIdsMaxLen1600: TypeAlias = list[
    "aws_sdk_application_auto_scaling.types.resource_id_max_len1600.ResourceIdMaxLen1600"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceIdsMaxLen1600) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ResourceIdsMaxLen1600:
    return list(data)
