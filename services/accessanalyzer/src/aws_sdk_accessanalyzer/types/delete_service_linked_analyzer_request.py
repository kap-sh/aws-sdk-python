"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#DeleteServiceLinkedAnalyzerRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.analyzer_name


class DeleteServiceLinkedAnalyzerRequest(TypedDict):
    analyzer_name: "aws_sdk_accessanalyzer.types.analyzer_name.AnalyzerName"
    """<p>The name of the service-linked analyzer to delete. Service-linked analyzer names follow the format <code>_AccessAnalyzerFor{ServiceName}-{Id}</code>.</p>"""
    client_token: NotRequired["str"]
    """<p>A client token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteServiceLinkedAnalyzerRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteServiceLinkedAnalyzerRequest:
    out: DeleteServiceLinkedAnalyzerRequest = {}  # type: ignore[typeddict-item]
    return out
