"""Generated from Smithy shape ``com.amazonaws.sagemaker#PartnerAppAdminUserList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.non_empty_string256

PartnerAppAdminUserList: TypeAlias = list[
    "aws_sdk_sagemaker.types.non_empty_string256.NonEmptyString256"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PartnerAppAdminUserList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> PartnerAppAdminUserList:
    return list(data)
