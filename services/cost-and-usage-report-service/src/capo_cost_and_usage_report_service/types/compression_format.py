"""Generated from Smithy shape ``com.amazonaws.costandusagereportservice#CompressionFormat``."""

from typing import Literal, TypeAlias, cast

"""<p>The compression format that Amazon Web Services uses for the report.</p>"""
CompressionFormat: TypeAlias = Literal[
    "ZIP",
    "GZIP",
    "Parquet",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CompressionFormat) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CompressionFormat:
    return cast(CompressionFormat, data)
