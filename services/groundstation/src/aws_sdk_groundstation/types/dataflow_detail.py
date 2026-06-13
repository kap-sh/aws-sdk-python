"""Generated from Smithy shape ``com.amazonaws.groundstation#DataflowDetail``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.destination
    import aws_sdk_groundstation.types.source


class DataflowDetail(TypedDict):
    source: NotRequired["aws_sdk_groundstation.types.source.Source"]
    destination: NotRequired["aws_sdk_groundstation.types.destination.Destination"]
    error_message: NotRequired["str"]
    """<p>Error message for a dataflow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataflowDetail) -> dict:
    out: dict = {}
    if "source" in value:
        import aws_sdk_groundstation.types.source

        out["source"] = aws_sdk_groundstation.types.source.serialize_json(
            value["source"]
        )
    if "destination" in value:
        import aws_sdk_groundstation.types.destination

        out["destination"] = aws_sdk_groundstation.types.destination.serialize_json(
            value["destination"]
        )
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> DataflowDetail:
    out: DataflowDetail = {}  # type: ignore[typeddict-item]
    if "source" in data:
        import aws_sdk_groundstation.types.source

        out["source"] = aws_sdk_groundstation.types.source.deserialize_json(
            data["source"]
        )
    if "destination" in data:
        import aws_sdk_groundstation.types.destination

        out["destination"] = aws_sdk_groundstation.types.destination.deserialize_json(
            data["destination"]
        )
    if "errorMessage" in data:
        out["error_message"] = data["errorMessage"]
    return out
