"""Generated from Smithy shape ``com.amazonaws.bcmdataexports#ExportReferenceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bcm_data_exports.types.export_reference

ExportReferenceList: TypeAlias = list[
    "aws_sdk_bcm_data_exports.types.export_reference.ExportReference"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExportReferenceList) -> list:
    import aws_sdk_bcm_data_exports.types.export_reference

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bcm_data_exports.types.export_reference.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ExportReferenceList:
    import aws_sdk_bcm_data_exports.types.export_reference

    out: ExportReferenceList = []
    for item in data:
        out.append(
            aws_sdk_bcm_data_exports.types.export_reference.deserialize_aws_json_1_1(
                item
            )
        )
    return out
