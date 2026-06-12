"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#ErrorDetailList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_partnercentral_account.types.error_detail

ErrorDetailList: TypeAlias = list[
    "aws_sdk_partnercentral_account.types.error_detail.ErrorDetail"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ErrorDetailList) -> list:
    import aws_sdk_partnercentral_account.types.error_detail

    out: list = []
    for item in value:
        out.append(
            aws_sdk_partnercentral_account.types.error_detail.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ErrorDetailList:
    import aws_sdk_partnercentral_account.types.error_detail

    out: ErrorDetailList = []
    for item in data:
        out.append(
            aws_sdk_partnercentral_account.types.error_detail.deserialize_aws_json_1_0(
                item
            )
        )
    return out
