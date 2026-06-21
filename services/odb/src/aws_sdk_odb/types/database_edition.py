"""Generated from Smithy shape ``com.amazonaws.odb#DatabaseEdition``."""

from typing import Literal, TypeAlias, cast

DatabaseEdition: TypeAlias = Literal[
    "STANDARD_EDITION",
    "ENTERPRISE_EDITION",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DatabaseEdition) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> DatabaseEdition:
    return cast(DatabaseEdition, data)
