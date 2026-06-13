"""Generated from Smithy shape ``com.amazonaws.quicksight#LogoSetConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.image_set_configuration


class LogoSetConfiguration(TypedDict):
    primary: "aws_sdk_quicksight.types.image_set_configuration.ImageSetConfiguration"
    """<p>The primary logo.</p>"""
    favicon: NotRequired[
        "aws_sdk_quicksight.types.image_set_configuration.ImageSetConfiguration"
    ]
    """<p>The favicon logo.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LogoSetConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_quicksight.types.image_set_configuration

    out["Primary"] = aws_sdk_quicksight.types.image_set_configuration.serialize_json(
        value["primary"]
    )
    if "favicon" in value:
        import aws_sdk_quicksight.types.image_set_configuration

        out["Favicon"] = (
            aws_sdk_quicksight.types.image_set_configuration.serialize_json(
                value["favicon"]
            )
        )
    return out


def deserialize_json(data: dict) -> LogoSetConfiguration:
    out: LogoSetConfiguration = {}  # type: ignore[typeddict-item]
    if "Primary" in data:
        import aws_sdk_quicksight.types.image_set_configuration

        out["primary"] = (
            aws_sdk_quicksight.types.image_set_configuration.deserialize_json(
                data["Primary"]
            )
        )
    else:
        raise DeserializationError("LogoSetConfiguration.primary required")
    if "Favicon" in data:
        import aws_sdk_quicksight.types.image_set_configuration

        out["favicon"] = (
            aws_sdk_quicksight.types.image_set_configuration.deserialize_json(
                data["Favicon"]
            )
        )
    return out
