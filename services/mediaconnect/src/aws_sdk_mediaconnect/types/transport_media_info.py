"""Generated from Smithy shape ``com.amazonaws.mediaconnect#TransportMediaInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.__list_of_transport_stream_program


class TransportMediaInfo(TypedDict):
    programs: NotRequired[
        "aws_sdk_mediaconnect.types.__list_of_transport_stream_program.__listOfTransportStreamProgram"
    ]
    """<p> The list of transport stream programs in the current flow's source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TransportMediaInfo) -> dict:
    out: dict = {}
    if "programs" in value:
        import aws_sdk_mediaconnect.types.__list_of_transport_stream_program

        out["programs"] = (
            aws_sdk_mediaconnect.types.__list_of_transport_stream_program.serialize_json(
                value["programs"]
            )
        )
    return out


def deserialize_json(data: dict) -> TransportMediaInfo:
    out: TransportMediaInfo = {}  # type: ignore[typeddict-item]
    if "programs" in data:
        import aws_sdk_mediaconnect.types.__list_of_transport_stream_program

        out["programs"] = (
            aws_sdk_mediaconnect.types.__list_of_transport_stream_program.deserialize_json(
                data["programs"]
            )
        )
    return out
