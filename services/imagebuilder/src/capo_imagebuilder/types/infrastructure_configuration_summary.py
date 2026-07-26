"""Generated from Smithy shape ``com.amazonaws.imagebuilder#InfrastructureConfigurationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.date_time
    import capo_imagebuilder.types.image_builder_arn
    import capo_imagebuilder.types.instance_profile_name_type
    import capo_imagebuilder.types.instance_type_list
    import capo_imagebuilder.types.non_empty_string
    import capo_imagebuilder.types.placement
    import capo_imagebuilder.types.resource_name
    import capo_imagebuilder.types.resource_tag_map
    import capo_imagebuilder.types.tag_map


class InfrastructureConfigurationSummary(TypedDict, closed=True):
    arn: NotRequired["capo_imagebuilder.types.image_builder_arn.ImageBuilderArn"]
    """<p>The Amazon Resource Name (ARN) of the infrastructure configuration.</p>"""
    name: NotRequired["capo_imagebuilder.types.resource_name.ResourceName"]
    """<p>The name of the infrastructure configuration.</p>"""
    description: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The description of the infrastructure configuration.</p>"""
    date_created: NotRequired["capo_imagebuilder.types.date_time.DateTime"]
    """<p>The date on which the infrastructure configuration was created.</p>"""
    date_updated: NotRequired["capo_imagebuilder.types.date_time.DateTime"]
    """<p>The date on which the infrastructure configuration was last updated.</p>"""
    resource_tags: NotRequired[
        "capo_imagebuilder.types.resource_tag_map.ResourceTagMap"
    ]
    """<p>The tags attached to the image created by Image Builder.</p>"""
    tags: NotRequired["capo_imagebuilder.types.tag_map.TagMap"]
    """<p>The tags of the infrastructure configuration.</p>"""
    instance_types: NotRequired[
        "capo_imagebuilder.types.instance_type_list.InstanceTypeList"
    ]
    """<p>The instance types of the infrastructure configuration.</p>"""
    instance_profile_name: NotRequired[
        "capo_imagebuilder.types.instance_profile_name_type.InstanceProfileNameType"
    ]
    """<p>The instance profile of the infrastructure configuration.</p>"""
    placement: NotRequired["capo_imagebuilder.types.placement.Placement"]
    """<p>The instance placement settings that define where the instances that are launched from your image will run.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InfrastructureConfigurationSummary) -> dict:
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
    if "resource_tags" in value:
        import capo_imagebuilder.types.resource_tag_map

        out["resourceTags"] = capo_imagebuilder.types.resource_tag_map.serialize_json(
            value["resource_tags"]
        )
    if "tags" in value:
        import capo_imagebuilder.types.tag_map

        out["tags"] = capo_imagebuilder.types.tag_map.serialize_json(value["tags"])
    if "instance_types" in value:
        import capo_imagebuilder.types.instance_type_list

        out["instanceTypes"] = (
            capo_imagebuilder.types.instance_type_list.serialize_json(
                value["instance_types"]
            )
        )
    if "instance_profile_name" in value:
        out["instanceProfileName"] = value["instance_profile_name"]
    if "placement" in value:
        import capo_imagebuilder.types.placement

        out["placement"] = capo_imagebuilder.types.placement.serialize_json(
            value["placement"]
        )
    return out


def deserialize_json(data: dict) -> InfrastructureConfigurationSummary:
    out: InfrastructureConfigurationSummary = {}  # type: ignore[typeddict-item]
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
    if "resourceTags" in data:
        import capo_imagebuilder.types.resource_tag_map

        out["resource_tags"] = (
            capo_imagebuilder.types.resource_tag_map.deserialize_json(
                data["resourceTags"]
            )
        )
    if "tags" in data:
        import capo_imagebuilder.types.tag_map

        out["tags"] = capo_imagebuilder.types.tag_map.deserialize_json(data["tags"])
    if "instanceTypes" in data:
        import capo_imagebuilder.types.instance_type_list

        out["instance_types"] = (
            capo_imagebuilder.types.instance_type_list.deserialize_json(
                data["instanceTypes"]
            )
        )
    if "instanceProfileName" in data:
        out["instance_profile_name"] = data["instanceProfileName"]
    if "placement" in data:
        import capo_imagebuilder.types.placement

        out["placement"] = capo_imagebuilder.types.placement.deserialize_json(
            data["placement"]
        )
    return out
