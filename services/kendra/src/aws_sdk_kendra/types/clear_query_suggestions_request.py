"""Generated from Smithy shape ``com.amazonaws.kendra#ClearQuerySuggestionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kendra.types.index_id


class ClearQuerySuggestionsRequest(TypedDict, closed=True):
    index_id: "aws_sdk_kendra.types.index_id.IndexId"
    """<p>The identifier of the index you want to clear query suggestions from.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClearQuerySuggestionsRequest) -> dict:
    out: dict = {}
    out["IndexId"] = value["index_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ClearQuerySuggestionsRequest:
    out: ClearQuerySuggestionsRequest = {}  # type: ignore[typeddict-item]
    if "IndexId" in data:
        out["index_id"] = data["IndexId"]
    else:
        raise DeserializationError("ClearQuerySuggestionsRequest.index_id required")
    return out
