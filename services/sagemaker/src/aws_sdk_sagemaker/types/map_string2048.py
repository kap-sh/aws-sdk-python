"""Generated from Smithy shape ``com.amazonaws.sagemaker#MapString2048``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.string2048

MapString2048: TypeAlias = dict[
    "aws_sdk_sagemaker.types.string2048.String2048",
    "aws_sdk_sagemaker.types.string2048.String2048",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: MapString2048) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> MapString2048:
    out: MapString2048 = {}
    for key, value in data.items():
        out[key] = value
    return out
