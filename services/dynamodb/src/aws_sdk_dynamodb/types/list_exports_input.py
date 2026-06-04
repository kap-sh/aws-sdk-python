"""Generated from Smithy shape ``com.amazonaws.dynamodb#ListExportsInput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.export_next_token
    import aws_sdk_dynamodb.types.list_exports_max_limit
    import aws_sdk_dynamodb.types.table_arn


class ListExportsInput(TypedDict):
    table_arn: NotRequired["aws_sdk_dynamodb.types.table_arn.TableArn"]
    """<p>The Amazon Resource Name (ARN) associated with the exported table.</p>"""
    max_results: NotRequired[
        "aws_sdk_dynamodb.types.list_exports_max_limit.ListExportsMaxLimit"
    ]
    """<p>Maximum number of results to return per page.</p>"""
    next_token: NotRequired["aws_sdk_dynamodb.types.export_next_token.ExportNextToken"]
    """<p>An optional string that, if supplied, must be copied from the output of a previous call to <code>ListExports</code>. When provided in this manner, the API fetches the next page of results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListExportsInput) -> dict:
    out: dict = {}
    if "table_arn" in value:
        out["TableArn"] = value["table_arn"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListExportsInput:
    out: ListExportsInput = {}  # type: ignore[typeddict-item]
    if "TableArn" in data:
        out["table_arn"] = data["TableArn"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
