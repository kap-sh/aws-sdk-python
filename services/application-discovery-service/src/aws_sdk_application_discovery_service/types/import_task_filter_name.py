"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#ImportTaskFilterName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_application_discovery_service.errors import DeserializationError

ImportTaskFilterName: TypeAlias = Literal[
    "IMPORT_TASK_ID",
    "STATUS",
    "NAME",
    "FILE_CLASSIFICATION",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IMPORT_TASK_ID",
        "STATUS",
        "NAME",
        "FILE_CLASSIFICATION",
    )
)


def serialize_aws_json_1_1(value: ImportTaskFilterName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ImportTaskFilterName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ImportTaskFilterName value: {data!r}")
    return cast(ImportTaskFilterName, data)
