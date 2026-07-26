"""Generated from Smithy shape ``com.amazonaws.fsx#StorageType``."""

from typing import Literal, TypeAlias, cast

"""<p>Specifies the file system's storage type.</p>"""
StorageType: TypeAlias = Literal[
    "SSD",
    "HDD",
    "INTELLIGENT_TIERING",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StorageType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StorageType:
    return cast(StorageType, data)
