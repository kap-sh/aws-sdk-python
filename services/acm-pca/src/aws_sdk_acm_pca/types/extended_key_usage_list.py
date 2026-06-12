"""Generated from Smithy shape ``com.amazonaws.acmpca#ExtendedKeyUsageList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_acm_pca.types.extended_key_usage

ExtendedKeyUsageList: TypeAlias = list[
    "aws_sdk_acm_pca.types.extended_key_usage.ExtendedKeyUsage"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExtendedKeyUsageList) -> list:
    import aws_sdk_acm_pca.types.extended_key_usage

    out: list = []
    for item in value:
        out.append(
            aws_sdk_acm_pca.types.extended_key_usage.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ExtendedKeyUsageList:
    import aws_sdk_acm_pca.types.extended_key_usage

    out: ExtendedKeyUsageList = []
    for item in data:
        out.append(
            aws_sdk_acm_pca.types.extended_key_usage.deserialize_aws_json_1_1(item)
        )
    return out
