"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#CreateServiceLinkedAnalyzerResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.analyzer_arn


class CreateServiceLinkedAnalyzerResponse(TypedDict):
    arn: NotRequired["aws_sdk_accessanalyzer.types.analyzer_arn.AnalyzerArn"]
    """<p>The ARN of the service-linked analyzer that was created by the request. The analyzer name follows the format <code>_AccessAnalyzerFor{ServiceName}-{Id}</code> where <code>Id</code> is a randomly generated identifier.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateServiceLinkedAnalyzerResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> CreateServiceLinkedAnalyzerResponse:
    out: CreateServiceLinkedAnalyzerResponse = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    return out
