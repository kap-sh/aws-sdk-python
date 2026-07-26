"""Generated from Smithy shape ``com.amazonaws.frauddetector#BatchImportList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_frauddetector.types.batch_import

BatchImportList: TypeAlias = list["capo_frauddetector.types.batch_import.BatchImport"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchImportList) -> list:
    import capo_frauddetector.types.batch_import

    out: list = []
    for item in value:
        out.append(capo_frauddetector.types.batch_import.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> BatchImportList:
    import capo_frauddetector.types.batch_import

    out: BatchImportList = []
    for item in data:
        out.append(capo_frauddetector.types.batch_import.deserialize_aws_json_1_1(item))
    return out
