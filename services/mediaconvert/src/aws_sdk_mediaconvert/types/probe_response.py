"""Generated from Smithy shape ``com.amazonaws.mediaconvert#ProbeResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__list_of_probe_result


class ProbeResponse(TypedDict, closed=True):
    probe_results: NotRequired[
        "aws_sdk_mediaconvert.types.__list_of_probe_result.__listOfProbeResult"
    ]
    """Probe results for your media file."""


# --- restJson1 ser/de ---
def serialize_json(value: ProbeResponse) -> dict:
    out: dict = {}
    if "probe_results" in value:
        import aws_sdk_mediaconvert.types.__list_of_probe_result

        out["probeResults"] = (
            aws_sdk_mediaconvert.types.__list_of_probe_result.serialize_json(
                value["probe_results"]
            )
        )
    return out


def deserialize_json(data: dict) -> ProbeResponse:
    out: ProbeResponse = {}  # type: ignore[typeddict-item]
    if "probeResults" in data:
        import aws_sdk_mediaconvert.types.__list_of_probe_result

        out["probe_results"] = (
            aws_sdk_mediaconvert.types.__list_of_probe_result.deserialize_json(
                data["probeResults"]
            )
        )
    return out
