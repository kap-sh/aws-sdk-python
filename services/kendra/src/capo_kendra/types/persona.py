"""Generated from Smithy shape ``com.amazonaws.kendra#Persona``."""

from typing import Literal, TypeAlias, cast

Persona: TypeAlias = Literal[
    "OWNER",
    "VIEWER",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Persona) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Persona:
    return cast(Persona, data)
