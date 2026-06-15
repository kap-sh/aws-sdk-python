"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#GetAccessPreviewRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.access_preview_id
    import aws_sdk_accessanalyzer.types.analyzer_arn


class GetAccessPreviewRequest(TypedDict):
    access_preview_id: "aws_sdk_accessanalyzer.types.access_preview_id.AccessPreviewId"
    """<p>The unique ID for the access preview.</p>"""
    analyzer_arn: "aws_sdk_accessanalyzer.types.analyzer_arn.AnalyzerArn"
    r"""<p>The <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-getting-started.html#permission-resources\">ARN of the analyzer</a> used to generate the access preview.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAccessPreviewRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetAccessPreviewRequest:
    out: GetAccessPreviewRequest = {}  # type: ignore[typeddict-item]
    return out
