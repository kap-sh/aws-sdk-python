"""Generated from Smithy shape ``com.amazonaws.kendra#IndexEdition``."""

from typing import Literal, TypeAlias, cast

IndexEdition: TypeAlias = Literal[
    "DEVELOPER_EDITION",
    "ENTERPRISE_EDITION",
    "GEN_AI_ENTERPRISE_EDITION",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IndexEdition) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> IndexEdition:
    return cast(IndexEdition, data)
