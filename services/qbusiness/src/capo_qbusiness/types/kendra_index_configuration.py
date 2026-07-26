"""Generated from Smithy shape ``com.amazonaws.qbusiness#KendraIndexConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_qbusiness.errors import DeserializationError

if TYPE_CHECKING:
    import capo_qbusiness.types.kendra_index_id


class KendraIndexConfiguration(TypedDict, closed=True):
    index_id: "capo_qbusiness.types.kendra_index_id.KendraIndexId"
    """<p>The identifier of the Amazon Kendra index.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KendraIndexConfiguration) -> dict:
    out: dict = {}
    out["indexId"] = value["index_id"]
    return out


def deserialize_json(data: dict) -> KendraIndexConfiguration:
    out: KendraIndexConfiguration = {}  # type: ignore[typeddict-item]
    if "indexId" in data:
        out["index_id"] = data["indexId"]
    else:
        raise DeserializationError("KendraIndexConfiguration.index_id required")
    return out
