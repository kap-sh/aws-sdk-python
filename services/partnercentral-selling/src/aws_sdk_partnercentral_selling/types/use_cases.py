"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#UseCases``."""

from typing import TypeAlias

UseCases: TypeAlias = list["str"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UseCases) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> UseCases:
    return list(data)
