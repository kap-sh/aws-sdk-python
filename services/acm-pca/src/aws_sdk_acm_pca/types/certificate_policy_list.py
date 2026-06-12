"""Generated from Smithy shape ``com.amazonaws.acmpca#CertificatePolicyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_acm_pca.types.policy_information

CertificatePolicyList: TypeAlias = list[
    "aws_sdk_acm_pca.types.policy_information.PolicyInformation"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CertificatePolicyList) -> list:
    import aws_sdk_acm_pca.types.policy_information

    out: list = []
    for item in value:
        out.append(
            aws_sdk_acm_pca.types.policy_information.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> CertificatePolicyList:
    import aws_sdk_acm_pca.types.policy_information

    out: CertificatePolicyList = []
    for item in data:
        out.append(
            aws_sdk_acm_pca.types.policy_information.deserialize_aws_json_1_1(item)
        )
    return out
