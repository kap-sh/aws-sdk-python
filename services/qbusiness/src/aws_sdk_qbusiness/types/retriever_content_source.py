"""Generated from Smithy shape ``com.amazonaws.qbusiness#RetrieverContentSource``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_qbusiness.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.retriever_id


class RetrieverContentSource(TypedDict, closed=True):
    retriever_id: "aws_sdk_qbusiness.types.retriever_id.RetrieverId"
    """<p>The unique identifier of the retriever to use as the content source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RetrieverContentSource) -> dict:
    out: dict = {}
    out["retrieverId"] = value["retriever_id"]
    return out


def deserialize_json(data: dict) -> RetrieverContentSource:
    out: RetrieverContentSource = {}  # type: ignore[typeddict-item]
    if "retrieverId" in data:
        out["retriever_id"] = data["retrieverId"]
    else:
        raise DeserializationError("RetrieverContentSource.retriever_id required")
    return out
