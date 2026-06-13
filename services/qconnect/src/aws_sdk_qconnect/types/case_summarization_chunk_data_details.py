"""Generated from Smithy shape ``com.amazonaws.qconnect#CaseSummarizationChunkDataDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.next_token
    import aws_sdk_qconnect.types.non_empty_sensitive_string


class CaseSummarizationChunkDataDetails(TypedDict):
    completion: NotRequired[
        "aws_sdk_qconnect.types.non_empty_sensitive_string.NonEmptySensitiveString"
    ]
    """<p>A chunk of the case summarization completion.</p>"""
    next_chunk_token: NotRequired["aws_sdk_qconnect.types.next_token.NextToken"]
    """<p>Token for retrieving the next chunk of streaming summarization data, if available.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CaseSummarizationChunkDataDetails) -> dict:
    out: dict = {}
    if "completion" in value:
        out["completion"] = value["completion"]
    if "next_chunk_token" in value:
        out["nextChunkToken"] = value["next_chunk_token"]
    return out


def deserialize_json(data: dict) -> CaseSummarizationChunkDataDetails:
    out: CaseSummarizationChunkDataDetails = {}  # type: ignore[typeddict-item]
    if "completion" in data:
        out["completion"] = data["completion"]
    if "nextChunkToken" in data:
        out["next_chunk_token"] = data["nextChunkToken"]
    return out
