"""Generated from Smithy shape ``com.amazonaws.costandusagereportservice#CompressionFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cost_and_usage_report_service.errors import DeserializationError

"""<p>The compression format that Amazon Web Services uses for the report.</p>"""
CompressionFormat: TypeAlias = Literal[
    "ZIP",
    "GZIP",
    "Parquet",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ZIP",
        "GZIP",
        "Parquet",
    )
)


def serialize_aws_json_1_1(value: CompressionFormat) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CompressionFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CompressionFormat value: {data!r}")
    return cast(CompressionFormat, data)
