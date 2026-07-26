"""Generated from Smithy shape ``com.amazonaws.quicksight#LogoSet``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.image_set


class LogoSet(TypedDict, closed=True):
    primary: "capo_quicksight.types.image_set.ImageSet"
    """<p>The primary logo.</p>"""
    favicon: NotRequired["capo_quicksight.types.image_set.ImageSet"]
    """<p>The favicon logo.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LogoSet) -> dict:
    out: dict = {}
    import capo_quicksight.types.image_set

    out["Primary"] = capo_quicksight.types.image_set.serialize_json(value["primary"])
    if "favicon" in value:
        import capo_quicksight.types.image_set

        out["Favicon"] = capo_quicksight.types.image_set.serialize_json(
            value["favicon"]
        )
    return out


def deserialize_json(data: dict) -> LogoSet:
    out: LogoSet = {}  # type: ignore[typeddict-item]
    if "Primary" in data:
        import capo_quicksight.types.image_set

        out["primary"] = capo_quicksight.types.image_set.deserialize_json(
            data["Primary"]
        )
    else:
        raise DeserializationError("LogoSet.primary required")
    if "Favicon" in data:
        import capo_quicksight.types.image_set

        out["favicon"] = capo_quicksight.types.image_set.deserialize_json(
            data["Favicon"]
        )
    return out
