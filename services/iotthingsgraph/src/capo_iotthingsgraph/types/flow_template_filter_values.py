"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#FlowTemplateFilterValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotthingsgraph.types.flow_template_filter_value

FlowTemplateFilterValues: TypeAlias = list[
    "capo_iotthingsgraph.types.flow_template_filter_value.FlowTemplateFilterValue"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FlowTemplateFilterValues) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> FlowTemplateFilterValues:
    return list(data)
