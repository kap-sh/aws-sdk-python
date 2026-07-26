"""Generated from Smithy shape ``com.amazonaws.quicksight#LogoSetConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.image_set_configuration


class LogoSetConfiguration(TypedDict, closed=True):
    primary: "capo_quicksight.types.image_set_configuration.ImageSetConfiguration"
    """<p>The primary logo.</p>"""
    favicon: NotRequired[
        "capo_quicksight.types.image_set_configuration.ImageSetConfiguration"
    ]
    """<p>The favicon logo.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LogoSetConfiguration) -> dict:
    out: dict = {}
    import capo_quicksight.types.image_set_configuration

    out["Primary"] = capo_quicksight.types.image_set_configuration.serialize_json(
        value["primary"]
    )
    if "favicon" in value:
        import capo_quicksight.types.image_set_configuration

        out["Favicon"] = capo_quicksight.types.image_set_configuration.serialize_json(
            value["favicon"]
        )
    return out


def deserialize_json(data: dict) -> LogoSetConfiguration:
    out: LogoSetConfiguration = {}  # type: ignore[typeddict-item]
    if "Primary" in data:
        import capo_quicksight.types.image_set_configuration

        out["primary"] = capo_quicksight.types.image_set_configuration.deserialize_json(
            data["Primary"]
        )
    else:
        raise DeserializationError("LogoSetConfiguration.primary required")
    if "Favicon" in data:
        import capo_quicksight.types.image_set_configuration

        out["favicon"] = capo_quicksight.types.image_set_configuration.deserialize_json(
            data["Favicon"]
        )
    return out
