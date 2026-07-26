"""Generated from Smithy shape ``com.amazonaws.lightsail#CreateDistributionResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.lightsail_distribution
    import capo_lightsail.types.operation


class CreateDistributionResult(TypedDict, closed=True):
    distribution: NotRequired[
        "capo_lightsail.types.lightsail_distribution.LightsailDistribution"
    ]
    """<p>An object that describes the distribution created.</p>"""
    operation: NotRequired["capo_lightsail.types.operation.Operation"]
    """<p>An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateDistributionResult) -> dict:
    out: dict = {}
    if "distribution" in value:
        import capo_lightsail.types.lightsail_distribution

        out["distribution"] = (
            capo_lightsail.types.lightsail_distribution.serialize_aws_json_1_1(
                value["distribution"]
            )
        )
    if "operation" in value:
        import capo_lightsail.types.operation

        out["operation"] = capo_lightsail.types.operation.serialize_aws_json_1_1(
            value["operation"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateDistributionResult:
    out: CreateDistributionResult = {}  # type: ignore[typeddict-item]
    if "distribution" in data:
        import capo_lightsail.types.lightsail_distribution

        out["distribution"] = (
            capo_lightsail.types.lightsail_distribution.deserialize_aws_json_1_1(
                data["distribution"]
            )
        )
    if "operation" in data:
        import capo_lightsail.types.operation

        out["operation"] = capo_lightsail.types.operation.deserialize_aws_json_1_1(
            data["operation"]
        )
    return out
