"""Generated from Smithy shape ``com.amazonaws.lightsail#GetDistributionBundlesResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.distribution_bundle_list


class GetDistributionBundlesResult(TypedDict):
    bundles: NotRequired[
        "aws_sdk_lightsail.types.distribution_bundle_list.DistributionBundleList"
    ]
    """<p>An object that describes a distribution bundle.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDistributionBundlesResult) -> dict:
    out: dict = {}
    if "bundles" in value:
        import aws_sdk_lightsail.types.distribution_bundle_list

        out["bundles"] = (
            aws_sdk_lightsail.types.distribution_bundle_list.serialize_aws_json_1_1(
                value["bundles"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDistributionBundlesResult:
    out: GetDistributionBundlesResult = {}  # type: ignore[typeddict-item]
    if "bundles" in data:
        import aws_sdk_lightsail.types.distribution_bundle_list

        out["bundles"] = (
            aws_sdk_lightsail.types.distribution_bundle_list.deserialize_aws_json_1_1(
                data["bundles"]
            )
        )
    return out
