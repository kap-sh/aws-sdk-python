"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#UpdateIngestConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ivs_realtime.types.ingest_configuration


class UpdateIngestConfigurationResponse(TypedDict, closed=True):
    ingest_configuration: NotRequired[
        "capo_ivs_realtime.types.ingest_configuration.IngestConfiguration"
    ]
    """<p>The updated IngestConfiguration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateIngestConfigurationResponse) -> dict:
    out: dict = {}
    if "ingest_configuration" in value:
        import capo_ivs_realtime.types.ingest_configuration

        out["ingestConfiguration"] = (
            capo_ivs_realtime.types.ingest_configuration.serialize_json(
                value["ingest_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateIngestConfigurationResponse:
    out: UpdateIngestConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "ingestConfiguration" in data:
        import capo_ivs_realtime.types.ingest_configuration

        out["ingest_configuration"] = (
            capo_ivs_realtime.types.ingest_configuration.deserialize_json(
                data["ingestConfiguration"]
            )
        )
    return out
