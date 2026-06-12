"""Generated from Smithy shape ``com.amazonaws.imagebuilder#GetInfrastructureConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.infrastructure_configuration_arn


class GetInfrastructureConfigurationRequest(TypedDict):
    infrastructure_configuration_arn: "aws_sdk_imagebuilder.types.infrastructure_configuration_arn.InfrastructureConfigurationArn"
    """<p>The Amazon Resource Name (ARN) of the infrastructure configuration that you want to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetInfrastructureConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetInfrastructureConfigurationRequest:
    out: GetInfrastructureConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
