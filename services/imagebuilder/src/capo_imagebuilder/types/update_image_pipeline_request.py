"""Generated from Smithy shape ``com.amazonaws.imagebuilder#UpdateImagePipelineRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_imagebuilder.errors import DeserializationError

if TYPE_CHECKING:
    import capo_imagebuilder.types.client_token
    import capo_imagebuilder.types.container_recipe_arn
    import capo_imagebuilder.types.distribution_configuration_arn
    import capo_imagebuilder.types.image_pipeline_arn
    import capo_imagebuilder.types.image_recipe_arn
    import capo_imagebuilder.types.image_scanning_configuration
    import capo_imagebuilder.types.image_tests_configuration
    import capo_imagebuilder.types.infrastructure_configuration_arn
    import capo_imagebuilder.types.non_empty_string
    import capo_imagebuilder.types.nullable_boolean
    import capo_imagebuilder.types.pipeline_logging_configuration
    import capo_imagebuilder.types.pipeline_status
    import capo_imagebuilder.types.role_name_or_arn
    import capo_imagebuilder.types.schedule
    import capo_imagebuilder.types.tag_map
    import capo_imagebuilder.types.workflow_configuration_list


class UpdateImagePipelineRequest(TypedDict, closed=True):
    image_pipeline_arn: "capo_imagebuilder.types.image_pipeline_arn.ImagePipelineArn"
    """<p>The Amazon Resource Name (ARN) of the image pipeline that you want to update.</p>"""
    description: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The description of the image pipeline.</p>"""
    image_recipe_arn: NotRequired[
        "capo_imagebuilder.types.image_recipe_arn.ImageRecipeArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the image recipe that will be used to configure images updated by this image pipeline.</p>"""
    container_recipe_arn: NotRequired[
        "capo_imagebuilder.types.container_recipe_arn.ContainerRecipeArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the container pipeline to update.</p>"""
    infrastructure_configuration_arn: "capo_imagebuilder.types.infrastructure_configuration_arn.InfrastructureConfigurationArn"
    """<p>The Amazon Resource Name (ARN) of the infrastructure configuration that Image Builder uses to build images that this image pipeline has updated.</p>"""
    distribution_configuration_arn: NotRequired[
        "capo_imagebuilder.types.distribution_configuration_arn.DistributionConfigurationArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the distribution configuration that Image Builder uses to configure and distribute images that this image pipeline has updated.</p>"""
    image_tests_configuration: NotRequired[
        "capo_imagebuilder.types.image_tests_configuration.ImageTestsConfiguration"
    ]
    """<p>The image test configuration of the image pipeline.</p>"""
    enhanced_image_metadata_enabled: NotRequired[
        "capo_imagebuilder.types.nullable_boolean.NullableBoolean"
    ]
    """<p>Collects additional information about the image being created, including the operating system (OS) version and package list. This information is used to enhance the overall experience of using EC2 Image Builder. Enabled by default.</p>"""
    schedule: NotRequired["capo_imagebuilder.types.schedule.Schedule"]
    """<p>The schedule of the image pipeline.</p>"""
    status: NotRequired["capo_imagebuilder.types.pipeline_status.PipelineStatus"]
    """<p>The status of the image pipeline.</p>"""
    client_token: "capo_imagebuilder.types.client_token.ClientToken"
    r"""<p>Unique, case-sensitive identifier you provide to ensure idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a> in the <i>Amazon EC2 API Reference</i>.</p>"""
    image_scanning_configuration: NotRequired[
        "capo_imagebuilder.types.image_scanning_configuration.ImageScanningConfiguration"
    ]
    """<p>Contains settings for vulnerability scans.</p>"""
    workflows: NotRequired[
        "capo_imagebuilder.types.workflow_configuration_list.WorkflowConfigurationList"
    ]
    """<p>Contains the workflows to run for the pipeline.</p>"""
    logging_configuration: NotRequired[
        "capo_imagebuilder.types.pipeline_logging_configuration.PipelineLoggingConfiguration"
    ]
    """<p>Update logging configuration for the output image that's created when the pipeline runs.</p>"""
    execution_role: NotRequired[
        "capo_imagebuilder.types.role_name_or_arn.RoleNameOrArn"
    ]
    """<p>The name or Amazon Resource Name (ARN) for the IAM role you create that grants Image Builder access to perform workflow actions.</p>"""
    image_tags: NotRequired["capo_imagebuilder.types.tag_map.TagMap"]
    """<p>The tags to be applied to the images produced by this pipeline.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateImagePipelineRequest) -> dict:
    out: dict = {}
    out["imagePipelineArn"] = value["image_pipeline_arn"]
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
        import capo_imagebuilder.types.image_tests_configuration

        out["imageTestsConfiguration"] = (
            capo_imagebuilder.types.image_tests_configuration.serialize_json(
                value["image_tests_configuration"]
            )
        )
    if "enhanced_image_metadata_enabled" in value:
        out["enhancedImageMetadataEnabled"] = value["enhanced_image_metadata_enabled"]
    if "schedule" in value:
        import capo_imagebuilder.types.schedule

        out["schedule"] = capo_imagebuilder.types.schedule.serialize_json(
            value["schedule"]
        )
    if "status" in value:
        import capo_imagebuilder.types.pipeline_status

        out["status"] = capo_imagebuilder.types.pipeline_status.serialize_json(
            value["status"]
        )
    out["clientToken"] = value["client_token"]
    if "image_scanning_configuration" in value:
        import capo_imagebuilder.types.image_scanning_configuration

        out["imageScanningConfiguration"] = (
            capo_imagebuilder.types.image_scanning_configuration.serialize_json(
                value["image_scanning_configuration"]
            )
        )
    if "workflows" in value:
        import capo_imagebuilder.types.workflow_configuration_list

        out["workflows"] = (
            capo_imagebuilder.types.workflow_configuration_list.serialize_json(
                value["workflows"]
            )
        )
    if "logging_configuration" in value:
        import capo_imagebuilder.types.pipeline_logging_configuration

        out["loggingConfiguration"] = (
            capo_imagebuilder.types.pipeline_logging_configuration.serialize_json(
                value["logging_configuration"]
            )
        )
    if "execution_role" in value:
        out["executionRole"] = value["execution_role"]
    if "image_tags" in value:
        import capo_imagebuilder.types.tag_map

        out["imageTags"] = capo_imagebuilder.types.tag_map.serialize_json(
            value["image_tags"]
        )
    return out


def deserialize_json(data: dict) -> UpdateImagePipelineRequest:
    out: UpdateImagePipelineRequest = {}  # type: ignore[typeddict-item]
    if "imagePipelineArn" in data:
        out["image_pipeline_arn"] = data["imagePipelineArn"]
    else:
        raise DeserializationError(
            "UpdateImagePipelineRequest.image_pipeline_arn required"
        )
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
            "UpdateImagePipelineRequest.infrastructure_configuration_arn required"
        )
    if "distributionConfigurationArn" in data:
        out["distribution_configuration_arn"] = data["distributionConfigurationArn"]
    if "imageTestsConfiguration" in data:
        import capo_imagebuilder.types.image_tests_configuration

        out["image_tests_configuration"] = (
            capo_imagebuilder.types.image_tests_configuration.deserialize_json(
                data["imageTestsConfiguration"]
            )
        )
    if "enhancedImageMetadataEnabled" in data:
        out["enhanced_image_metadata_enabled"] = data["enhancedImageMetadataEnabled"]
    if "schedule" in data:
        import capo_imagebuilder.types.schedule

        out["schedule"] = capo_imagebuilder.types.schedule.deserialize_json(
            data["schedule"]
        )
    if "status" in data:
        import capo_imagebuilder.types.pipeline_status

        out["status"] = capo_imagebuilder.types.pipeline_status.deserialize_json(
            data["status"]
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    else:
        raise DeserializationError("UpdateImagePipelineRequest.client_token required")
    if "imageScanningConfiguration" in data:
        import capo_imagebuilder.types.image_scanning_configuration

        out["image_scanning_configuration"] = (
            capo_imagebuilder.types.image_scanning_configuration.deserialize_json(
                data["imageScanningConfiguration"]
            )
        )
    if "workflows" in data:
        import capo_imagebuilder.types.workflow_configuration_list

        out["workflows"] = (
            capo_imagebuilder.types.workflow_configuration_list.deserialize_json(
                data["workflows"]
            )
        )
    if "loggingConfiguration" in data:
        import capo_imagebuilder.types.pipeline_logging_configuration

        out["logging_configuration"] = (
            capo_imagebuilder.types.pipeline_logging_configuration.deserialize_json(
                data["loggingConfiguration"]
            )
        )
    if "executionRole" in data:
        out["execution_role"] = data["executionRole"]
    if "imageTags" in data:
        import capo_imagebuilder.types.tag_map

        out["image_tags"] = capo_imagebuilder.types.tag_map.deserialize_json(
            data["imageTags"]
        )
    return out
