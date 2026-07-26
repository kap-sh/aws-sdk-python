"""Generated from Smithy shape ``com.amazonaws.imagebuilder#DistributeImageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_imagebuilder.errors import DeserializationError

if TYPE_CHECKING:
    import capo_imagebuilder.types.client_token
    import capo_imagebuilder.types.distribution_configuration_arn
    import capo_imagebuilder.types.image_logging_configuration
    import capo_imagebuilder.types.non_empty_string
    import capo_imagebuilder.types.role_name_or_arn
    import capo_imagebuilder.types.tag_map


class DistributeImageRequest(TypedDict, closed=True):
    source_image: "capo_imagebuilder.types.non_empty_string.NonEmptyString"
    """<p>The source image Amazon Resource Name (ARN) to distribute.</p>"""
    distribution_configuration_arn: "capo_imagebuilder.types.distribution_configuration_arn.DistributionConfigurationArn"
    """<p>The Amazon Resource Name (ARN) of the distribution configuration to use.</p>"""
    execution_role: "capo_imagebuilder.types.role_name_or_arn.RoleNameOrArn"
    """<p>The IAM role to use for the distribution.</p>"""
    tags: NotRequired["capo_imagebuilder.types.tag_map.TagMap"]
    """<p>The tags to apply to the distributed image.</p>"""
    client_token: "capo_imagebuilder.types.client_token.ClientToken"
    r"""<p>Unique, case-sensitive identifier you provide to ensure idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a> in the <i>Amazon EC2 API Reference</i>.</p>"""
    logging_configuration: NotRequired[
        "capo_imagebuilder.types.image_logging_configuration.ImageLoggingConfiguration"
    ]
    """<p>The logging configuration for the distribution.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DistributeImageRequest) -> dict:
    out: dict = {}
    out["sourceImage"] = value["source_image"]
    out["distributionConfigurationArn"] = value["distribution_configuration_arn"]
    out["executionRole"] = value["execution_role"]
    if "tags" in value:
        import capo_imagebuilder.types.tag_map

        out["tags"] = capo_imagebuilder.types.tag_map.serialize_json(value["tags"])
    out["clientToken"] = value["client_token"]
    if "logging_configuration" in value:
        import capo_imagebuilder.types.image_logging_configuration

        out["loggingConfiguration"] = (
            capo_imagebuilder.types.image_logging_configuration.serialize_json(
                value["logging_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> DistributeImageRequest:
    out: DistributeImageRequest = {}  # type: ignore[typeddict-item]
    if "sourceImage" in data:
        out["source_image"] = data["sourceImage"]
    else:
        raise DeserializationError("DistributeImageRequest.source_image required")
    if "distributionConfigurationArn" in data:
        out["distribution_configuration_arn"] = data["distributionConfigurationArn"]
    else:
        raise DeserializationError(
            "DistributeImageRequest.distribution_configuration_arn required"
        )
    if "executionRole" in data:
        out["execution_role"] = data["executionRole"]
    else:
        raise DeserializationError("DistributeImageRequest.execution_role required")
    if "tags" in data:
        import capo_imagebuilder.types.tag_map

        out["tags"] = capo_imagebuilder.types.tag_map.deserialize_json(data["tags"])
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    else:
        raise DeserializationError("DistributeImageRequest.client_token required")
    if "loggingConfiguration" in data:
        import capo_imagebuilder.types.image_logging_configuration

        out["logging_configuration"] = (
            capo_imagebuilder.types.image_logging_configuration.deserialize_json(
                data["loggingConfiguration"]
            )
        )
    return out
