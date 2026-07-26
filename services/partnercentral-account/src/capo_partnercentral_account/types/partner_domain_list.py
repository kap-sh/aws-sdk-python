"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#PartnerDomainList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_account.types.partner_domain

PartnerDomainList: TypeAlias = list[
    "capo_partnercentral_account.types.partner_domain.PartnerDomain"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PartnerDomainList) -> list:
    import capo_partnercentral_account.types.partner_domain

    out: list = []
    for item in value:
        out.append(
            capo_partnercentral_account.types.partner_domain.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> PartnerDomainList:
    import capo_partnercentral_account.types.partner_domain

    out: PartnerDomainList = []
    for item in data:
        out.append(
            capo_partnercentral_account.types.partner_domain.deserialize_aws_json_1_0(
                item
            )
        )
    return out
