"""Generated from Smithy shape ``com.amazonaws.freetier#MatchOptions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_freetier.types.match_option

MatchOptions: TypeAlias = list["capo_freetier.types.match_option.MatchOption"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MatchOptions) -> list:
    import capo_freetier.types.match_option

    out: list = []
    for item in value:
        out.append(capo_freetier.types.match_option.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> MatchOptions:
    import capo_freetier.types.match_option

    out: MatchOptions = []
    for item in data:
        out.append(capo_freetier.types.match_option.deserialize_aws_json_1_0(item))
    return out
