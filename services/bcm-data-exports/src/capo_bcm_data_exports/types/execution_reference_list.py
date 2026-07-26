"""Generated from Smithy shape ``com.amazonaws.bcmdataexports#ExecutionReferenceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bcm_data_exports.types.execution_reference

ExecutionReferenceList: TypeAlias = list[
    "capo_bcm_data_exports.types.execution_reference.ExecutionReference"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExecutionReferenceList) -> list:
    import capo_bcm_data_exports.types.execution_reference

    out: list = []
    for item in value:
        out.append(
            capo_bcm_data_exports.types.execution_reference.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ExecutionReferenceList:
    import capo_bcm_data_exports.types.execution_reference

    out: ExecutionReferenceList = []
    for item in data:
        out.append(
            capo_bcm_data_exports.types.execution_reference.deserialize_aws_json_1_1(
                item
            )
        )
    return out
