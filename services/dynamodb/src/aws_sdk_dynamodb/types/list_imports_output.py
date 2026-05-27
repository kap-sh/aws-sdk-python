"""Generated from Smithy shape ``com.amazonaws.dynamodb#ListImportsOutput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.import_next_token
    import aws_sdk_dynamodb.types.import_summary_list


class ListImportsOutput(TypedDict):
    import_summary_list: NotRequired[
        "aws_sdk_dynamodb.types.import_summary_list.ImportSummaryList"
    ]
    """<p> A list of <code>ImportSummary</code> objects. </p>"""
    next_token: NotRequired["aws_sdk_dynamodb.types.import_next_token.ImportNextToken"]
    """<p> If this value is returned, there are additional results to be displayed. To retrieve them, call <code>ListImports</code> again, with <code>NextToken</code> set to this value. </p>"""
