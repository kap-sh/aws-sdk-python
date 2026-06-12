"""Generated from Smithy shape ``com.amazonaws.imagebuilder#GetDistributionConfigurationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.distribution_configuration
    import aws_sdk_imagebuilder.types.non_empty_string


class GetDistributionConfigurationResponse(TypedDict):
    request_id: NotRequired[
        "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    """<p>The request ID that uniquely identifies this request.</p>"""
    distribution_configuration: NotRequired[
        "aws_sdk_imagebuilder.types.distribution_configuration.DistributionConfiguration"
    ]
    """<p>The distribution configuration object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDistributionConfigurationResponse) -> dict:
    out: dict = {}
    if "request_id" in value:
        out["requestId"] = value["request_id"]
    if "distribution_configuration" in value:
        import aws_sdk_imagebuilder.types.distribution_configuration

        out["distributionConfiguration"] = (
            aws_sdk_imagebuilder.types.distribution_configuration.serialize_json(
                value["distribution_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetDistributionConfigurationResponse:
    out: GetDistributionConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "requestId" in data:
        out["request_id"] = data["requestId"]
    if "distributionConfiguration" in data:
        import aws_sdk_imagebuilder.types.distribution_configuration

        out["distribution_configuration"] = (
            aws_sdk_imagebuilder.types.distribution_configuration.deserialize_json(
                data["distributionConfiguration"]
            )
        )
    return out
