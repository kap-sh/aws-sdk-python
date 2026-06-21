"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#FileClassification``."""

from typing import Literal, TypeAlias, cast

FileClassification: TypeAlias = Literal[
    "MODELIZEIT_EXPORT",
    "RVTOOLS_EXPORT",
    "VMWARE_NSX_EXPORT",
    "IMPORT_TEMPLATE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FileClassification) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FileClassification:
    return cast(FileClassification, data)
