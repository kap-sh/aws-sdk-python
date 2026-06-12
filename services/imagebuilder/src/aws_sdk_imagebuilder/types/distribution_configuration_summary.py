"""Generated from Smithy shape ``com.amazonaws.imagebuilder#DistributionConfigurationSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.date_time
    import aws_sdk_imagebuilder.types.image_builder_arn
    import aws_sdk_imagebuilder.types.non_empty_string
    import aws_sdk_imagebuilder.types.region_list
    import aws_sdk_imagebuilder.types.resource_name
    import aws_sdk_imagebuilder.types.tag_map


class DistributionConfigurationSummary(TypedDict):
    arn: NotRequired["aws_sdk_imagebuilder.types.image_builder_arn.ImageBuilderArn"]
    """<p>The Amazon Resource Name (ARN) of the distribution configuration.</p>"""
    name: NotRequired["aws_sdk_imagebuilder.types.resource_name.ResourceName"]
    """<p>The name of the distribution configuration.</p>"""
    description: NotRequired[
        "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    """<p>The description of the distribution configuration.</p>"""
    date_created: NotRequired["aws_sdk_imagebuilder.types.date_time.DateTime"]
    """<p>The date on which the distribution configuration was created.</p>"""
    date_updated: NotRequired["aws_sdk_imagebuilder.types.date_time.DateTime"]
    """<p>The date on which the distribution configuration was updated.</p>"""
    tags: NotRequired["aws_sdk_imagebuilder.types.tag_map.TagMap"]
    """<p>The tags associated with the distribution configuration.</p>"""
    regions: NotRequired["aws_sdk_imagebuilder.types.region_list.RegionList"]
    """<p>A list of Regions where the container image is distributed to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DistributionConfigurationSummary) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "date_created" in value:
        out["dateCreated"] = value["date_created"]
    if "date_updated" in value:
        out["dateUpdated"] = value["date_updated"]
    if "tags" in value:
        import aws_sdk_imagebuilder.types.tag_map

        out["tags"] = aws_sdk_imagebuilder.types.tag_map.serialize_json(value["tags"])
    if "regions" in value:
        import aws_sdk_imagebuilder.types.region_list

        out["regions"] = aws_sdk_imagebuilder.types.region_list.serialize_json(
            value["regions"]
        )
    return out


def deserialize_json(data: dict) -> DistributionConfigurationSummary:
    out: DistributionConfigurationSummary = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "dateCreated" in data:
        out["date_created"] = data["dateCreated"]
    if "dateUpdated" in data:
        out["date_updated"] = data["dateUpdated"]
    if "tags" in data:
        import aws_sdk_imagebuilder.types.tag_map

        out["tags"] = aws_sdk_imagebuilder.types.tag_map.deserialize_json(data["tags"])
    if "regions" in data:
        import aws_sdk_imagebuilder.types.region_list

        out["regions"] = aws_sdk_imagebuilder.types.region_list.deserialize_json(
            data["regions"]
        )
    return out
