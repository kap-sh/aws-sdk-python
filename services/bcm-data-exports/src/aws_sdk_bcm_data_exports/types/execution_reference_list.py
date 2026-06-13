"""Generated from Smithy shape ``com.amazonaws.bcmdataexports#ExecutionReferenceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bcm_data_exports.types.execution_reference

ExecutionReferenceList: TypeAlias = list[
    "aws_sdk_bcm_data_exports.types.execution_reference.ExecutionReference"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExecutionReferenceList) -> list:
    import aws_sdk_bcm_data_exports.types.execution_reference

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bcm_data_exports.types.execution_reference.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ExecutionReferenceList:
    import aws_sdk_bcm_data_exports.types.execution_reference

    out: ExecutionReferenceList = []
    for item in data:
        out.append(
            aws_sdk_bcm_data_exports.types.execution_reference.deserialize_aws_json_1_1(
                item
            )
        )
    return out
