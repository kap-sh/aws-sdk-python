"""Generated from Smithy shape ``com.amazonaws.connect#WorkspaceThemeImages``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.images_logo


class WorkspaceThemeImages(TypedDict, closed=True):
    logo: NotRequired["aws_sdk_connect.types.images_logo.ImagesLogo"]
    """<p>The logo images used in the workspace.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WorkspaceThemeImages) -> dict:
    out: dict = {}
    if "logo" in value:
        import aws_sdk_connect.types.images_logo

        out["Logo"] = aws_sdk_connect.types.images_logo.serialize_json(value["logo"])
    return out


def deserialize_json(data: dict) -> WorkspaceThemeImages:
    out: WorkspaceThemeImages = {}  # type: ignore[typeddict-item]
    if "Logo" in data:
        import aws_sdk_connect.types.images_logo

        out["logo"] = aws_sdk_connect.types.images_logo.deserialize_json(data["Logo"])
    return out
