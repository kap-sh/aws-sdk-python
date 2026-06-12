"""Generated from Smithy shape ``com.amazonaws.sagemaker#AthenaResultFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

"""<p>The data storage format for Athena query results.</p>"""
AthenaResultFormat: TypeAlias = Literal[
    "PARQUET",
    "ORC",
    "AVRO",
    "JSON",
    "TEXTFILE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PARQUET",
        "ORC",
        "AVRO",
        "JSON",
        "TEXTFILE",
    )
)


def serialize_aws_json_1_1(value: AthenaResultFormat) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AthenaResultFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AthenaResultFormat value: {data!r}")
    return cast(AthenaResultFormat, data)
