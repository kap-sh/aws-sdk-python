"""Generated from Smithy shape ``com.amazonaws.sagemaker#AthenaResultCompressionType``."""

from typing import Literal, TypeAlias, cast

"""<p>The compression used for Athena query results.</p>"""
AthenaResultCompressionType: TypeAlias = Literal[
    "GZIP",
    "SNAPPY",
    "ZLIB",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AthenaResultCompressionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AthenaResultCompressionType:
    return cast(AthenaResultCompressionType, data)
