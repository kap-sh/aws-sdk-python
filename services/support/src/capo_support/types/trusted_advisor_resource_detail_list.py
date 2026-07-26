"""Generated from Smithy shape ``com.amazonaws.support#TrustedAdvisorResourceDetailList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_support.types.trusted_advisor_resource_detail

TrustedAdvisorResourceDetailList: TypeAlias = list[
    "capo_support.types.trusted_advisor_resource_detail.TrustedAdvisorResourceDetail"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrustedAdvisorResourceDetailList) -> list:
    import capo_support.types.trusted_advisor_resource_detail

    out: list = []
    for item in value:
        out.append(
            capo_support.types.trusted_advisor_resource_detail.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> TrustedAdvisorResourceDetailList:
    import capo_support.types.trusted_advisor_resource_detail

    out: TrustedAdvisorResourceDetailList = []
    for item in data:
        out.append(
            capo_support.types.trusted_advisor_resource_detail.deserialize_aws_json_1_1(
                item
            )
        )
    return out
