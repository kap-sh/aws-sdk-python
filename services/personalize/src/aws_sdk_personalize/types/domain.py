"""Generated from Smithy shape ``com.amazonaws.personalize#Domain``."""

from typing import Literal, TypeAlias, cast

Domain: TypeAlias = Literal[
    "ECOMMERCE",
    "VIDEO_ON_DEMAND",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Domain) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Domain:
    return cast(Domain, data)
