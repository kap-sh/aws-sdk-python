"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ImageRecipeSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.date_time
    import aws_sdk_imagebuilder.types.image_builder_arn
    import aws_sdk_imagebuilder.types.non_empty_string
    import aws_sdk_imagebuilder.types.platform
    import aws_sdk_imagebuilder.types.resource_name
    import aws_sdk_imagebuilder.types.tag_map


class ImageRecipeSummary(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_imagebuilder.types.image_builder_arn.ImageBuilderArn"]
    """<p>The Amazon Resource Name (ARN) of the image recipe.</p>"""
    name: NotRequired["aws_sdk_imagebuilder.types.resource_name.ResourceName"]
    """<p>The name of the image recipe.</p>"""
    platform: NotRequired["aws_sdk_imagebuilder.types.platform.Platform"]
    """<p>The platform of the image recipe.</p>"""
    owner: NotRequired["aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The owner of the image recipe.</p>"""
    parent_image: NotRequired[
        "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    """<p>The base image of the image recipe.</p>"""
    date_created: NotRequired["aws_sdk_imagebuilder.types.date_time.DateTime"]
    """<p>The date on which this image recipe was created.</p>"""
    tags: NotRequired["aws_sdk_imagebuilder.types.tag_map.TagMap"]
    """<p>The tags of the image recipe.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImageRecipeSummary) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "platform" in value:
        import aws_sdk_imagebuilder.types.platform

        out["platform"] = aws_sdk_imagebuilder.types.platform.serialize_json(
            value["platform"]
        )
    if "owner" in value:
        out["owner"] = value["owner"]
    if "parent_image" in value:
        out["parentImage"] = value["parent_image"]
    if "date_created" in value:
        out["dateCreated"] = value["date_created"]
    if "tags" in value:
        import aws_sdk_imagebuilder.types.tag_map

        out["tags"] = aws_sdk_imagebuilder.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> ImageRecipeSummary:
    out: ImageRecipeSummary = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "name" in data:
        out["name"] = data["name"]
    if "platform" in data:
        import aws_sdk_imagebuilder.types.platform

        out["platform"] = aws_sdk_imagebuilder.types.platform.deserialize_json(
            data["platform"]
        )
    if "owner" in data:
        out["owner"] = data["owner"]
    if "parentImage" in data:
        out["parent_image"] = data["parentImage"]
    if "dateCreated" in data:
        out["date_created"] = data["dateCreated"]
    if "tags" in data:
        import aws_sdk_imagebuilder.types.tag_map

        out["tags"] = aws_sdk_imagebuilder.types.tag_map.deserialize_json(data["tags"])
    return out
