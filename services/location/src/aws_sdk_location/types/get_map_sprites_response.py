"""Generated from Smithy shape ``com.amazonaws.location#GetMapSpritesResponse``."""

from typing_extensions import NotRequired, TypedDict


class GetMapSpritesResponse(TypedDict, closed=True):
    blob: NotRequired["bytes"]
    """<p>Contains the body of the sprite sheet or JSON offset ﬁle.</p>"""
    content_type: NotRequired["str"]
    """<p>The content type of the sprite sheet and offsets. For example, the sprite sheet content type is <code>image/png</code>, and the sprite offset JSON document is <code>application/json</code>. </p>"""
    cache_control: NotRequired["str"]
    """<p>The HTTP Cache-Control directive for the value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMapSpritesResponse) -> dict:
    out: dict = {}
    if "blob" in value:
        import aws_sdk_location.types._prelude.blob

        out["Blob"] = aws_sdk_location.types._prelude.blob.serialize_json(value["blob"])
    return out


def deserialize_json(data: dict) -> GetMapSpritesResponse:
    out: GetMapSpritesResponse = {}  # type: ignore[typeddict-item]
    if "Blob" in data:
        import aws_sdk_location.types._prelude.blob

        out["blob"] = aws_sdk_location.types._prelude.blob.deserialize_json(
            data["Blob"]
        )
    return out
