"""Generated from Smithy shape ``com.amazonaws.dataexchange#Event``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dataexchange.types.revision_published


class Event(TypedDict):
    revision_published: NotRequired[
        "aws_sdk_dataexchange.types.revision_published.RevisionPublished"
    ]
    """<p>What occurs to start the revision publish action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Event) -> dict:
    out: dict = {}
    if "revision_published" in value:
        import aws_sdk_dataexchange.types.revision_published

        out["RevisionPublished"] = (
            aws_sdk_dataexchange.types.revision_published.serialize_json(
                value["revision_published"]
            )
        )
    return out


def deserialize_json(data: dict) -> Event:
    out: Event = {}  # type: ignore[typeddict-item]
    if "RevisionPublished" in data:
        import aws_sdk_dataexchange.types.revision_published

        out["revision_published"] = (
            aws_sdk_dataexchange.types.revision_published.deserialize_json(
                data["RevisionPublished"]
            )
        )
    return out
