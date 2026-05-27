"""Generated from Smithy shape ``com.amazonaws.dynamodb#ListImportsInput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.import_next_token
    import aws_sdk_dynamodb.types.list_imports_max_limit
    import aws_sdk_dynamodb.types.table_arn


class ListImportsInput(TypedDict):
    table_arn: NotRequired["aws_sdk_dynamodb.types.table_arn.TableArn"]
    """<p> The Amazon Resource Name (ARN) associated with the table that was imported to. </p>"""
    page_size: NotRequired[
        "aws_sdk_dynamodb.types.list_imports_max_limit.ListImportsMaxLimit"
    ]
    """<p> The number of <code>ImportSummary </code>objects returned in a single page. </p>"""
    next_token: NotRequired["aws_sdk_dynamodb.types.import_next_token.ImportNextToken"]
    """<p> An optional string that, if supplied, must be copied from the output of a previous call to <code>ListImports</code>. When provided in this manner, the API fetches the next page of results. </p>"""
