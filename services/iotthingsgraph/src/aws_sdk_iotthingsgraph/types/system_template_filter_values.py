"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#SystemTemplateFilterValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iotthingsgraph.types.system_template_filter_value

SystemTemplateFilterValues: TypeAlias = list[
    "aws_sdk_iotthingsgraph.types.system_template_filter_value.SystemTemplateFilterValue"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SystemTemplateFilterValues) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> SystemTemplateFilterValues:
    return list(data)
