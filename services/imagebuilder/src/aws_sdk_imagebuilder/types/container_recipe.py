"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ContainerRecipe``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.component_configuration_list
    import aws_sdk_imagebuilder.types.container_type
    import aws_sdk_imagebuilder.types.date_time
    import aws_sdk_imagebuilder.types.docker_file_template
    import aws_sdk_imagebuilder.types.image_builder_arn
    import aws_sdk_imagebuilder.types.instance_configuration
    import aws_sdk_imagebuilder.types.non_empty_string
    import aws_sdk_imagebuilder.types.nullable_boolean
    import aws_sdk_imagebuilder.types.platform
    import aws_sdk_imagebuilder.types.resource_name
    import aws_sdk_imagebuilder.types.tag_map
    import aws_sdk_imagebuilder.types.target_container_repository
    import aws_sdk_imagebuilder.types.version_number


class ContainerRecipe(TypedDict):
    arn: NotRequired["aws_sdk_imagebuilder.types.image_builder_arn.ImageBuilderArn"]
    """<p>The Amazon Resource Name (ARN) of the container recipe.</p> <note> <p>Semantic versioning is included in each object's Amazon Resource Name (ARN), at the level that applies to that object as follows:</p> <ol> <li> <p>Versionless ARNs and Name ARNs do not include specific values in any of the nodes. The nodes are either left off entirely, or they are specified as wildcards, for example: x.x.x.</p> </li> <li> <p>Version ARNs have only the first three nodes: <major>.<minor>.<patch></p> </li> <li> <p>Build version ARNs have all four nodes, and point to a specific build for a specific version of an object.</p> </li> </ol> </note>"""
    container_type: NotRequired[
        "aws_sdk_imagebuilder.types.container_type.ContainerType"
    ]
    """<p>Specifies the type of container, such as Docker.</p>"""
    name: NotRequired["aws_sdk_imagebuilder.types.resource_name.ResourceName"]
    """<p>The name of the container recipe.</p>"""
    description: NotRequired[
        "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    """<p>The description of the container recipe.</p>"""
    platform: NotRequired["aws_sdk_imagebuilder.types.platform.Platform"]
    """<p>The system platform for the container, such as Windows or Linux.</p>"""
    owner: NotRequired["aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The owner of the container recipe.</p>"""
    version: NotRequired["aws_sdk_imagebuilder.types.version_number.VersionNumber"]
    """<p>The semantic version of the container recipe.</p> <note> <p>The semantic version has four nodes: <major>.<minor>.<patch>/<build>. You can assign values for the first three, and can filter on all of them.</p> <p> <b>Assignment:</b> For the first three nodes you can assign any positive integer value, including zero, with an upper limit of 2^30-1, or 1073741823 for each node. Image Builder automatically assigns the build number to the fourth node.</p> <p> <b>Patterns:</b> You can use any numeric pattern that adheres to the assignment requirements for the nodes that you can assign. For example, you might choose a software version pattern, such as 1.0.0, or a date, such as 2021.01.01.</p> <p> <b>Filtering:</b> With semantic versioning, you have the flexibility to use wildcards (x) to specify the most recent versions or nodes when selecting the base image or components for your recipe. When you use a wildcard in any node, all nodes to the right of the first wildcard must also be wildcards.</p> </note>"""
    components: NotRequired[
        "aws_sdk_imagebuilder.types.component_configuration_list.ComponentConfigurationList"
    ]
    """<p>Build and test components that are included in the container recipe. Recipes require a minimum of one build component, and can have a maximum of 20 build and test components in any combination.</p>"""
    instance_configuration: NotRequired[
        "aws_sdk_imagebuilder.types.instance_configuration.InstanceConfiguration"
    ]
    """<p>A group of options that can be used to configure an instance for building and testing container images.</p>"""
    dockerfile_template_data: NotRequired[
        "aws_sdk_imagebuilder.types.docker_file_template.DockerFileTemplate"
    ]
    """<p>Dockerfiles are text documents that are used to build Docker containers, and ensure that they contain all of the elements required by the application running inside. The template data consists of contextual variables where Image Builder places build information or scripts, based on your container image recipe.</p>"""
    kms_key_id: NotRequired[
        "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    r"""<p>The Amazon Resource Name (ARN) that uniquely identifies which KMS key is used to encrypt the container image for distribution to the target Region. This can be either the Key ARN or the Alias ARN. For more information, see <a href=\"https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN\">Key identifiers (KeyId)</a> in the <i>Key Management Service Developer Guide</i>.</p>"""
    encrypted: NotRequired[
        "aws_sdk_imagebuilder.types.nullable_boolean.NullableBoolean"
    ]
    """<p>A flag that indicates if the target container is encrypted.</p>"""
    parent_image: NotRequired[
        "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    """<p>The base image for customizations specified in the container recipe. This can contain an Image Builder image resource ARN or a container image URI, for example <code>amazonlinux:latest</code>.</p>"""
    date_created: NotRequired["aws_sdk_imagebuilder.types.date_time.DateTime"]
    """<p>The date when this container recipe was created.</p>"""
    tags: NotRequired["aws_sdk_imagebuilder.types.tag_map.TagMap"]
    """<p>Tags that are attached to the container recipe.</p>"""
    working_directory: NotRequired[
        "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    """<p>The working directory for use during build and test workflows.</p>"""
    target_repository: NotRequired[
        "aws_sdk_imagebuilder.types.target_container_repository.TargetContainerRepository"
    ]
    """<p>The destination repository for the container image.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContainerRecipe) -> dict:
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
    if "description" in value:
        out["description"] = value["description"]
    if "platform" in value:
        import aws_sdk_imagebuilder.types.platform

        out["platform"] = aws_sdk_imagebuilder.types.platform.serialize_json(
            value["platform"]
        )
    if "owner" in value:
        out["owner"] = value["owner"]
    if "version" in value:
        out["version"] = value["version"]
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
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    if "encrypted" in value:
        out["encrypted"] = value["encrypted"]
    if "parent_image" in value:
        out["parentImage"] = value["parent_image"]
    if "date_created" in value:
        out["dateCreated"] = value["date_created"]
    if "tags" in value:
        import aws_sdk_imagebuilder.types.tag_map

        out["tags"] = aws_sdk_imagebuilder.types.tag_map.serialize_json(value["tags"])
    if "working_directory" in value:
        out["workingDirectory"] = value["working_directory"]
    if "target_repository" in value:
        import aws_sdk_imagebuilder.types.target_container_repository

        out["targetRepository"] = (
            aws_sdk_imagebuilder.types.target_container_repository.serialize_json(
                value["target_repository"]
            )
        )
    return out


def deserialize_json(data: dict) -> ContainerRecipe:
    out: ContainerRecipe = {}  # type: ignore[typeddict-item]
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
    if "description" in data:
        out["description"] = data["description"]
    if "platform" in data:
        import aws_sdk_imagebuilder.types.platform

        out["platform"] = aws_sdk_imagebuilder.types.platform.deserialize_json(
            data["platform"]
        )
    if "owner" in data:
        out["owner"] = data["owner"]
    if "version" in data:
        out["version"] = data["version"]
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
    if "kmsKeyId" in data:
        out["kms_key_id"] = data["kmsKeyId"]
    if "encrypted" in data:
        out["encrypted"] = data["encrypted"]
    if "parentImage" in data:
        out["parent_image"] = data["parentImage"]
    if "dateCreated" in data:
        out["date_created"] = data["dateCreated"]
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
    return out
