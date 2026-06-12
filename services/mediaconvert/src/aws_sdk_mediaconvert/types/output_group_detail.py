"""Generated from Smithy shape ``com.amazonaws.mediaconvert#OutputGroupDetail``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__list_of_output_detail


class OutputGroupDetail(TypedDict):
    output_details: NotRequired[
        "aws_sdk_mediaconvert.types.__list_of_output_detail.__listOfOutputDetail"
    ]
    """Details about the output"""


# --- restJson1 ser/de ---
def serialize_json(value: OutputGroupDetail) -> dict:
    out: dict = {}
    if "output_details" in value:
        import aws_sdk_mediaconvert.types.__list_of_output_detail

        out["outputDetails"] = (
            aws_sdk_mediaconvert.types.__list_of_output_detail.serialize_json(
                value["output_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> OutputGroupDetail:
    out: OutputGroupDetail = {}  # type: ignore[typeddict-item]
    if "outputDetails" in data:
        import aws_sdk_mediaconvert.types.__list_of_output_detail

        out["output_details"] = (
            aws_sdk_mediaconvert.types.__list_of_output_detail.deserialize_json(
                data["outputDetails"]
            )
        )
    return out
