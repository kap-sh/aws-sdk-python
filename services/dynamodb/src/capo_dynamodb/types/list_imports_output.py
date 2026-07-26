"""Generated from Smithy shape ``com.amazonaws.dynamodb#ListImportsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.import_next_token
    import capo_dynamodb.types.import_summary_list


class ListImportsOutput(TypedDict, closed=True):
    import_summary_list: NotRequired[
        "capo_dynamodb.types.import_summary_list.ImportSummaryList"
    ]
    """<p> A list of <code>ImportSummary</code> objects. </p>"""
    next_token: NotRequired["capo_dynamodb.types.import_next_token.ImportNextToken"]
    """<p> If this value is returned, there are additional results to be displayed. To retrieve them, call <code>ListImports</code> again, with <code>NextToken</code> set to this value. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListImportsOutput) -> dict:
    out: dict = {}
    if "import_summary_list" in value:
        import capo_dynamodb.types.import_summary_list

        out["ImportSummaryList"] = (
            capo_dynamodb.types.import_summary_list.serialize_aws_json_1_0(
                value["import_summary_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListImportsOutput:
    out: ListImportsOutput = {}  # type: ignore[typeddict-item]
    if "ImportSummaryList" in data:
        import capo_dynamodb.types.import_summary_list

        out["import_summary_list"] = (
            capo_dynamodb.types.import_summary_list.deserialize_aws_json_1_0(
                data["ImportSummaryList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
