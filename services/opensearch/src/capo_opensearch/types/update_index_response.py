"""Generated from Smithy shape ``com.amazonaws.opensearch#UpdateIndexResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_opensearch.errors import DeserializationError

if TYPE_CHECKING:
    import capo_opensearch.types.index_status


class UpdateIndexResponse(TypedDict, closed=True):
    status: "capo_opensearch.types.index_status.IndexStatus"
    """<p>The status of the index update operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateIndexResponse) -> dict:
    out: dict = {}
    import capo_opensearch.types.index_status

    out["Status"] = capo_opensearch.types.index_status.serialize_json(value["status"])
    return out


def deserialize_json(data: dict) -> UpdateIndexResponse:
    out: UpdateIndexResponse = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        import capo_opensearch.types.index_status

        out["status"] = capo_opensearch.types.index_status.deserialize_json(
            data["Status"]
        )
    else:
        raise DeserializationError("UpdateIndexResponse.status required")
    return out
