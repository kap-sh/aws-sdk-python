"""Generated from Smithy shape ``com.amazonaws.mediaconvert#ProbeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__list_of_probe_input_file


class ProbeRequest(TypedDict, closed=True):
    input_files: NotRequired[
        "aws_sdk_mediaconvert.types.__list_of_probe_input_file.__listOfProbeInputFile"
    ]
    """Specify a media file to probe."""


# --- restJson1 ser/de ---
def serialize_json(value: ProbeRequest) -> dict:
    out: dict = {}
    if "input_files" in value:
        import aws_sdk_mediaconvert.types.__list_of_probe_input_file

        out["inputFiles"] = (
            aws_sdk_mediaconvert.types.__list_of_probe_input_file.serialize_json(
                value["input_files"]
            )
        )
    return out


def deserialize_json(data: dict) -> ProbeRequest:
    out: ProbeRequest = {}  # type: ignore[typeddict-item]
    if "inputFiles" in data:
        import aws_sdk_mediaconvert.types.__list_of_probe_input_file

        out["input_files"] = (
            aws_sdk_mediaconvert.types.__list_of_probe_input_file.deserialize_json(
                data["inputFiles"]
            )
        )
    return out
