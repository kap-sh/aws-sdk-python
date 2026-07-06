"""Generated from Smithy shape ``com.amazonaws.mediatailor#AudienceMedia``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.__list_of_alternate_media
    import aws_sdk_mediatailor.types.__string


class AudienceMedia(TypedDict, closed=True):
    audience: NotRequired["aws_sdk_mediatailor.types.__string.__string"]
    """<p>The Audience defined in AudienceMedia.</p>"""
    alternate_media: NotRequired[
        "aws_sdk_mediatailor.types.__list_of_alternate_media.__listOfAlternateMedia"
    ]
    """<p>The list of AlternateMedia defined in AudienceMedia.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AudienceMedia) -> dict:
    out: dict = {}
    if "audience" in value:
        out["Audience"] = value["audience"]
    if "alternate_media" in value:
        import aws_sdk_mediatailor.types.__list_of_alternate_media

        out["AlternateMedia"] = (
            aws_sdk_mediatailor.types.__list_of_alternate_media.serialize_json(
                value["alternate_media"]
            )
        )
    return out


def deserialize_json(data: dict) -> AudienceMedia:
    out: AudienceMedia = {}  # type: ignore[typeddict-item]
    if "Audience" in data:
        out["audience"] = data["Audience"]
    if "AlternateMedia" in data:
        import aws_sdk_mediatailor.types.__list_of_alternate_media

        out["alternate_media"] = (
            aws_sdk_mediatailor.types.__list_of_alternate_media.deserialize_json(
                data["AlternateMedia"]
            )
        )
    return out
