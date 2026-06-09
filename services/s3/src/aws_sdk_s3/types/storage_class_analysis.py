"""Generated from Smithy shape ``com.amazonaws.s3#StorageClassAnalysis``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3.types.storage_class_analysis_data_export


class StorageClassAnalysis(TypedDict):
    data_export: NotRequired[
        "aws_sdk_s3.types.storage_class_analysis_data_export.StorageClassAnalysisDataExport"
    ]
    """<p>Specifies how data related to the storage class analysis for an Amazon S3 bucket should be exported.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: StorageClassAnalysis, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "data_export" in value:
        import aws_sdk_s3.types.storage_class_analysis_data_export

        aws_sdk_s3.types.storage_class_analysis_data_export.serialize_xml(
            value["data_export"], el, "DataExport"
        )


def deserialize_xml(el: Element) -> StorageClassAnalysis:
    out: StorageClassAnalysis = {}  # type: ignore[typeddict-item]
    child_data_export = el.find("DataExport")
    if child_data_export is not None:
        import aws_sdk_s3.types.storage_class_analysis_data_export

        out["data_export"] = (
            aws_sdk_s3.types.storage_class_analysis_data_export.deserialize_xml(
                child_data_export
            )
        )
    return out
