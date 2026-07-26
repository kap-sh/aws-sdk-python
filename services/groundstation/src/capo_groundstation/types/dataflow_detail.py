"""Generated from Smithy shape ``com.amazonaws.groundstation#DataflowDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_groundstation.types.destination
    import capo_groundstation.types.source


class DataflowDetail(TypedDict, closed=True):
    source: NotRequired["capo_groundstation.types.source.Source"]
    destination: NotRequired["capo_groundstation.types.destination.Destination"]
    error_message: NotRequired["str"]
    """<p>Error message for a dataflow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataflowDetail) -> dict:
    out: dict = {}
    if "source" in value:
        import capo_groundstation.types.source

        out["source"] = capo_groundstation.types.source.serialize_json(value["source"])
    if "destination" in value:
        import capo_groundstation.types.destination

        out["destination"] = capo_groundstation.types.destination.serialize_json(
            value["destination"]
        )
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> DataflowDetail:
    out: DataflowDetail = {}  # type: ignore[typeddict-item]
    if "source" in data:
        import capo_groundstation.types.source

        out["source"] = capo_groundstation.types.source.deserialize_json(data["source"])
    if "destination" in data:
        import capo_groundstation.types.destination

        out["destination"] = capo_groundstation.types.destination.deserialize_json(
            data["destination"]
        )
    if "errorMessage" in data:
        out["error_message"] = data["errorMessage"]
    return out
