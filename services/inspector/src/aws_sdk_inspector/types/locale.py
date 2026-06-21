"""Generated from Smithy shape ``com.amazonaws.inspector#Locale``."""

from typing import Literal, TypeAlias, cast

Locale: TypeAlias = Literal["EN_US",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Locale) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Locale:
    return cast(Locale, data)
