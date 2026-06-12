"""Generated from Smithy shape ``com.amazonaws.ssm#OpsItemEventSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.ops_item_event_summary

OpsItemEventSummaries: TypeAlias = list[
    "aws_sdk_ssm.types.ops_item_event_summary.OpsItemEventSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpsItemEventSummaries) -> list:
    import aws_sdk_ssm.types.ops_item_event_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_ssm.types.ops_item_event_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> OpsItemEventSummaries:
    import aws_sdk_ssm.types.ops_item_event_summary

    out: OpsItemEventSummaries = []
    for item in data:
        out.append(
            aws_sdk_ssm.types.ops_item_event_summary.deserialize_aws_json_1_1(item)
        )
    return out
