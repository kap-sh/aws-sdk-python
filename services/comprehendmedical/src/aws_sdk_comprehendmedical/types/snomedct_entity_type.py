"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#SNOMEDCTEntityType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_comprehendmedical.errors import DeserializationError

SNOMEDCTEntityType: TypeAlias = Literal[
    "DX_NAME",
    "TEST_NAME",
    "PROCEDURE_NAME",
    "TREATMENT_NAME",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DX_NAME",
        "TEST_NAME",
        "PROCEDURE_NAME",
        "TREATMENT_NAME",
    )
)


def serialize_aws_json_1_1(value: SNOMEDCTEntityType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SNOMEDCTEntityType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SNOMEDCTEntityType value: {data!r}")
    return cast(SNOMEDCTEntityType, data)
