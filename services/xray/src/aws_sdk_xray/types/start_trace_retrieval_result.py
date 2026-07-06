"""Generated from Smithy shape ``com.amazonaws.xray#StartTraceRetrievalResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_xray.types.retrieval_token


class StartTraceRetrievalResult(TypedDict, closed=True):
    retrieval_token: NotRequired["aws_sdk_xray.types.retrieval_token.RetrievalToken"]
    """<p> Retrieval token. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartTraceRetrievalResult) -> dict:
    out: dict = {}
    if "retrieval_token" in value:
        out["RetrievalToken"] = value["retrieval_token"]
    return out


def deserialize_json(data: dict) -> StartTraceRetrievalResult:
    out: StartTraceRetrievalResult = {}  # type: ignore[typeddict-item]
    if "RetrievalToken" in data:
        out["retrieval_token"] = data["RetrievalToken"]
    return out
