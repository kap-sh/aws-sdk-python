"""Generated from Smithy shape ``com.amazonaws.imagebuilder#DeleteInfrastructureConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.infrastructure_configuration_arn


class DeleteInfrastructureConfigurationRequest(TypedDict):
    infrastructure_configuration_arn: "aws_sdk_imagebuilder.types.infrastructure_configuration_arn.InfrastructureConfigurationArn"
    """<p>The Amazon Resource Name (ARN) of the infrastructure configuration to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteInfrastructureConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteInfrastructureConfigurationRequest:
    out: DeleteInfrastructureConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
