"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#ListAccessPreviewsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.analyzer_arn
    import aws_sdk_accessanalyzer.types.token


class ListAccessPreviewsRequest(TypedDict, closed=True):
    analyzer_arn: "aws_sdk_accessanalyzer.types.analyzer_arn.AnalyzerArn"
    r"""<p>The <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-getting-started.html#permission-resources\">ARN of the analyzer</a> used to generate the access preview.</p>"""
    next_token: NotRequired["aws_sdk_accessanalyzer.types.token.Token"]
    """<p>A token used for pagination of results returned.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of results to return in the response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAccessPreviewsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAccessPreviewsRequest:
    out: ListAccessPreviewsRequest = {}  # type: ignore[typeddict-item]
    return out
