"""Generated from Smithy shape ``com.amazonaws.dynamodb#ListExportsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.export_next_token
    import aws_sdk_dynamodb.types.export_summaries


class ListExportsOutput(TypedDict):
    export_summaries: NotRequired[
        "aws_sdk_dynamodb.types.export_summaries.ExportSummaries"
    ]
    """<p>A list of <code>ExportSummary</code> objects.</p>"""
    next_token: NotRequired["aws_sdk_dynamodb.types.export_next_token.ExportNextToken"]
    """<p>If this value is returned, there are additional results to be displayed. To retrieve them, call <code>ListExports</code> again, with <code>NextToken</code> set to this value.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListExportsOutput) -> dict:
    out: dict = {}
    if "export_summaries" in value:
        import aws_sdk_dynamodb.types.export_summaries

        out["ExportSummaries"] = (
            aws_sdk_dynamodb.types.export_summaries.serialize_aws_json_1_0(
                value["export_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListExportsOutput:
    out: ListExportsOutput = {}  # type: ignore[typeddict-item]
    if "ExportSummaries" in data:
        import aws_sdk_dynamodb.types.export_summaries

        out["export_summaries"] = (
            aws_sdk_dynamodb.types.export_summaries.deserialize_aws_json_1_0(
                data["ExportSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
