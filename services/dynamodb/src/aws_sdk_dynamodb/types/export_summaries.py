"""Generated from Smithy shape ``com.amazonaws.dynamodb#ExportSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.export_summary

ExportSummaries: TypeAlias = list["aws_sdk_dynamodb.types.export_summary.ExportSummary"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExportSummaries) -> list:
    import aws_sdk_dynamodb.types.export_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_dynamodb.types.export_summary.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> ExportSummaries:
    import aws_sdk_dynamodb.types.export_summary

    out: ExportSummaries = []
    for item in data:
        out.append(aws_sdk_dynamodb.types.export_summary.deserialize_aws_json_1_0(item))
    return out
