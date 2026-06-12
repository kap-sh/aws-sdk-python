"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#ICD10CMEntityType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_comprehendmedical.errors import DeserializationError

ICD10CMEntityType: TypeAlias = Literal[
    "DX_NAME",
    "TIME_EXPRESSION",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DX_NAME",
        "TIME_EXPRESSION",
    )
)


def serialize_aws_json_1_1(value: ICD10CMEntityType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ICD10CMEntityType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ICD10CMEntityType value: {data!r}")
    return cast(ICD10CMEntityType, data)
