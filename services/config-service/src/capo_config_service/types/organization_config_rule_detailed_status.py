"""Generated from Smithy shape ``com.amazonaws.configservice#OrganizationConfigRuleDetailedStatus``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_config_service.types.member_account_status

OrganizationConfigRuleDetailedStatus: TypeAlias = list[
    "capo_config_service.types.member_account_status.MemberAccountStatus"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OrganizationConfigRuleDetailedStatus) -> list:
    import capo_config_service.types.member_account_status

    out: list = []
    for item in value:
        out.append(
            capo_config_service.types.member_account_status.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> OrganizationConfigRuleDetailedStatus:
    import capo_config_service.types.member_account_status

    out: OrganizationConfigRuleDetailedStatus = []
    for item in data:
        out.append(
            capo_config_service.types.member_account_status.deserialize_aws_json_1_1(
                item
            )
        )
    return out
