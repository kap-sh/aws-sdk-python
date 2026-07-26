"""Generated from Smithy shape ``com.amazonaws.personalize#RecipeProvider``."""

from typing import Literal, TypeAlias, cast

RecipeProvider: TypeAlias = Literal["SERVICE",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RecipeProvider) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RecipeProvider:
    return cast(RecipeProvider, data)
