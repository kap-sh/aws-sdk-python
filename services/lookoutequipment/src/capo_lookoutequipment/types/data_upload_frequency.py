"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#DataUploadFrequency``."""

from typing import Literal, TypeAlias, cast

DataUploadFrequency: TypeAlias = Literal[
    "PT5M",
    "PT10M",
    "PT15M",
    "PT30M",
    "PT1H",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DataUploadFrequency) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> DataUploadFrequency:
    return cast(DataUploadFrequency, data)
