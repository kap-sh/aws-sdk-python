"""Generated from Smithy shape ``com.amazonaws.personalize#RecipeProvider``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_personalize.errors import DeserializationError

RecipeProvider: TypeAlias = Literal["SERVICE",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("SERVICE",))


def serialize_aws_json_1_1(value: RecipeProvider) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RecipeProvider:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RecipeProvider value: {data!r}")
    return cast(RecipeProvider, data)
