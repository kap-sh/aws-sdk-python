"""Generated from Smithy shape ``com.amazonaws.iotsitewise#Citation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.content
    import capo_iotsitewise.types.reference


class Citation(TypedDict, closed=True):
    reference: NotRequired["capo_iotsitewise.types.reference.Reference"]
    """<p>Contains information about the data source.</p>"""
    content: NotRequired["capo_iotsitewise.types.content.Content"]
    """<p>Contains the cited text from the data source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Citation) -> dict:
    out: dict = {}
    if "reference" in value:
        import capo_iotsitewise.types.reference

        out["reference"] = capo_iotsitewise.types.reference.serialize_json(
            value["reference"]
        )
    if "content" in value:
        import capo_iotsitewise.types.content

        out["content"] = capo_iotsitewise.types.content.serialize_json(value["content"])
    return out


def deserialize_json(data: dict) -> Citation:
    out: Citation = {}  # type: ignore[typeddict-item]
    if "reference" in data:
        import capo_iotsitewise.types.reference

        out["reference"] = capo_iotsitewise.types.reference.deserialize_json(
            data["reference"]
        )
    if "content" in data:
        import capo_iotsitewise.types.content

        out["content"] = capo_iotsitewise.types.content.deserialize_json(
            data["content"]
        )
    return out
