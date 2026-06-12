"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#DefinitionLanguage``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotthingsgraph.errors import DeserializationError

DefinitionLanguage: TypeAlias = Literal["GRAPHQL",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("GRAPHQL",))


def serialize_aws_json_1_1(value: DefinitionLanguage) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DefinitionLanguage:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DefinitionLanguage value: {data!r}")
    return cast(DefinitionLanguage, data)
