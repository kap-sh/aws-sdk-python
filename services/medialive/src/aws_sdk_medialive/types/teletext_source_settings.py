"""Generated from Smithy shape ``com.amazonaws.medialive#TeletextSourceSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string
    import aws_sdk_medialive.types.caption_rectangle


class TeletextSourceSettings(TypedDict):
    output_rectangle: NotRequired[
        "aws_sdk_medialive.types.caption_rectangle.CaptionRectangle"
    ]
    """Optionally defines a region where TTML style captions will be displayed"""
    page_number: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """Specifies the teletext page number within the data stream from which to extract captions. Range of 0x100 (256) to 0x8FF (2303). Unused for passthrough. Should be specified as a hexadecimal string with no \"0x\" prefix."""


# --- restJson1 ser/de ---
def serialize_json(value: TeletextSourceSettings) -> dict:
    out: dict = {}
    if "output_rectangle" in value:
        import aws_sdk_medialive.types.caption_rectangle

        out["outputRectangle"] = (
            aws_sdk_medialive.types.caption_rectangle.serialize_json(
                value["output_rectangle"]
            )
        )
    if "page_number" in value:
        out["pageNumber"] = value["page_number"]
    return out


def deserialize_json(data: dict) -> TeletextSourceSettings:
    out: TeletextSourceSettings = {}  # type: ignore[typeddict-item]
    if "outputRectangle" in data:
        import aws_sdk_medialive.types.caption_rectangle

        out["output_rectangle"] = (
            aws_sdk_medialive.types.caption_rectangle.deserialize_json(
                data["outputRectangle"]
            )
        )
    if "pageNumber" in data:
        out["page_number"] = data["pageNumber"]
    return out
