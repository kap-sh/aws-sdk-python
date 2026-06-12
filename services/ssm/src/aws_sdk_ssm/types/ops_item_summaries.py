"""Generated from Smithy shape ``com.amazonaws.ssm#OpsItemSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.ops_item_summary

OpsItemSummaries: TypeAlias = list["aws_sdk_ssm.types.ops_item_summary.OpsItemSummary"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpsItemSummaries) -> list:
    import aws_sdk_ssm.types.ops_item_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_ssm.types.ops_item_summary.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> OpsItemSummaries:
    import aws_sdk_ssm.types.ops_item_summary

    out: OpsItemSummaries = []
    for item in data:
        out.append(aws_sdk_ssm.types.ops_item_summary.deserialize_aws_json_1_1(item))
    return out
