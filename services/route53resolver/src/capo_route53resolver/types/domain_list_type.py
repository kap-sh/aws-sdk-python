"""Generated from Smithy shape ``com.amazonaws.route53resolver#DomainListType``."""

from typing import Literal, TypeAlias, cast

DomainListType: TypeAlias = Literal[
    "THREAT",
    "CONTENT",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DomainListType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DomainListType:
    return cast(DomainListType, data)
