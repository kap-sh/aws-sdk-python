"""Generated from Smithy shape ``com.amazonaws.workmail#PersonalAccessTokenSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workmail.types.personal_access_token_summary

PersonalAccessTokenSummaryList: TypeAlias = list[
    "capo_workmail.types.personal_access_token_summary.PersonalAccessTokenSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PersonalAccessTokenSummaryList) -> list:
    import capo_workmail.types.personal_access_token_summary

    out: list = []
    for item in value:
        out.append(
            capo_workmail.types.personal_access_token_summary.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> PersonalAccessTokenSummaryList:
    import capo_workmail.types.personal_access_token_summary

    out: PersonalAccessTokenSummaryList = []
    for item in data:
        out.append(
            capo_workmail.types.personal_access_token_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
