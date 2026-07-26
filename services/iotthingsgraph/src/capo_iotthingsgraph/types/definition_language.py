"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#DefinitionLanguage``."""

from typing import Literal, TypeAlias, cast

DefinitionLanguage: TypeAlias = Literal["GRAPHQL",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DefinitionLanguage) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DefinitionLanguage:
    return cast(DefinitionLanguage, data)
