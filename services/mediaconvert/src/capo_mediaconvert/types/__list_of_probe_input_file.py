"""Generated from Smithy shape ``com.amazonaws.mediaconvert#__listOfProbeInputFile``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediaconvert.types.probe_input_file

__listOfProbeInputFile: TypeAlias = list[
    "capo_mediaconvert.types.probe_input_file.ProbeInputFile"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfProbeInputFile) -> list:
    import capo_mediaconvert.types.probe_input_file

    out: list = []
    for item in value:
        out.append(capo_mediaconvert.types.probe_input_file.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfProbeInputFile:
    import capo_mediaconvert.types.probe_input_file

    out: __listOfProbeInputFile = []
    for item in data:
        out.append(capo_mediaconvert.types.probe_input_file.deserialize_json(item))
    return out
