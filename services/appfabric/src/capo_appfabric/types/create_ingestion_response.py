"""Generated from Smithy shape ``com.amazonaws.appfabric#CreateIngestionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_appfabric.errors import DeserializationError

if TYPE_CHECKING:
    import capo_appfabric.types.ingestion


class CreateIngestionResponse(TypedDict, closed=True):
    ingestion: "capo_appfabric.types.ingestion.Ingestion"
    """<p>Contains information about an ingestion.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateIngestionResponse) -> dict:
    out: dict = {}
    import capo_appfabric.types.ingestion

    out["ingestion"] = capo_appfabric.types.ingestion.serialize_json(value["ingestion"])
    return out


def deserialize_json(data: dict) -> CreateIngestionResponse:
    out: CreateIngestionResponse = {}  # type: ignore[typeddict-item]
    if "ingestion" in data:
        import capo_appfabric.types.ingestion

        out["ingestion"] = capo_appfabric.types.ingestion.deserialize_json(
            data["ingestion"]
        )
    else:
        raise DeserializationError("CreateIngestionResponse.ingestion required")
    return out
