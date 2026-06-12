"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#LocalizedContentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_partnercentral_account.types.localized_content

LocalizedContentList: TypeAlias = list[
    "aws_sdk_partnercentral_account.types.localized_content.LocalizedContent"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LocalizedContentList) -> list:
    import aws_sdk_partnercentral_account.types.localized_content

    out: list = []
    for item in value:
        out.append(
            aws_sdk_partnercentral_account.types.localized_content.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> LocalizedContentList:
    import aws_sdk_partnercentral_account.types.localized_content

    out: LocalizedContentList = []
    for item in data:
        out.append(
            aws_sdk_partnercentral_account.types.localized_content.deserialize_aws_json_1_0(
                item
            )
        )
    return out
