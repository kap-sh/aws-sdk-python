"""Generated from Smithy shape ``com.amazonaws.imagebuilder#CreateImageRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_imagebuilder.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.client_token
    import aws_sdk_imagebuilder.types.container_recipe_arn
    import aws_sdk_imagebuilder.types.distribution_configuration_arn
    import aws_sdk_imagebuilder.types.image_logging_configuration
    import aws_sdk_imagebuilder.types.image_recipe_arn
    import aws_sdk_imagebuilder.types.image_scanning_configuration
    import aws_sdk_imagebuilder.types.image_tests_configuration
    import aws_sdk_imagebuilder.types.infrastructure_configuration_arn
    import aws_sdk_imagebuilder.types.nullable_boolean
    import aws_sdk_imagebuilder.types.role_name_or_arn
    import aws_sdk_imagebuilder.types.tag_map
    import aws_sdk_imagebuilder.types.workflow_configuration_list


class CreateImageRequest(TypedDict):
    image_recipe_arn: NotRequired[
        "aws_sdk_imagebuilder.types.image_recipe_arn.ImageRecipeArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the image recipe that defines how images are configured, tested, and assessed.</p>"""
    container_recipe_arn: NotRequired[
        "aws_sdk_imagebuilder.types.container_recipe_arn.ContainerRecipeArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the container recipe that defines how images are configured and tested.</p>"""
    distribution_configuration_arn: NotRequired[
        "aws_sdk_imagebuilder.types.distribution_configuration_arn.DistributionConfigurationArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the distribution configuration that defines and configures the outputs of your pipeline.</p>"""
    infrastructure_configuration_arn: "aws_sdk_imagebuilder.types.infrastructure_configuration_arn.InfrastructureConfigurationArn"
    """<p>The Amazon Resource Name (ARN) of the infrastructure configuration that defines the environment in which your image will be built and tested.</p>"""
    image_tests_configuration: NotRequired[
        "aws_sdk_imagebuilder.types.image_tests_configuration.ImageTestsConfiguration"
    ]
    """<p>The image tests configuration of the image.</p>"""
    enhanced_image_metadata_enabled: NotRequired[
        "aws_sdk_imagebuilder.types.nullable_boolean.NullableBoolean"
    ]
    """<p>Collects additional information about the image being created, including the operating system (OS) version and package list. This information is used to enhance the overall experience of using EC2 Image Builder. Enabled by default.</p>"""
    tags: NotRequired["aws_sdk_imagebuilder.types.tag_map.TagMap"]
    """<p>The tags of the image.</p>"""
    client_token: "aws_sdk_imagebuilder.types.client_token.ClientToken"
    r"""<p>Unique, case-sensitive identifier you provide to ensure idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a> in the <i>Amazon EC2 API Reference</i>.</p>"""
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
        "aws_sdk_imagebuilder.types.image_logging_configuration.ImageLoggingConfiguration"
    ]
    """<p>Define logging configuration for the image build process.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateImageRequest) -> dict:
    out: dict = {}
    if "image_recipe_arn" in value:
        out["imageRecipeArn"] = value["image_recipe_arn"]
    if "container_recipe_arn" in value:
        out["containerRecipeArn"] = value["container_recipe_arn"]
    if "distribution_configuration_arn" in value:
        out["distributionConfigurationArn"] = value["distribution_configuration_arn"]
    out["infrastructureConfigurationArn"] = value["infrastructure_configuration_arn"]
    if "image_tests_configuration" in value:
        import aws_sdk_imagebuilder.types.image_tests_configuration

        out["imageTestsConfiguration"] = (
            aws_sdk_imagebuilder.types.image_tests_configuration.serialize_json(
                value["image_tests_configuration"]
            )
        )
    if "enhanced_image_metadata_enabled" in value:
        out["enhancedImageMetadataEnabled"] = value["enhanced_image_metadata_enabled"]
    if "tags" in value:
        import aws_sdk_imagebuilder.types.tag_map

        out["tags"] = aws_sdk_imagebuilder.types.tag_map.serialize_json(value["tags"])
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
        import aws_sdk_imagebuilder.types.image_logging_configuration

        out["loggingConfiguration"] = (
            aws_sdk_imagebuilder.types.image_logging_configuration.serialize_json(
                value["logging_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateImageRequest:
    out: CreateImageRequest = {}  # type: ignore[typeddict-item]
    if "imageRecipeArn" in data:
        out["image_recipe_arn"] = data["imageRecipeArn"]
    if "containerRecipeArn" in data:
        out["container_recipe_arn"] = data["containerRecipeArn"]
    if "distributionConfigurationArn" in data:
        out["distribution_configuration_arn"] = data["distributionConfigurationArn"]
    if "infrastructureConfigurationArn" in data:
        out["infrastructure_configuration_arn"] = data["infrastructureConfigurationArn"]
    else:
        raise DeserializationError(
            "CreateImageRequest.infrastructure_configuration_arn required"
        )
    if "imageTestsConfiguration" in data:
        import aws_sdk_imagebuilder.types.image_tests_configuration

        out["image_tests_configuration"] = (
            aws_sdk_imagebuilder.types.image_tests_configuration.deserialize_json(
                data["imageTestsConfiguration"]
            )
        )
    if "enhancedImageMetadataEnabled" in data:
        out["enhanced_image_metadata_enabled"] = data["enhancedImageMetadataEnabled"]
    if "tags" in data:
        import aws_sdk_imagebuilder.types.tag_map

        out["tags"] = aws_sdk_imagebuilder.types.tag_map.deserialize_json(data["tags"])
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    else:
        raise DeserializationError("CreateImageRequest.client_token required")
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
        import aws_sdk_imagebuilder.types.image_logging_configuration

        out["logging_configuration"] = (
            aws_sdk_imagebuilder.types.image_logging_configuration.deserialize_json(
                data["loggingConfiguration"]
            )
        )
    return out
