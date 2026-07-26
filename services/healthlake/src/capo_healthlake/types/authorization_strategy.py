"""Generated from Smithy shape ``com.amazonaws.healthlake#AuthorizationStrategy``."""

from typing import Literal, TypeAlias, cast

AuthorizationStrategy: TypeAlias = Literal[
    "SMART_ON_FHIR_V1",
    "SMART_ON_FHIR",
    "AWS_AUTH",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AuthorizationStrategy) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> AuthorizationStrategy:
    return cast(AuthorizationStrategy, data)
