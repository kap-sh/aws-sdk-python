"""Generated from Smithy shape ``com.amazonaws.acmpca#ExtendedKeyUsageList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_acm_pca.types.extended_key_usage

ExtendedKeyUsageList: TypeAlias = list[
    "capo_acm_pca.types.extended_key_usage.ExtendedKeyUsage"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExtendedKeyUsageList) -> list:
    import capo_acm_pca.types.extended_key_usage

    out: list = []
    for item in value:
        out.append(capo_acm_pca.types.extended_key_usage.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ExtendedKeyUsageList:
    import capo_acm_pca.types.extended_key_usage

    out: ExtendedKeyUsageList = []
    for item in data:
        out.append(capo_acm_pca.types.extended_key_usage.deserialize_aws_json_1_1(item))
    return out
