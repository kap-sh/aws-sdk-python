"""Generated from Smithy shape ``com.amazonaws.support#TrustedAdvisorCheckRefreshStatusList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_support.types.trusted_advisor_check_refresh_status

TrustedAdvisorCheckRefreshStatusList: TypeAlias = list[
    "capo_support.types.trusted_advisor_check_refresh_status.TrustedAdvisorCheckRefreshStatus"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrustedAdvisorCheckRefreshStatusList) -> list:
    import capo_support.types.trusted_advisor_check_refresh_status

    out: list = []
    for item in value:
        out.append(
            capo_support.types.trusted_advisor_check_refresh_status.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> TrustedAdvisorCheckRefreshStatusList:
    import capo_support.types.trusted_advisor_check_refresh_status

    out: TrustedAdvisorCheckRefreshStatusList = []
    for item in data:
        out.append(
            capo_support.types.trusted_advisor_check_refresh_status.deserialize_aws_json_1_1(
                item
            )
        )
    return out
