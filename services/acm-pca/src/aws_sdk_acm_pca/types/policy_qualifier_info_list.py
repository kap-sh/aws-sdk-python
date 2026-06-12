"""Generated from Smithy shape ``com.amazonaws.acmpca#PolicyQualifierInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_acm_pca.types.policy_qualifier_info

PolicyQualifierInfoList: TypeAlias = list[
    "aws_sdk_acm_pca.types.policy_qualifier_info.PolicyQualifierInfo"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PolicyQualifierInfoList) -> list:
    import aws_sdk_acm_pca.types.policy_qualifier_info

    out: list = []
    for item in value:
        out.append(
            aws_sdk_acm_pca.types.policy_qualifier_info.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> PolicyQualifierInfoList:
    import aws_sdk_acm_pca.types.policy_qualifier_info

    out: PolicyQualifierInfoList = []
    for item in data:
        out.append(
            aws_sdk_acm_pca.types.policy_qualifier_info.deserialize_aws_json_1_1(item)
        )
    return out
