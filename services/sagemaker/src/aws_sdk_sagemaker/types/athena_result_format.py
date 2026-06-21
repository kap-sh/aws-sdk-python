"""Generated from Smithy shape ``com.amazonaws.sagemaker#AthenaResultFormat``."""

from typing import Literal, TypeAlias, cast

"""<p>The data storage format for Athena query results.</p>"""
AthenaResultFormat: TypeAlias = Literal[
    "PARQUET",
    "ORC",
    "AVRO",
    "JSON",
    "TEXTFILE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AthenaResultFormat) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AthenaResultFormat:
    return cast(AthenaResultFormat, data)
