"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#PartnerDomainList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_partnercentral_account.types.partner_domain

PartnerDomainList: TypeAlias = list[
    "aws_sdk_partnercentral_account.types.partner_domain.PartnerDomain"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PartnerDomainList) -> list:
    import aws_sdk_partnercentral_account.types.partner_domain

    out: list = []
    for item in value:
        out.append(
            aws_sdk_partnercentral_account.types.partner_domain.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> PartnerDomainList:
    import aws_sdk_partnercentral_account.types.partner_domain

    out: PartnerDomainList = []
    for item in data:
        out.append(
            aws_sdk_partnercentral_account.types.partner_domain.deserialize_aws_json_1_0(
                item
            )
        )
    return out
