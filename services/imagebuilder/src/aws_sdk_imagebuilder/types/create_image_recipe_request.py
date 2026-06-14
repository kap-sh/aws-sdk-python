"""Generated from Smithy shape ``com.amazonaws.imagebuilder#CreateImageRecipeRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_imagebuilder.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.additional_instance_configuration
    import aws_sdk_imagebuilder.types.client_token
    import aws_sdk_imagebuilder.types.component_configuration_list
    import aws_sdk_imagebuilder.types.instance_block_device_mappings
    import aws_sdk_imagebuilder.types.non_empty_string
    import aws_sdk_imagebuilder.types.resource_name
    import aws_sdk_imagebuilder.types.tag_map
    import aws_sdk_imagebuilder.types.wildcard_version_number


class CreateImageRecipeRequest(TypedDict):
    name: "aws_sdk_imagebuilder.types.resource_name.ResourceName"
    """<p>The name of the image recipe.</p>"""
    description: NotRequired[
        "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    """<p>The description of the image recipe.</p>"""
    semantic_version: (
        "aws_sdk_imagebuilder.types.wildcard_version_number.WildcardVersionNumber"
    )
    """<p>The semantic version of the image recipe. This version follows the semantic version syntax.</p> <note> <p>The semantic version has four nodes: <major>.<minor>.<patch>/<build>. You can assign values for the first three, and can filter on all of them.</p> <p> <b>Assignment:</b> For the first three nodes you can assign any positive integer value, including zero, with an upper limit of 2^30-1, or 1073741823 for each node. Image Builder automatically assigns the build number to the fourth node.</p> <p> <b>Patterns:</b> You can use any numeric pattern that adheres to the assignment requirements for the nodes that you can assign. For example, you might choose a software version pattern, such as 1.0.0, or a date, such as 2021.01.01.</p> </note>"""
    components: NotRequired[
        "aws_sdk_imagebuilder.types.component_configuration_list.ComponentConfigurationList"
    ]
    """<p>The components included in the image recipe.</p>"""
    parent_image: "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
    """<p>The base image for customizations specified in the image recipe. You can specify the parent image using one of the following options:</p> <ul> <li> <p>AMI ID</p> </li> <li> <p>Image Builder image Amazon Resource Name (ARN)</p> </li> <li> <p>Amazon Web Services Systems Manager (SSM) Parameter Store Parameter, prefixed by <code>ssm:</code>, followed by the parameter name or ARN.</p> </li> <li> <p>Amazon Web Services Marketplace product ID</p> </li> </ul> <p>If you enter an AMI ID or an SSM parameter that contains the AMI ID, you must have access to the AMI, and the AMI must be in the source Region.</p>"""
    block_device_mappings: NotRequired[
        "aws_sdk_imagebuilder.types.instance_block_device_mappings.InstanceBlockDeviceMappings"
    ]
    """<p>The block device mappings of the image recipe.</p>"""
    tags: NotRequired["aws_sdk_imagebuilder.types.tag_map.TagMap"]
    """<p>The tags of the image recipe.</p>"""
    working_directory: NotRequired[
        "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    """<p>The working directory used during build and test workflows.</p>"""
    additional_instance_configuration: NotRequired[
        "aws_sdk_imagebuilder.types.additional_instance_configuration.AdditionalInstanceConfiguration"
    ]
    """<p>Specify additional settings and launch scripts for your build instances.</p>"""
    ami_tags: NotRequired["aws_sdk_imagebuilder.types.tag_map.TagMap"]
    """<p>Tags that are applied to the AMI that Image Builder creates during the Build phase prior to image distribution.</p>"""
    client_token: "aws_sdk_imagebuilder.types.client_token.ClientToken"
    r"""<p>Unique, case-sensitive identifier you provide to ensure idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a> in the <i>Amazon EC2 API Reference</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateImageRecipeRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    out["semanticVersion"] = value["semantic_version"]
    if "components" in value:
        import aws_sdk_imagebuilder.types.component_configuration_list

        out["components"] = (
            aws_sdk_imagebuilder.types.component_configuration_list.serialize_json(
                value["components"]
            )
        )
    out["parentImage"] = value["parent_image"]
    if "block_device_mappings" in value:
        import aws_sdk_imagebuilder.types.instance_block_device_mappings

        out["blockDeviceMappings"] = (
            aws_sdk_imagebuilder.types.instance_block_device_mappings.serialize_json(
                value["block_device_mappings"]
            )
        )
    if "tags" in value:
        import aws_sdk_imagebuilder.types.tag_map

        out["tags"] = aws_sdk_imagebuilder.types.tag_map.serialize_json(value["tags"])
    if "working_directory" in value:
        out["workingDirectory"] = value["working_directory"]
    if "additional_instance_configuration" in value:
        import aws_sdk_imagebuilder.types.additional_instance_configuration

        out["additionalInstanceConfiguration"] = (
            aws_sdk_imagebuilder.types.additional_instance_configuration.serialize_json(
                value["additional_instance_configuration"]
            )
        )
    if "ami_tags" in value:
        import aws_sdk_imagebuilder.types.tag_map

        out["amiTags"] = aws_sdk_imagebuilder.types.tag_map.serialize_json(
            value["ami_tags"]
        )
    out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateImageRecipeRequest:
    out: CreateImageRecipeRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateImageRecipeRequest.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "semanticVersion" in data:
        out["semantic_version"] = data["semanticVersion"]
    else:
        raise DeserializationError("CreateImageRecipeRequest.semantic_version required")
    if "components" in data:
        import aws_sdk_imagebuilder.types.component_configuration_list

        out["components"] = (
            aws_sdk_imagebuilder.types.component_configuration_list.deserialize_json(
                data["components"]
            )
        )
    if "parentImage" in data:
        out["parent_image"] = data["parentImage"]
    else:
        raise DeserializationError("CreateImageRecipeRequest.parent_image required")
    if "blockDeviceMappings" in data:
        import aws_sdk_imagebuilder.types.instance_block_device_mappings

        out["block_device_mappings"] = (
            aws_sdk_imagebuilder.types.instance_block_device_mappings.deserialize_json(
                data["blockDeviceMappings"]
            )
        )
    if "tags" in data:
        import aws_sdk_imagebuilder.types.tag_map

        out["tags"] = aws_sdk_imagebuilder.types.tag_map.deserialize_json(data["tags"])
    if "workingDirectory" in data:
        out["working_directory"] = data["workingDirectory"]
    if "additionalInstanceConfiguration" in data:
        import aws_sdk_imagebuilder.types.additional_instance_configuration

        out["additional_instance_configuration"] = (
            aws_sdk_imagebuilder.types.additional_instance_configuration.deserialize_json(
                data["additionalInstanceConfiguration"]
            )
        )
    if "amiTags" in data:
        import aws_sdk_imagebuilder.types.tag_map

        out["ami_tags"] = aws_sdk_imagebuilder.types.tag_map.deserialize_json(
            data["amiTags"]
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    else:
        raise DeserializationError("CreateImageRecipeRequest.client_token required")
    return out
