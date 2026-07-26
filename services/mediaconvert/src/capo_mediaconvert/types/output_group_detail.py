"""Generated from Smithy shape ``com.amazonaws.mediaconvert#OutputGroupDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.__list_of_output_detail


class OutputGroupDetail(TypedDict, closed=True):
    output_details: NotRequired[
        "capo_mediaconvert.types.__list_of_output_detail.__listOfOutputDetail"
    ]
    """Details about the output"""


# --- restJson1 ser/de ---
def serialize_json(value: OutputGroupDetail) -> dict:
    out: dict = {}
    if "output_details" in value:
        import capo_mediaconvert.types.__list_of_output_detail

        out["outputDetails"] = (
            capo_mediaconvert.types.__list_of_output_detail.serialize_json(
                value["output_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> OutputGroupDetail:
    out: OutputGroupDetail = {}  # type: ignore[typeddict-item]
    if "outputDetails" in data:
        import capo_mediaconvert.types.__list_of_output_detail

        out["output_details"] = (
            capo_mediaconvert.types.__list_of_output_detail.deserialize_json(
                data["outputDetails"]
            )
        )
    return out
