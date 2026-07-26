"""Generated from Smithy shape ``com.amazonaws.budgets#MatchOptions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_budgets.types.match_option

MatchOptions: TypeAlias = list["capo_budgets.types.match_option.MatchOption"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MatchOptions) -> list:
    import capo_budgets.types.match_option

    out: list = []
    for item in value:
        out.append(capo_budgets.types.match_option.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> MatchOptions:
    import capo_budgets.types.match_option

    out: MatchOptions = []
    for item in data:
        out.append(capo_budgets.types.match_option.deserialize_aws_json_1_1(item))
    return out
