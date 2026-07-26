"""Generated from Smithy shape ``com.amazonaws.dynamodb#ListImportsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.import_next_token
    import capo_dynamodb.types.list_imports_max_limit
    import capo_dynamodb.types.table_arn


class ListImportsInput(TypedDict, closed=True):
    table_arn: NotRequired["capo_dynamodb.types.table_arn.TableArn"]
    """<p> The Amazon Resource Name (ARN) associated with the table that was imported to. </p>"""
    page_size: NotRequired[
        "capo_dynamodb.types.list_imports_max_limit.ListImportsMaxLimit"
    ]
    """<p> The number of <code>ImportSummary </code>objects returned in a single page. </p>"""
    next_token: NotRequired["capo_dynamodb.types.import_next_token.ImportNextToken"]
    """<p> An optional string that, if supplied, must be copied from the output of a previous call to <code>ListImports</code>. When provided in this manner, the API fetches the next page of results. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListImportsInput) -> dict:
    out: dict = {}
    if "table_arn" in value:
        out["TableArn"] = value["table_arn"]
    if "page_size" in value:
        out["PageSize"] = value["page_size"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListImportsInput:
    out: ListImportsInput = {}  # type: ignore[typeddict-item]
    if "TableArn" in data:
        out["table_arn"] = data["TableArn"]
    if "PageSize" in data:
        out["page_size"] = data["PageSize"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
