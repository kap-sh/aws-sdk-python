"""Generated from Smithy shape ``com.amazonaws.lightsail#GetBucketBundlesResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.bucket_bundle_list


class GetBucketBundlesResult(TypedDict):
    bundles: NotRequired["aws_sdk_lightsail.types.bucket_bundle_list.BucketBundleList"]
    """<p>An object that describes bucket bundles.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetBucketBundlesResult) -> dict:
    out: dict = {}
    if "bundles" in value:
        import aws_sdk_lightsail.types.bucket_bundle_list

        out["bundles"] = (
            aws_sdk_lightsail.types.bucket_bundle_list.serialize_aws_json_1_1(
                value["bundles"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetBucketBundlesResult:
    out: GetBucketBundlesResult = {}  # type: ignore[typeddict-item]
    if "bundles" in data:
        import aws_sdk_lightsail.types.bucket_bundle_list

        out["bundles"] = (
            aws_sdk_lightsail.types.bucket_bundle_list.deserialize_aws_json_1_1(
                data["bundles"]
            )
        )
    return out
