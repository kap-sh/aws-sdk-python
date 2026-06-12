"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#ICD10CMEntityCategory``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_comprehendmedical.errors import DeserializationError

ICD10CMEntityCategory: TypeAlias = Literal["MEDICAL_CONDITION",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("MEDICAL_CONDITION",))


def serialize_aws_json_1_1(value: ICD10CMEntityCategory) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ICD10CMEntityCategory:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ICD10CMEntityCategory value: {data!r}")
    return cast(ICD10CMEntityCategory, data)
