"""Generated from Smithy shape ``com.amazonaws.sagemaker#RedshiftResultFormat``."""

from typing import Literal, TypeAlias, cast

"""<p>The data storage format for Redshift query results.</p>"""
RedshiftResultFormat: TypeAlias = Literal[
    "PARQUET",
    "CSV",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RedshiftResultFormat) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RedshiftResultFormat:
    return cast(RedshiftResultFormat, data)
