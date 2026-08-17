"""Generated from Smithy shape ``com.amazonaws.dynamodb#ListExportsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.export_next_token
    import capo_dynamodb.types.export_summaries


class ListExportsOutput(TypedDict, closed=True):
    export_summaries: NotRequired[
        "capo_dynamodb.types.export_summaries.ExportSummaries"
    ]
    """<p>A list of <code>ExportSummary</code> objects.</p>"""
    next_token: NotRequired["capo_dynamodb.types.export_next_token.ExportNextToken"]
    """<p>If this value is returned, there are additional results to be displayed. To retrieve them, call <code>ListExports</code> again, with <code>NextToken</code> set to this value.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListExportsOutput) -> dict:
    out: dict = {}
    if "export_summaries" in value:
        import capo_dynamodb.types.export_summaries

        out["ExportSummaries"] = (
            capo_dynamodb.types.export_summaries.serialize_aws_json_1_0(
                value["export_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListExportsOutput:
    out: ListExportsOutput = {}  # type: ignore[typeddict-item]
    if data.get("ExportSummaries") is not None:
        import capo_dynamodb.types.export_summaries

        out["export_summaries"] = (
            capo_dynamodb.types.export_summaries.deserialize_aws_json_1_0(
                data["ExportSummaries"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
