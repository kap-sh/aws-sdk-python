"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ImageRecipe``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.additional_instance_configuration
    import capo_imagebuilder.types.component_configuration_list
    import capo_imagebuilder.types.date_time
    import capo_imagebuilder.types.image_builder_arn
    import capo_imagebuilder.types.image_type
    import capo_imagebuilder.types.instance_block_device_mappings
    import capo_imagebuilder.types.non_empty_string
    import capo_imagebuilder.types.platform
    import capo_imagebuilder.types.resource_name
    import capo_imagebuilder.types.tag_map
    import capo_imagebuilder.types.version_number


class ImageRecipe(TypedDict, closed=True):
    arn: NotRequired["capo_imagebuilder.types.image_builder_arn.ImageBuilderArn"]
    """<p>The Amazon Resource Name (ARN) of the image recipe.</p>"""
    type: NotRequired["capo_imagebuilder.types.image_type.ImageType"]
    """<p>Specifies which type of image is created by the recipe - an AMI or a container image.</p>"""
    name: NotRequired["capo_imagebuilder.types.resource_name.ResourceName"]
    """<p>The name of the image recipe.</p>"""
    description: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The description of the image recipe.</p>"""
    platform: NotRequired["capo_imagebuilder.types.platform.Platform"]
    """<p>The platform of the image recipe.</p>"""
    owner: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The owner of the image recipe.</p>"""
    version: NotRequired["capo_imagebuilder.types.version_number.VersionNumber"]
    """<p>The version of the image recipe.</p>"""
    components: NotRequired[
        "capo_imagebuilder.types.component_configuration_list.ComponentConfigurationList"
    ]
    """<p>The components that are included in the image recipe. Recipes require a minimum of one build component, and can have a maximum of 20 build and test components in any combination.</p>"""
    parent_image: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The base image for customizations specified in the image recipe. You can specify the parent image using one of the following options:</p> <ul> <li> <p>AMI ID</p> </li> <li> <p>Image Builder image Amazon Resource Name (ARN)</p> </li> <li> <p>Amazon Web Services Systems Manager (SSM) Parameter Store Parameter, prefixed by <code>ssm:</code>, followed by the parameter name or ARN.</p> </li> <li> <p>Amazon Web Services Marketplace product ID</p> </li> </ul>"""
    block_device_mappings: NotRequired[
        "capo_imagebuilder.types.instance_block_device_mappings.InstanceBlockDeviceMappings"
    ]
    """<p>The block device mappings to apply when creating images from this recipe.</p>"""
    date_created: NotRequired["capo_imagebuilder.types.date_time.DateTime"]
    """<p>The date on which this image recipe was created.</p>"""
    tags: NotRequired["capo_imagebuilder.types.tag_map.TagMap"]
    """<p>The tags of the image recipe.</p>"""
    working_directory: NotRequired[
        "capo_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    """<p>The working directory to be used during build and test workflows.</p>"""
    additional_instance_configuration: NotRequired[
        "capo_imagebuilder.types.additional_instance_configuration.AdditionalInstanceConfiguration"
    ]
    """<p>Before you create a new AMI, Image Builder launches temporary Amazon EC2 instances to build and test your image configuration. Instance configuration adds a layer of control over those instances. You can define settings and add scripts to run when an instance is launched from your AMI.</p>"""
    ami_tags: NotRequired["capo_imagebuilder.types.tag_map.TagMap"]
    """<p>Tags that are applied to the AMI that Image Builder creates during the Build phase prior to image distribution.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImageRecipe) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "type" in value:
        import capo_imagebuilder.types.image_type

        out["type"] = capo_imagebuilder.types.image_type.serialize_json(value["type"])
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "platform" in value:
        import capo_imagebuilder.types.platform

        out["platform"] = capo_imagebuilder.types.platform.serialize_json(
            value["platform"]
        )
    if "owner" in value:
        out["owner"] = value["owner"]
    if "version" in value:
        out["version"] = value["version"]
    if "components" in value:
        import capo_imagebuilder.types.component_configuration_list

        out["components"] = (
            capo_imagebuilder.types.component_configuration_list.serialize_json(
                value["components"]
            )
        )
    if "parent_image" in value:
        out["parentImage"] = value["parent_image"]
    if "block_device_mappings" in value:
        import capo_imagebuilder.types.instance_block_device_mappings

        out["blockDeviceMappings"] = (
            capo_imagebuilder.types.instance_block_device_mappings.serialize_json(
                value["block_device_mappings"]
            )
        )
    if "date_created" in value:
        out["dateCreated"] = value["date_created"]
    if "tags" in value:
        import capo_imagebuilder.types.tag_map

        out["tags"] = capo_imagebuilder.types.tag_map.serialize_json(value["tags"])
    if "working_directory" in value:
        out["workingDirectory"] = value["working_directory"]
    if "additional_instance_configuration" in value:
        import capo_imagebuilder.types.additional_instance_configuration

        out["additionalInstanceConfiguration"] = (
            capo_imagebuilder.types.additional_instance_configuration.serialize_json(
                value["additional_instance_configuration"]
            )
        )
    if "ami_tags" in value:
        import capo_imagebuilder.types.tag_map

        out["amiTags"] = capo_imagebuilder.types.tag_map.serialize_json(
            value["ami_tags"]
        )
    return out


def deserialize_json(data: dict) -> ImageRecipe:
    out: ImageRecipe = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "type" in data:
        import capo_imagebuilder.types.image_type

        out["type"] = capo_imagebuilder.types.image_type.deserialize_json(data["type"])
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "platform" in data:
        import capo_imagebuilder.types.platform

        out["platform"] = capo_imagebuilder.types.platform.deserialize_json(
            data["platform"]
        )
    if "owner" in data:
        out["owner"] = data["owner"]
    if "version" in data:
        out["version"] = data["version"]
    if "components" in data:
        import capo_imagebuilder.types.component_configuration_list

        out["components"] = (
            capo_imagebuilder.types.component_configuration_list.deserialize_json(
                data["components"]
            )
        )
    if "parentImage" in data:
        out["parent_image"] = data["parentImage"]
    if "blockDeviceMappings" in data:
        import capo_imagebuilder.types.instance_block_device_mappings

        out["block_device_mappings"] = (
            capo_imagebuilder.types.instance_block_device_mappings.deserialize_json(
                data["blockDeviceMappings"]
            )
        )
    if "dateCreated" in data:
        out["date_created"] = data["dateCreated"]
    if "tags" in data:
        import capo_imagebuilder.types.tag_map

        out["tags"] = capo_imagebuilder.types.tag_map.deserialize_json(data["tags"])
    if "workingDirectory" in data:
        out["working_directory"] = data["workingDirectory"]
    if "additionalInstanceConfiguration" in data:
        import capo_imagebuilder.types.additional_instance_configuration

        out["additional_instance_configuration"] = (
            capo_imagebuilder.types.additional_instance_configuration.deserialize_json(
                data["additionalInstanceConfiguration"]
            )
        )
    if "amiTags" in data:
        import capo_imagebuilder.types.tag_map

        out["ami_tags"] = capo_imagebuilder.types.tag_map.deserialize_json(
            data["amiTags"]
        )
    return out
