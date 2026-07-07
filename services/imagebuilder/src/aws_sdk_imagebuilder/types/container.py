"""Generated from Smithy shape ``com.amazonaws.imagebuilder#Container``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.non_empty_string
    import aws_sdk_imagebuilder.types.string_list


class Container(TypedDict, closed=True):
    region: NotRequired["aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>Containers and container images are Region-specific. This is the Region context for the container.</p>"""
    image_uris: NotRequired["aws_sdk_imagebuilder.types.string_list.StringList"]
    """<p>A list of URIs for containers created in the context Region.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Container) -> dict:
    out: dict = {}
    if "region" in value:
        out["region"] = value["region"]
    if "image_uris" in value:
        import aws_sdk_imagebuilder.types.string_list

        out["imageUris"] = aws_sdk_imagebuilder.types.string_list.serialize_json(
            value["image_uris"]
        )
    return out


def deserialize_json(data: dict) -> Container:
    out: Container = {}  # type: ignore[typeddict-item]
    if "region" in data:
        out["region"] = data["region"]
    if "imageUris" in data:
        import aws_sdk_imagebuilder.types.string_list

        out["image_uris"] = aws_sdk_imagebuilder.types.string_list.deserialize_json(
            data["imageUris"]
        )
    return out
