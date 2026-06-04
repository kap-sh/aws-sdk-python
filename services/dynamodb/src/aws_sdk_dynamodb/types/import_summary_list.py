"""Generated from Smithy shape ``com.amazonaws.dynamodb#ImportSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.import_summary

ImportSummaryList: TypeAlias = list[
    "aws_sdk_dynamodb.types.import_summary.ImportSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ImportSummaryList) -> list:
    import aws_sdk_dynamodb.types.import_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_dynamodb.types.import_summary.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> ImportSummaryList:
    import aws_sdk_dynamodb.types.import_summary

    out: ImportSummaryList = []
    for item in data:
        out.append(aws_sdk_dynamodb.types.import_summary.deserialize_aws_json_1_0(item))
    return out
