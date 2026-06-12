"""Generated from Smithy shape ``com.amazonaws.imagebuilder#DeleteDistributionConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.distribution_configuration_arn


class DeleteDistributionConfigurationRequest(TypedDict):
    distribution_configuration_arn: "aws_sdk_imagebuilder.types.distribution_configuration_arn.DistributionConfigurationArn"
    """<p>The Amazon Resource Name (ARN) of the distribution configuration to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDistributionConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteDistributionConfigurationRequest:
    out: DeleteDistributionConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
