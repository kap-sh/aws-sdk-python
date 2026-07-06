"""Generated from Smithy shape ``com.amazonaws.imagebuilder#CreateContainerRecipeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_imagebuilder.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.client_token
    import aws_sdk_imagebuilder.types.component_configuration_list
    import aws_sdk_imagebuilder.types.container_type
    import aws_sdk_imagebuilder.types.inline_docker_file_template
    import aws_sdk_imagebuilder.types.instance_configuration
    import aws_sdk_imagebuilder.types.non_empty_string
    import aws_sdk_imagebuilder.types.platform
    import aws_sdk_imagebuilder.types.resource_name
    import aws_sdk_imagebuilder.types.tag_map
    import aws_sdk_imagebuilder.types.target_container_repository
    import aws_sdk_imagebuilder.types.uri
    import aws_sdk_imagebuilder.types.wildcard_version_number


class CreateContainerRecipeRequest(TypedDict, closed=True):
    container_type: "aws_sdk_imagebuilder.types.container_type.ContainerType"
    """<p>The type of container to create.</p>"""
    name: "aws_sdk_imagebuilder.types.resource_name.ResourceName"
    """<p>The name of the container recipe.</p>"""
    description: NotRequired[
        "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    """<p>The description of the container recipe.</p>"""
    semantic_version: (
        "aws_sdk_imagebuilder.types.wildcard_version_number.WildcardVersionNumber"
    )
    """<p>The semantic version of the container recipe. This version follows the semantic version syntax.</p> <note> <p>The semantic version has four nodes: <major>.<minor>.<patch>/<build>. You can assign values for the first three, and can filter on all of them.</p> <p> <b>Assignment:</b> For the first three nodes you can assign any positive integer value, including zero, with an upper limit of 2^30-1, or 1073741823 for each node. Image Builder automatically assigns the build number to the fourth node.</p> <p> <b>Patterns:</b> You can use any numeric pattern that adheres to the assignment requirements for the nodes that you can assign. For example, you might choose a software version pattern, such as 1.0.0, or a date, such as 2021.01.01.</p> </note>"""
    components: NotRequired[
        "aws_sdk_imagebuilder.types.component_configuration_list.ComponentConfigurationList"
    ]
    """<p>The components included in the container recipe.</p>"""
    instance_configuration: NotRequired[
        "aws_sdk_imagebuilder.types.instance_configuration.InstanceConfiguration"
    ]
    """<p>A group of options that can be used to configure an instance for building and testing container images.</p>"""
    dockerfile_template_data: NotRequired[
        "aws_sdk_imagebuilder.types.inline_docker_file_template.InlineDockerFileTemplate"
    ]
    """<p>The Dockerfile template used to build your image as an inline data blob.</p>"""
    dockerfile_template_uri: NotRequired["aws_sdk_imagebuilder.types.uri.Uri"]
    """<p>The Amazon S3 URI for the Dockerfile that will be used to build your container image.</p>"""
    platform_override: NotRequired["aws_sdk_imagebuilder.types.platform.Platform"]
    """<p>Specifies the operating system platform when you use a custom base image.</p>"""
    image_os_version_override: NotRequired[
        "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    """<p>Specifies the operating system version for the base image.</p>"""
    parent_image: "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
    """<p>The base image for the container recipe.</p>"""
    tags: NotRequired["aws_sdk_imagebuilder.types.tag_map.TagMap"]
    """<p>Tags that are attached to the container recipe.</p>"""
    working_directory: NotRequired[
        "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    """<p>The working directory for use during build and test workflows.</p>"""
    target_repository: "aws_sdk_imagebuilder.types.target_container_repository.TargetContainerRepository"
    """<p>The destination repository for the container image.</p>"""
    kms_key_id: NotRequired[
        "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    r"""<p>The Amazon Resource Name (ARN) that uniquely identifies which KMS key is used to encrypt the Dockerfile template. This can be either the Key ARN or the Alias ARN. For more information, see <a href=\"https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN\">Key identifiers (KeyId)</a> in the <i>Key Management Service Developer Guide</i>.</p>"""
    client_token: "aws_sdk_imagebuilder.types.client_token.ClientToken"
    r"""<p>Unique, case-sensitive identifier you provide to ensure idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a> in the <i>Amazon EC2 API Reference</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateContainerRecipeRequest) -> dict:
    out: dict = {}
    import aws_sdk_imagebuilder.types.container_type

    out["containerType"] = aws_sdk_imagebuilder.types.container_type.serialize_json(
        value["container_type"]
    )
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
    if "instance_configuration" in value:
        import aws_sdk_imagebuilder.types.instance_configuration

        out["instanceConfiguration"] = (
            aws_sdk_imagebuilder.types.instance_configuration.serialize_json(
                value["instance_configuration"]
            )
        )
    if "dockerfile_template_data" in value:
        out["dockerfileTemplateData"] = value["dockerfile_template_data"]
    if "dockerfile_template_uri" in value:
        out["dockerfileTemplateUri"] = value["dockerfile_template_uri"]
    if "platform_override" in value:
        import aws_sdk_imagebuilder.types.platform

        out["platformOverride"] = aws_sdk_imagebuilder.types.platform.serialize_json(
            value["platform_override"]
        )
    if "image_os_version_override" in value:
        out["imageOsVersionOverride"] = value["image_os_version_override"]
    out["parentImage"] = value["parent_image"]
    if "tags" in value:
        import aws_sdk_imagebuilder.types.tag_map

        out["tags"] = aws_sdk_imagebuilder.types.tag_map.serialize_json(value["tags"])
    if "working_directory" in value:
        out["workingDirectory"] = value["working_directory"]
    import aws_sdk_imagebuilder.types.target_container_repository

    out["targetRepository"] = (
        aws_sdk_imagebuilder.types.target_container_repository.serialize_json(
            value["target_repository"]
        )
    )
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateContainerRecipeRequest:
    out: CreateContainerRecipeRequest = {}  # type: ignore[typeddict-item]
    if "containerType" in data:
        import aws_sdk_imagebuilder.types.container_type

        out["container_type"] = (
            aws_sdk_imagebuilder.types.container_type.deserialize_json(
                data["containerType"]
            )
        )
    else:
        raise DeserializationError(
            "CreateContainerRecipeRequest.container_type required"
        )
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateContainerRecipeRequest.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "semanticVersion" in data:
        out["semantic_version"] = data["semanticVersion"]
    else:
        raise DeserializationError(
            "CreateContainerRecipeRequest.semantic_version required"
        )
    if "components" in data:
        import aws_sdk_imagebuilder.types.component_configuration_list

        out["components"] = (
            aws_sdk_imagebuilder.types.component_configuration_list.deserialize_json(
                data["components"]
            )
        )
    if "instanceConfiguration" in data:
        import aws_sdk_imagebuilder.types.instance_configuration

        out["instance_configuration"] = (
            aws_sdk_imagebuilder.types.instance_configuration.deserialize_json(
                data["instanceConfiguration"]
            )
        )
    if "dockerfileTemplateData" in data:
        out["dockerfile_template_data"] = data["dockerfileTemplateData"]
    if "dockerfileTemplateUri" in data:
        out["dockerfile_template_uri"] = data["dockerfileTemplateUri"]
    if "platformOverride" in data:
        import aws_sdk_imagebuilder.types.platform

        out["platform_override"] = aws_sdk_imagebuilder.types.platform.deserialize_json(
            data["platformOverride"]
        )
    if "imageOsVersionOverride" in data:
        out["image_os_version_override"] = data["imageOsVersionOverride"]
    if "parentImage" in data:
        out["parent_image"] = data["parentImage"]
    else:
        raise DeserializationError("CreateContainerRecipeRequest.parent_image required")
    if "tags" in data:
        import aws_sdk_imagebuilder.types.tag_map

        out["tags"] = aws_sdk_imagebuilder.types.tag_map.deserialize_json(data["tags"])
    if "workingDirectory" in data:
        out["working_directory"] = data["workingDirectory"]
    if "targetRepository" in data:
        import aws_sdk_imagebuilder.types.target_container_repository

        out["target_repository"] = (
            aws_sdk_imagebuilder.types.target_container_repository.deserialize_json(
                data["targetRepository"]
            )
        )
    else:
        raise DeserializationError(
            "CreateContainerRecipeRequest.target_repository required"
        )
    if "kmsKeyId" in data:
        out["kms_key_id"] = data["kmsKeyId"]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    else:
        raise DeserializationError("CreateContainerRecipeRequest.client_token required")
    return out
