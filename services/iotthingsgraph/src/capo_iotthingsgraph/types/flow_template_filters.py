"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#FlowTemplateFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotthingsgraph.types.flow_template_filter

FlowTemplateFilters: TypeAlias = list[
    "capo_iotthingsgraph.types.flow_template_filter.FlowTemplateFilter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FlowTemplateFilters) -> list:
    import capo_iotthingsgraph.types.flow_template_filter

    out: list = []
    for item in value:
        out.append(
            capo_iotthingsgraph.types.flow_template_filter.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> FlowTemplateFilters:
    import capo_iotthingsgraph.types.flow_template_filter

    out: FlowTemplateFilters = []
    for item in data:
        out.append(
            capo_iotthingsgraph.types.flow_template_filter.deserialize_aws_json_1_1(
                item
            )
        )
    return out
