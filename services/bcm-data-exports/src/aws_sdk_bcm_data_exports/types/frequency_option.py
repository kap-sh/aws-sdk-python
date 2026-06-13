"""Generated from Smithy shape ``com.amazonaws.bcmdataexports#FrequencyOption``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bcm_data_exports.errors import DeserializationError

FrequencyOption: TypeAlias = Literal["SYNCHRONOUS",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("SYNCHRONOUS",))


def serialize_aws_json_1_1(value: FrequencyOption) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FrequencyOption:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FrequencyOption value: {data!r}")
    return cast(FrequencyOption, data)
