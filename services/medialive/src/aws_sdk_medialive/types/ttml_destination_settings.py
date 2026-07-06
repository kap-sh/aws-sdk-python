"""Generated from Smithy shape ``com.amazonaws.medialive#TtmlDestinationSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.ttml_destination_style_control


class TtmlDestinationSettings(TypedDict, closed=True):
    style_control: NotRequired[
        "aws_sdk_medialive.types.ttml_destination_style_control.TtmlDestinationStyleControl"
    ]
    """This field is not currently supported and will not affect the output styling. Leave the default value."""


# --- restJson1 ser/de ---
def serialize_json(value: TtmlDestinationSettings) -> dict:
    out: dict = {}
    if "style_control" in value:
        import aws_sdk_medialive.types.ttml_destination_style_control

        out["styleControl"] = (
            aws_sdk_medialive.types.ttml_destination_style_control.serialize_json(
                value["style_control"]
            )
        )
    return out


def deserialize_json(data: dict) -> TtmlDestinationSettings:
    out: TtmlDestinationSettings = {}  # type: ignore[typeddict-item]
    if "styleControl" in data:
        import aws_sdk_medialive.types.ttml_destination_style_control

        out["style_control"] = (
            aws_sdk_medialive.types.ttml_destination_style_control.deserialize_json(
                data["styleControl"]
            )
        )
    return out
