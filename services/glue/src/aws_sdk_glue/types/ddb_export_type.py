"""Generated from Smithy shape ``com.amazonaws.glue#DdbExportType``."""

from typing import Literal, TypeAlias, cast

DdbExportType: TypeAlias = Literal[
    "ddb",
    "s3",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DdbExportType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DdbExportType:
    return cast(DdbExportType, data)
