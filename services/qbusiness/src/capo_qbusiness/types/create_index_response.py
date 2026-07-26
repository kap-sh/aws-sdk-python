"""Generated from Smithy shape ``com.amazonaws.qbusiness#CreateIndexResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.index_arn
    import capo_qbusiness.types.index_id


class CreateIndexResponse(TypedDict, closed=True):
    index_id: NotRequired["capo_qbusiness.types.index_id.IndexId"]
    """<p>The identifier for the Amazon Q Business index.</p>"""
    index_arn: NotRequired["capo_qbusiness.types.index_arn.IndexArn"]
    """<p> The Amazon Resource Name (ARN) of an Amazon Q Business index.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateIndexResponse) -> dict:
    out: dict = {}
    if "index_id" in value:
        out["indexId"] = value["index_id"]
    if "index_arn" in value:
        out["indexArn"] = value["index_arn"]
    return out


def deserialize_json(data: dict) -> CreateIndexResponse:
    out: CreateIndexResponse = {}  # type: ignore[typeddict-item]
    if "indexId" in data:
        out["index_id"] = data["indexId"]
    if "indexArn" in data:
        out["index_arn"] = data["indexArn"]
    return out
