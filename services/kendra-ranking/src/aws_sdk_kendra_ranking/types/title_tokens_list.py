"""Generated from Smithy shape ``com.amazonaws.kendraranking#TitleTokensList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kendra_ranking.types.tokens

TitleTokensList: TypeAlias = list["aws_sdk_kendra_ranking.types.tokens.Tokens"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TitleTokensList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> TitleTokensList:
    return list(data)
