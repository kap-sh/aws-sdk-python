"""Generated from Smithy shape ``com.amazonaws.lightsail#BucketBundleList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lightsail.types.bucket_bundle

BucketBundleList: TypeAlias = list["capo_lightsail.types.bucket_bundle.BucketBundle"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BucketBundleList) -> list:
    import capo_lightsail.types.bucket_bundle

    out: list = []
    for item in value:
        out.append(capo_lightsail.types.bucket_bundle.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> BucketBundleList:
    import capo_lightsail.types.bucket_bundle

    out: BucketBundleList = []
    for item in data:
        out.append(capo_lightsail.types.bucket_bundle.deserialize_aws_json_1_1(item))
    return out
