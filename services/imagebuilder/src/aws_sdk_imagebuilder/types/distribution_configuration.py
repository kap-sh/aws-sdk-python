"""Generated from Smithy shape ``com.amazonaws.imagebuilder#DistributionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_imagebuilder.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.date_time
    import aws_sdk_imagebuilder.types.distribution_list
    import aws_sdk_imagebuilder.types.distribution_timeout_minutes
    import aws_sdk_imagebuilder.types.image_builder_arn
    import aws_sdk_imagebuilder.types.non_empty_string
    import aws_sdk_imagebuilder.types.resource_name
    import aws_sdk_imagebuilder.types.tag_map


class DistributionConfiguration(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_imagebuilder.types.image_builder_arn.ImageBuilderArn"]
    """<p>The Amazon Resource Name (ARN) of the distribution configuration.</p>"""
    name: NotRequired["aws_sdk_imagebuilder.types.resource_name.ResourceName"]
    """<p>The name of the distribution configuration.</p>"""
    description: NotRequired[
        "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    """<p>The description of the distribution configuration.</p>"""
    distributions: NotRequired[
        "aws_sdk_imagebuilder.types.distribution_list.DistributionList"
    ]
    """<p>The distribution objects that apply Region-specific settings for the deployment of the image to targeted Regions.</p>"""
    timeout_minutes: "aws_sdk_imagebuilder.types.distribution_timeout_minutes.DistributionTimeoutMinutes"
    """<p>The maximum duration in minutes for this distribution configuration.</p>"""
    date_created: NotRequired["aws_sdk_imagebuilder.types.date_time.DateTime"]
    """<p>The date on which this distribution configuration was created.</p>"""
    date_updated: NotRequired["aws_sdk_imagebuilder.types.date_time.DateTime"]
    """<p>The date on which this distribution configuration was last updated.</p>"""
    tags: NotRequired["aws_sdk_imagebuilder.types.tag_map.TagMap"]
    """<p>The tags of the distribution configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DistributionConfiguration) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "distributions" in value:
        import aws_sdk_imagebuilder.types.distribution_list

        out["distributions"] = (
            aws_sdk_imagebuilder.types.distribution_list.serialize_json(
                value["distributions"]
            )
        )
    out["timeoutMinutes"] = value["timeout_minutes"]
    if "date_created" in value:
        out["dateCreated"] = value["date_created"]
    if "date_updated" in value:
        out["dateUpdated"] = value["date_updated"]
    if "tags" in value:
        import aws_sdk_imagebuilder.types.tag_map

        out["tags"] = aws_sdk_imagebuilder.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> DistributionConfiguration:
    out: DistributionConfiguration = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "distributions" in data:
        import aws_sdk_imagebuilder.types.distribution_list

        out["distributions"] = (
            aws_sdk_imagebuilder.types.distribution_list.deserialize_json(
                data["distributions"]
            )
        )
    if "timeoutMinutes" in data:
        out["timeout_minutes"] = data["timeoutMinutes"]
    else:
        raise DeserializationError("DistributionConfiguration.timeout_minutes required")
    if "dateCreated" in data:
        out["date_created"] = data["dateCreated"]
    if "dateUpdated" in data:
        out["date_updated"] = data["dateUpdated"]
    if "tags" in data:
        import aws_sdk_imagebuilder.types.tag_map

        out["tags"] = aws_sdk_imagebuilder.types.tag_map.deserialize_json(data["tags"])
    return out
