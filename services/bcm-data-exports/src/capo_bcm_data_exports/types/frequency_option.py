"""Generated from Smithy shape ``com.amazonaws.bcmdataexports#FrequencyOption``."""

from typing import Literal, TypeAlias, cast

FrequencyOption: TypeAlias = Literal["SYNCHRONOUS",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FrequencyOption) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FrequencyOption:
    return cast(FrequencyOption, data)
