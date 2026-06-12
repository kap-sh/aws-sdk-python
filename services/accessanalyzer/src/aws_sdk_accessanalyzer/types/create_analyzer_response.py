"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#CreateAnalyzerResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.analyzer_arn


class CreateAnalyzerResponse(TypedDict):
    arn: NotRequired["aws_sdk_accessanalyzer.types.analyzer_arn.AnalyzerArn"]
    """<p>The ARN of the analyzer that was created by the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAnalyzerResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> CreateAnalyzerResponse:
    out: CreateAnalyzerResponse = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    return out
