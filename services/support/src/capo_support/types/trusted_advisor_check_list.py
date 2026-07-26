"""Generated from Smithy shape ``com.amazonaws.support#TrustedAdvisorCheckList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_support.types.trusted_advisor_check_description

TrustedAdvisorCheckList: TypeAlias = list[
    "capo_support.types.trusted_advisor_check_description.TrustedAdvisorCheckDescription"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrustedAdvisorCheckList) -> list:
    import capo_support.types.trusted_advisor_check_description

    out: list = []
    for item in value:
        out.append(
            capo_support.types.trusted_advisor_check_description.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> TrustedAdvisorCheckList:
    import capo_support.types.trusted_advisor_check_description

    out: TrustedAdvisorCheckList = []
    for item in data:
        out.append(
            capo_support.types.trusted_advisor_check_description.deserialize_aws_json_1_1(
                item
            )
        )
    return out
