"""Generated from Smithy shape ``com.amazonaws.qconnect#EmailGenerativeAnswerChunkDataDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.data_summary_list
    import aws_sdk_qconnect.types.next_token
    import aws_sdk_qconnect.types.non_empty_sensitive_string


class EmailGenerativeAnswerChunkDataDetails(TypedDict, closed=True):
    completion: NotRequired[
        "aws_sdk_qconnect.types.non_empty_sensitive_string.NonEmptySensitiveString"
    ]
    """<p>The partial or complete text content of the generative answer response.</p>"""
    references: NotRequired["aws_sdk_qconnect.types.data_summary_list.DataSummaryList"]
    """<p>Source references and citations from knowledge base articles used to generate the answer.</p>"""
    next_chunk_token: NotRequired["aws_sdk_qconnect.types.next_token.NextToken"]
    """<p>Token for retrieving the next chunk of streaming response data, if available.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EmailGenerativeAnswerChunkDataDetails) -> dict:
    out: dict = {}
    if "completion" in value:
        out["completion"] = value["completion"]
    if "references" in value:
        import aws_sdk_qconnect.types.data_summary_list

        out["references"] = aws_sdk_qconnect.types.data_summary_list.serialize_json(
            value["references"]
        )
    if "next_chunk_token" in value:
        out["nextChunkToken"] = value["next_chunk_token"]
    return out


def deserialize_json(data: dict) -> EmailGenerativeAnswerChunkDataDetails:
    out: EmailGenerativeAnswerChunkDataDetails = {}  # type: ignore[typeddict-item]
    if "completion" in data:
        out["completion"] = data["completion"]
    if "references" in data:
        import aws_sdk_qconnect.types.data_summary_list

        out["references"] = aws_sdk_qconnect.types.data_summary_list.deserialize_json(
            data["references"]
        )
    if "nextChunkToken" in data:
        out["next_chunk_token"] = data["nextChunkToken"]
    return out
