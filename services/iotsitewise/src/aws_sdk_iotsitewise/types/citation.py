"""Generated from Smithy shape ``com.amazonaws.iotsitewise#Citation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.content
    import aws_sdk_iotsitewise.types.reference


class Citation(TypedDict, closed=True):
    reference: NotRequired["aws_sdk_iotsitewise.types.reference.Reference"]
    """<p>Contains information about the data source.</p>"""
    content: NotRequired["aws_sdk_iotsitewise.types.content.Content"]
    """<p>Contains the cited text from the data source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Citation) -> dict:
    out: dict = {}
    if "reference" in value:
        import aws_sdk_iotsitewise.types.reference

        out["reference"] = aws_sdk_iotsitewise.types.reference.serialize_json(
            value["reference"]
        )
    if "content" in value:
        import aws_sdk_iotsitewise.types.content

        out["content"] = aws_sdk_iotsitewise.types.content.serialize_json(
            value["content"]
        )
    return out


def deserialize_json(data: dict) -> Citation:
    out: Citation = {}  # type: ignore[typeddict-item]
    if "reference" in data:
        import aws_sdk_iotsitewise.types.reference

        out["reference"] = aws_sdk_iotsitewise.types.reference.deserialize_json(
            data["reference"]
        )
    if "content" in data:
        import aws_sdk_iotsitewise.types.content

        out["content"] = aws_sdk_iotsitewise.types.content.deserialize_json(
            data["content"]
        )
    return out
