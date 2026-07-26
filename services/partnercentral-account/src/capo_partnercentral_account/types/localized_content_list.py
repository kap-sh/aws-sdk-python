"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#LocalizedContentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_account.types.localized_content

LocalizedContentList: TypeAlias = list[
    "capo_partnercentral_account.types.localized_content.LocalizedContent"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LocalizedContentList) -> list:
    import capo_partnercentral_account.types.localized_content

    out: list = []
    for item in value:
        out.append(
            capo_partnercentral_account.types.localized_content.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> LocalizedContentList:
    import capo_partnercentral_account.types.localized_content

    out: LocalizedContentList = []
    for item in data:
        out.append(
            capo_partnercentral_account.types.localized_content.deserialize_aws_json_1_0(
                item
            )
        )
    return out
