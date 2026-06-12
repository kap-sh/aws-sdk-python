"""Generated from Smithy shape ``com.amazonaws.frauddetector#Language``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_frauddetector.errors import DeserializationError

Language: TypeAlias = Literal["DETECTORPL",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("DETECTORPL",))


def serialize_aws_json_1_1(value: Language) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Language:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Language value: {data!r}")
    return cast(Language, data)
