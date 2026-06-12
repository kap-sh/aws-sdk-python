"""Generated from Smithy shape ``com.amazonaws.sagemaker#RedshiftResultFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

"""<p>The data storage format for Redshift query results.</p>"""
RedshiftResultFormat: TypeAlias = Literal[
    "PARQUET",
    "CSV",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PARQUET",
        "CSV",
    )
)


def serialize_aws_json_1_1(value: RedshiftResultFormat) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RedshiftResultFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RedshiftResultFormat value: {data!r}")
    return cast(RedshiftResultFormat, data)
