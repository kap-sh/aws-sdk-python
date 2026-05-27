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
