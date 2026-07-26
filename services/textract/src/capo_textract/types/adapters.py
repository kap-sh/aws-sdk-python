"""Generated from Smithy shape ``com.amazonaws.textract#Adapters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_textract.types.adapter

Adapters: TypeAlias = list["capo_textract.types.adapter.Adapter"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Adapters) -> list:
    import capo_textract.types.adapter

    out: list = []
    for item in value:
        out.append(capo_textract.types.adapter.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Adapters:
    import capo_textract.types.adapter

    out: Adapters = []
    for item in data:
        out.append(capo_textract.types.adapter.deserialize_aws_json_1_1(item))
    return out
