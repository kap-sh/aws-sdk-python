"""Generated from Smithy shape ``com.amazonaws.imagebuilder#GetDistributionConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.distribution_configuration_arn


class GetDistributionConfigurationRequest(TypedDict, closed=True):
    distribution_configuration_arn: "aws_sdk_imagebuilder.types.distribution_configuration_arn.DistributionConfigurationArn"
    """<p>The Amazon Resource Name (ARN) of the distribution configuration that you want to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDistributionConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDistributionConfigurationRequest:
    out: GetDistributionConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
