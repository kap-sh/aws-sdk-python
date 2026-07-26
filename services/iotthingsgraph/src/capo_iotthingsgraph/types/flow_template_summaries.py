"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#FlowTemplateSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotthingsgraph.types.flow_template_summary

FlowTemplateSummaries: TypeAlias = list[
    "capo_iotthingsgraph.types.flow_template_summary.FlowTemplateSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FlowTemplateSummaries) -> list:
    import capo_iotthingsgraph.types.flow_template_summary

    out: list = []
    for item in value:
        out.append(
            capo_iotthingsgraph.types.flow_template_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> FlowTemplateSummaries:
    import capo_iotthingsgraph.types.flow_template_summary

    out: FlowTemplateSummaries = []
    for item in data:
        out.append(
            capo_iotthingsgraph.types.flow_template_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
