"""Generated from Smithy shape ``com.amazonaws.medialive#Scte35TimeSignalScheduleActionSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__list_of_scte35_descriptor


class Scte35TimeSignalScheduleActionSettings(TypedDict):
    scte35_descriptors: NotRequired[
        "aws_sdk_medialive.types.__list_of_scte35_descriptor.__listOfScte35Descriptor"
    ]
    """The list of SCTE-35 descriptors accompanying the SCTE-35 time_signal."""


# --- restJson1 ser/de ---
def serialize_json(value: Scte35TimeSignalScheduleActionSettings) -> dict:
    out: dict = {}
    if "scte35_descriptors" in value:
        import aws_sdk_medialive.types.__list_of_scte35_descriptor

        out["scte35Descriptors"] = (
            aws_sdk_medialive.types.__list_of_scte35_descriptor.serialize_json(
                value["scte35_descriptors"]
            )
        )
    return out


def deserialize_json(data: dict) -> Scte35TimeSignalScheduleActionSettings:
    out: Scte35TimeSignalScheduleActionSettings = {}  # type: ignore[typeddict-item]
    if "scte35Descriptors" in data:
        import aws_sdk_medialive.types.__list_of_scte35_descriptor

        out["scte35_descriptors"] = (
            aws_sdk_medialive.types.__list_of_scte35_descriptor.deserialize_json(
                data["scte35Descriptors"]
            )
        )
    return out
