"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#StateTemplateSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.state_template_summary

StateTemplateSummaries: TypeAlias = list[
    "aws_sdk_iotfleetwise.types.state_template_summary.StateTemplateSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StateTemplateSummaries) -> list:
    import aws_sdk_iotfleetwise.types.state_template_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iotfleetwise.types.state_template_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> StateTemplateSummaries:
    import aws_sdk_iotfleetwise.types.state_template_summary

    out: StateTemplateSummaries = []
    for item in data:
        out.append(
            aws_sdk_iotfleetwise.types.state_template_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out
