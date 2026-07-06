"""Generated from Smithy shape ``com.amazonaws.quicksight#Logo``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.alt_text
    import aws_sdk_quicksight.types.logo_set


class Logo(TypedDict, closed=True):
    alt_text: "aws_sdk_quicksight.types.alt_text.AltText"
    """<p>The alt text for the logo.</p>"""
    logo_set: "aws_sdk_quicksight.types.logo_set.LogoSet"
    """<p>A set of configured logos.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Logo) -> dict:
    out: dict = {}
    out["AltText"] = value["alt_text"]
    import aws_sdk_quicksight.types.logo_set

    out["LogoSet"] = aws_sdk_quicksight.types.logo_set.serialize_json(value["logo_set"])
    return out


def deserialize_json(data: dict) -> Logo:
    out: Logo = {}  # type: ignore[typeddict-item]
    if "AltText" in data:
        out["alt_text"] = data["AltText"]
    else:
        raise DeserializationError("Logo.alt_text required")
    if "LogoSet" in data:
        import aws_sdk_quicksight.types.logo_set

        out["logo_set"] = aws_sdk_quicksight.types.logo_set.deserialize_json(
            data["LogoSet"]
        )
    else:
        raise DeserializationError("Logo.logo_set required")
    return out
