"""Generated from Smithy shape ``com.amazonaws.sagemaker#Peft``."""

from typing import Literal, TypeAlias, cast

Peft: TypeAlias = Literal["LORA",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Peft) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Peft:
    return cast(Peft, data)
