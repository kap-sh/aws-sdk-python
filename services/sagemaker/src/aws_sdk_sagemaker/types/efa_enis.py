"""Generated from Smithy shape ``com.amazonaws.sagemaker#EfaEnis``."""

from typing import TypeAlias

EfaEnis: TypeAlias = list["str"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EfaEnis) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> EfaEnis:
    return list(data)
