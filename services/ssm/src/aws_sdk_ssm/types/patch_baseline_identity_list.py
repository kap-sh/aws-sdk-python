"""Generated from Smithy shape ``com.amazonaws.ssm#PatchBaselineIdentityList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.patch_baseline_identity

PatchBaselineIdentityList: TypeAlias = list[
    "aws_sdk_ssm.types.patch_baseline_identity.PatchBaselineIdentity"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PatchBaselineIdentityList) -> list:
    import aws_sdk_ssm.types.patch_baseline_identity

    out: list = []
    for item in value:
        out.append(
            aws_sdk_ssm.types.patch_baseline_identity.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> PatchBaselineIdentityList:
    import aws_sdk_ssm.types.patch_baseline_identity

    out: PatchBaselineIdentityList = []
    for item in data:
        out.append(
            aws_sdk_ssm.types.patch_baseline_identity.deserialize_aws_json_1_1(item)
        )
    return out
