"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ContainerRecipeSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.container_type
    import aws_sdk_imagebuilder.types.date_time
    import aws_sdk_imagebuilder.types.image_builder_arn
    import aws_sdk_imagebuilder.types.non_empty_string
    import aws_sdk_imagebuilder.types.platform
    import aws_sdk_imagebuilder.types.resource_name
    import aws_sdk_imagebuilder.types.tag_map


class ContainerRecipeSummary(TypedDict):
    arn: NotRequired["aws_sdk_imagebuilder.types.image_builder_arn.ImageBuilderArn"]
    """<p>The Amazon Resource Name (ARN) of the container recipe.</p>"""
    container_type: NotRequired[
        "aws_sdk_imagebuilder.types.container_type.ContainerType"
    ]
    r"""<p>Specifies the type of container, such as \"Docker\".</p>"""
    name: NotRequired["aws_sdk_imagebuilder.types.resource_name.ResourceName"]
    """<p>The name of the container recipe.</p>"""
    platform: NotRequired["aws_sdk_imagebuilder.types.platform.Platform"]
    """<p>The system platform for the container, such as Windows or Linux.</p>"""
    owner: NotRequired["aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The owner of the container recipe.</p>"""
    parent_image: NotRequired[
        "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    """<p>The base image for the container recipe.</p>"""
    date_created: NotRequired["aws_sdk_imagebuilder.types.date_time.DateTime"]
    """<p>The date when this container recipe was created.</p>"""
    instance_image: NotRequired[
        "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    """<p>The base image for a container build and test instance. This can contain an AMI ID or it can specify an Amazon Web Services Systems Manager (SSM) Parameter Store Parameter, prefixed by <code>ssm:</code>, followed by the parameter name or ARN.</p> <p>If not specified, Image Builder uses the appropriate ECS-optimized AMI as a base image.</p>"""
    tags: NotRequired["aws_sdk_imagebuilder.types.tag_map.TagMap"]
    """<p>Tags that are attached to the container recipe.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContainerRecipeSummary) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "container_type" in value:
        import aws_sdk_imagebuilder.types.container_type

        out["containerType"] = aws_sdk_imagebuilder.types.container_type.serialize_json(
            value["container_type"]
        )
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
    if "instance_image" in value:
        out["instanceImage"] = value["instance_image"]
    if "tags" in value:
        import aws_sdk_imagebuilder.types.tag_map

        out["tags"] = aws_sdk_imagebuilder.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> ContainerRecipeSummary:
    out: ContainerRecipeSummary = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "containerType" in data:
        import aws_sdk_imagebuilder.types.container_type

        out["container_type"] = (
            aws_sdk_imagebuilder.types.container_type.deserialize_json(
                data["containerType"]
            )
        )
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
    if "instanceImage" in data:
        out["instance_image"] = data["instanceImage"]
    if "tags" in data:
        import aws_sdk_imagebuilder.types.tag_map

        out["tags"] = aws_sdk_imagebuilder.types.tag_map.deserialize_json(data["tags"])
    return out
