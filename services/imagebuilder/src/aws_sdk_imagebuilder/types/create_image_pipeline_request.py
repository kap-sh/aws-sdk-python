"""Generated from Smithy shape ``com.amazonaws.imagebuilder#CreateImagePipelineRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_imagebuilder.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.client_token
    import aws_sdk_imagebuilder.types.container_recipe_arn
    import aws_sdk_imagebuilder.types.distribution_configuration_arn
    import aws_sdk_imagebuilder.types.image_recipe_arn
    import aws_sdk_imagebuilder.types.image_scanning_configuration
    import aws_sdk_imagebuilder.types.image_tests_configuration
    import aws_sdk_imagebuilder.types.infrastructure_configuration_arn
    import aws_sdk_imagebuilder.types.non_empty_string
    import aws_sdk_imagebuilder.types.nullable_boolean
    import aws_sdk_imagebuilder.types.pipeline_logging_configuration
    import aws_sdk_imagebuilder.types.pipeline_status
    import aws_sdk_imagebuilder.types.resource_name
    import aws_sdk_imagebuilder.types.role_name_or_arn
    import aws_sdk_imagebuilder.types.schedule
    import aws_sdk_imagebuilder.types.tag_map
    import aws_sdk_imagebuilder.types.workflow_configuration_list


class CreateImagePipelineRequest(TypedDict):
    name: "aws_sdk_imagebuilder.types.resource_name.ResourceName"
    """<p>The name of the image pipeline.</p>"""
    description: NotRequired[
        "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    """<p>The description of the image pipeline.</p>"""
    image_recipe_arn: NotRequired[
        "aws_sdk_imagebuilder.types.image_recipe_arn.ImageRecipeArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the image recipe that will be used to configure images created by this image pipeline.</p>"""
    container_recipe_arn: NotRequired[
        "aws_sdk_imagebuilder.types.container_recipe_arn.ContainerRecipeArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the container recipe that is used to configure images created by this container pipeline.</p>"""
    infrastructure_configuration_arn: "aws_sdk_imagebuilder.types.infrastructure_configuration_arn.InfrastructureConfigurationArn"
    """<p>The Amazon Resource Name (ARN) of the infrastructure configuration that will be used to build images created by this image pipeline.</p>"""
    distribution_configuration_arn: NotRequired[
        "aws_sdk_imagebuilder.types.distribution_configuration_arn.DistributionConfigurationArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the distribution configuration that will be used to configure and distribute images created by this image pipeline.</p>"""
    image_tests_configuration: NotRequired[
        "aws_sdk_imagebuilder.types.image_tests_configuration.ImageTestsConfiguration"
    ]
    """<p>The image test configuration of the image pipeline.</p>"""
    enhanced_image_metadata_enabled: NotRequired[
        "aws_sdk_imagebuilder.types.nullable_boolean.NullableBoolean"
    ]
    """<p>Collects additional information about the image being created, including the operating system (OS) version and package list. This information is used to enhance the overall experience of using EC2 Image Builder. Enabled by default.</p>"""
    schedule: NotRequired["aws_sdk_imagebuilder.types.schedule.Schedule"]
    """<p>The schedule of the image pipeline.</p>"""
    status: NotRequired["aws_sdk_imagebuilder.types.pipeline_status.PipelineStatus"]
    """<p>The status of the image pipeline.</p>"""
    tags: NotRequired["aws_sdk_imagebuilder.types.tag_map.TagMap"]
    """<p>The tags of the image pipeline.</p>"""
    image_tags: NotRequired["aws_sdk_imagebuilder.types.tag_map.TagMap"]
    """<p>The tags to be applied to the images produced by this pipeline.</p>"""
    client_token: "aws_sdk_imagebuilder.types.client_token.ClientToken"
    """<p>Unique, case-sensitive identifier you provide to ensure idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a> in the <i>Amazon EC2 API Reference</i>.</p>"""
    image_scanning_configuration: NotRequired[
        "aws_sdk_imagebuilder.types.image_scanning_configuration.ImageScanningConfiguration"
    ]
    """<p>Contains settings for vulnerability scans.</p>"""
    workflows: NotRequired[
        "aws_sdk_imagebuilder.types.workflow_configuration_list.WorkflowConfigurationList"
    ]
    """<p>Contains an array of workflow configuration objects.</p>"""
    execution_role: NotRequired[
        "aws_sdk_imagebuilder.types.role_name_or_arn.RoleNameOrArn"
    ]
    """<p>The name or Amazon Resource Name (ARN) for the IAM role you create that grants Image Builder access to perform workflow actions.</p>"""
    logging_configuration: NotRequired[
        "aws_sdk_imagebuilder.types.pipeline_logging_configuration.PipelineLoggingConfiguration"
    ]
    """<p>Define logging configuration for the image build process.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateImagePipelineRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "image_recipe_arn" in value:
        out["imageRecipeArn"] = value["image_recipe_arn"]
    if "container_recipe_arn" in value:
        out["containerRecipeArn"] = value["container_recipe_arn"]
    out["infrastructureConfigurationArn"] = value["infrastructure_configuration_arn"]
    if "distribution_configuration_arn" in value:
        out["distributionConfigurationArn"] = value["distribution_configuration_arn"]
    if "image_tests_configuration" in value:
        import aws_sdk_imagebuilder.types.image_tests_configuration

        out["imageTestsConfiguration"] = (
            aws_sdk_imagebuilder.types.image_tests_configuration.serialize_json(
                value["image_tests_configuration"]
            )
        )
    if "enhanced_image_metadata_enabled" in value:
        out["enhancedImageMetadataEnabled"] = value["enhanced_image_metadata_enabled"]
    if "schedule" in value:
        import aws_sdk_imagebuilder.types.schedule

        out["schedule"] = aws_sdk_imagebuilder.types.schedule.serialize_json(
            value["schedule"]
        )
    if "status" in value:
        import aws_sdk_imagebuilder.types.pipeline_status

        out["status"] = aws_sdk_imagebuilder.types.pipeline_status.serialize_json(
            value["status"]
        )
    if "tags" in value:
        import aws_sdk_imagebuilder.types.tag_map

        out["tags"] = aws_sdk_imagebuilder.types.tag_map.serialize_json(value["tags"])
    if "image_tags" in value:
        import aws_sdk_imagebuilder.types.tag_map

        out["imageTags"] = aws_sdk_imagebuilder.types.tag_map.serialize_json(
            value["image_tags"]
        )
    out["clientToken"] = value["client_token"]
    if "image_scanning_configuration" in value:
        import aws_sdk_imagebuilder.types.image_scanning_configuration

        out["imageScanningConfiguration"] = (
            aws_sdk_imagebuilder.types.image_scanning_configuration.serialize_json(
                value["image_scanning_configuration"]
            )
        )
    if "workflows" in value:
        import aws_sdk_imagebuilder.types.workflow_configuration_list

        out["workflows"] = (
            aws_sdk_imagebuilder.types.workflow_configuration_list.serialize_json(
                value["workflows"]
            )
        )
    if "execution_role" in value:
        out["executionRole"] = value["execution_role"]
    if "logging_configuration" in value:
        import aws_sdk_imagebuilder.types.pipeline_logging_configuration

        out["loggingConfiguration"] = (
            aws_sdk_imagebuilder.types.pipeline_logging_configuration.serialize_json(
                value["logging_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateImagePipelineRequest:
    out: CreateImagePipelineRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateImagePipelineRequest.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "imageRecipeArn" in data:
        out["image_recipe_arn"] = data["imageRecipeArn"]
    if "containerRecipeArn" in data:
        out["container_recipe_arn"] = data["containerRecipeArn"]
    if "infrastructureConfigurationArn" in data:
        out["infrastructure_configuration_arn"] = data["infrastructureConfigurationArn"]
    else:
        raise DeserializationError(
            "CreateImagePipelineRequest.infrastructure_configuration_arn required"
        )
    if "distributionConfigurationArn" in data:
        out["distribution_configuration_arn"] = data["distributionConfigurationArn"]
    if "imageTestsConfiguration" in data:
        import aws_sdk_imagebuilder.types.image_tests_configuration

        out["image_tests_configuration"] = (
            aws_sdk_imagebuilder.types.image_tests_configuration.deserialize_json(
                data["imageTestsConfiguration"]
            )
        )
    if "enhancedImageMetadataEnabled" in data:
        out["enhanced_image_metadata_enabled"] = data["enhancedImageMetadataEnabled"]
    if "schedule" in data:
        import aws_sdk_imagebuilder.types.schedule

        out["schedule"] = aws_sdk_imagebuilder.types.schedule.deserialize_json(
            data["schedule"]
        )
    if "status" in data:
        import aws_sdk_imagebuilder.types.pipeline_status

        out["status"] = aws_sdk_imagebuilder.types.pipeline_status.deserialize_json(
            data["status"]
        )
    if "tags" in data:
        import aws_sdk_imagebuilder.types.tag_map

        out["tags"] = aws_sdk_imagebuilder.types.tag_map.deserialize_json(data["tags"])
    if "imageTags" in data:
        import aws_sdk_imagebuilder.types.tag_map

        out["image_tags"] = aws_sdk_imagebuilder.types.tag_map.deserialize_json(
            data["imageTags"]
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    else:
        raise DeserializationError("CreateImagePipelineRequest.client_token required")
    if "imageScanningConfiguration" in data:
        import aws_sdk_imagebuilder.types.image_scanning_configuration

        out["image_scanning_configuration"] = (
            aws_sdk_imagebuilder.types.image_scanning_configuration.deserialize_json(
                data["imageScanningConfiguration"]
            )
        )
    if "workflows" in data:
        import aws_sdk_imagebuilder.types.workflow_configuration_list

        out["workflows"] = (
            aws_sdk_imagebuilder.types.workflow_configuration_list.deserialize_json(
                data["workflows"]
            )
        )
    if "executionRole" in data:
        out["execution_role"] = data["executionRole"]
    if "loggingConfiguration" in data:
        import aws_sdk_imagebuilder.types.pipeline_logging_configuration

        out["logging_configuration"] = (
            aws_sdk_imagebuilder.types.pipeline_logging_configuration.deserialize_json(
                data["loggingConfiguration"]
            )
        )
    return out
