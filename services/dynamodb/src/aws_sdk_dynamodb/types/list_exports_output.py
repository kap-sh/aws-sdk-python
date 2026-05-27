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
