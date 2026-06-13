"""Generated from Smithy shape ``com.amazonaws.mediaconnect#TransportStreamProgram``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.__list_of_transport_stream


class TransportStreamProgram(TypedDict):
    pcr_pid: NotRequired["int"]
    """<p> The Program Clock Reference (PCR) Packet ID (PID) as it is reported in the Program Association Table.</p>"""
    program_name: NotRequired["str"]
    """<p> The program name as it is reported in the Program Association Table.</p>"""
    program_number: NotRequired["int"]
    """<p> The program number as it is reported in the Program Association Table.</p>"""
    program_pid: NotRequired["int"]
    """<p> The program Packet ID (PID) as it is reported in the Program Association Table.</p>"""
    streams: NotRequired[
        "aws_sdk_mediaconnect.types.__list_of_transport_stream.__listOfTransportStream"
    ]
    """<p> The list of elementary transport streams in the program. The list includes video, audio, and data streams.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TransportStreamProgram) -> dict:
    out: dict = {}
    if "pcr_pid" in value:
        out["pcrPid"] = value["pcr_pid"]
    if "program_name" in value:
        out["programName"] = value["program_name"]
    if "program_number" in value:
        out["programNumber"] = value["program_number"]
    if "program_pid" in value:
        out["programPid"] = value["program_pid"]
    if "streams" in value:
        import aws_sdk_mediaconnect.types.__list_of_transport_stream

        out["streams"] = (
            aws_sdk_mediaconnect.types.__list_of_transport_stream.serialize_json(
                value["streams"]
            )
        )
    return out


def deserialize_json(data: dict) -> TransportStreamProgram:
    out: TransportStreamProgram = {}  # type: ignore[typeddict-item]
    if "pcrPid" in data:
        out["pcr_pid"] = data["pcrPid"]
    if "programName" in data:
        out["program_name"] = data["programName"]
    if "programNumber" in data:
        out["program_number"] = data["programNumber"]
    if "programPid" in data:
        out["program_pid"] = data["programPid"]
    if "streams" in data:
        import aws_sdk_mediaconnect.types.__list_of_transport_stream

        out["streams"] = (
            aws_sdk_mediaconnect.types.__list_of_transport_stream.deserialize_json(
                data["streams"]
            )
        )
    return out
