"""Generated from Smithy shape ``com.amazonaws.bcmdataexports#ExportReferenceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bcm_data_exports.types.export_reference

ExportReferenceList: TypeAlias = list[
    "capo_bcm_data_exports.types.export_reference.ExportReference"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExportReferenceList) -> list:
    import capo_bcm_data_exports.types.export_reference

    out: list = []
    for item in value:
        out.append(
            capo_bcm_data_exports.types.export_reference.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ExportReferenceList:
    import capo_bcm_data_exports.types.export_reference

    out: ExportReferenceList = []
    for item in data:
        out.append(
            capo_bcm_data_exports.types.export_reference.deserialize_aws_json_1_1(item)
        )
    return out
