"""Generated from Smithy shape ``com.amazonaws.s3#StorageClassAnalysisDataExport``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_s3._protocol.xml import Element, SubElement
from aws_sdk_s3.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_s3.types.analytics_export_destination
    import aws_sdk_s3.types.storage_class_analysis_schema_version


class StorageClassAnalysisDataExport(TypedDict, closed=True):
    output_schema_version: "aws_sdk_s3.types.storage_class_analysis_schema_version.StorageClassAnalysisSchemaVersion"
    """<p>The version of the output schema to use when exporting data. Must be <code>V_1</code>.</p>"""
    destination: (
        "aws_sdk_s3.types.analytics_export_destination.AnalyticsExportDestination"
    )
    """<p>The place to store the data for an analysis.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: StorageClassAnalysisDataExport, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_s3.types.storage_class_analysis_schema_version

    aws_sdk_s3.types.storage_class_analysis_schema_version.serialize_xml(
        value["output_schema_version"], el, "OutputSchemaVersion"
    )
    import aws_sdk_s3.types.analytics_export_destination

    aws_sdk_s3.types.analytics_export_destination.serialize_xml(
        value["destination"], el, "Destination"
    )


def deserialize_xml(el: Element) -> StorageClassAnalysisDataExport:
    out: StorageClassAnalysisDataExport = {}  # type: ignore[typeddict-item]
    child_output_schema_version = el.find("OutputSchemaVersion")
    if child_output_schema_version is not None:
        import aws_sdk_s3.types.storage_class_analysis_schema_version

        out["output_schema_version"] = (
            aws_sdk_s3.types.storage_class_analysis_schema_version.deserialize_xml(
                child_output_schema_version
            )
        )
    else:
        raise DeserializationError(
            "StorageClassAnalysisDataExport.output_schema_version required"
        )
    child_destination = el.find("Destination")
    if child_destination is not None:
        import aws_sdk_s3.types.analytics_export_destination

        out["destination"] = (
            aws_sdk_s3.types.analytics_export_destination.deserialize_xml(
                child_destination
            )
        )
    else:
        raise DeserializationError(
            "StorageClassAnalysisDataExport.destination required"
        )
    return out
