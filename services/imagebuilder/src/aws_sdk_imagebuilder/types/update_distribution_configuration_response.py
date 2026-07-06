"""Generated from Smithy shape ``com.amazonaws.imagebuilder#UpdateDistributionConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.client_token
    import aws_sdk_imagebuilder.types.distribution_configuration_arn
    import aws_sdk_imagebuilder.types.non_empty_string


class UpdateDistributionConfigurationResponse(TypedDict, closed=True):
    request_id: NotRequired[
        "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    """<p>The request ID that uniquely identifies this request.</p>"""
    client_token: NotRequired["aws_sdk_imagebuilder.types.client_token.ClientToken"]
    """<p>The client token that uniquely identifies the request.</p>"""
    distribution_configuration_arn: NotRequired[
        "aws_sdk_imagebuilder.types.distribution_configuration_arn.DistributionConfigurationArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the distribution configuration that was updated by this request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDistributionConfigurationResponse) -> dict:
    out: dict = {}
    if "request_id" in value:
        out["requestId"] = value["request_id"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "distribution_configuration_arn" in value:
        out["distributionConfigurationArn"] = value["distribution_configuration_arn"]
    return out


def deserialize_json(data: dict) -> UpdateDistributionConfigurationResponse:
    out: UpdateDistributionConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "requestId" in data:
        out["request_id"] = data["requestId"]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "distributionConfigurationArn" in data:
        out["distribution_configuration_arn"] = data["distributionConfigurationArn"]
    return out
