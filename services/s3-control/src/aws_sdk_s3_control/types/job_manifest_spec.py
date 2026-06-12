"""Generated from Smithy shape ``com.amazonaws.s3control#JobManifestSpec``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3_control._protocol.xml import Element, SubElement
from aws_sdk_s3_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.job_manifest_field_list
    import aws_sdk_s3_control.types.job_manifest_format


class JobManifestSpec(TypedDict):
    format: "aws_sdk_s3_control.types.job_manifest_format.JobManifestFormat"
    """<p>Indicates which of the available formats the specified manifest uses.</p>"""
    fields: NotRequired[
        "aws_sdk_s3_control.types.job_manifest_field_list.JobManifestFieldList"
    ]
    """<p>If the specified manifest object is in the <code>S3BatchOperations_CSV_20180820</code> format, this element describes which columns contain the required data.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: JobManifestSpec, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_s3_control.types.job_manifest_format

    aws_sdk_s3_control.types.job_manifest_format.serialize_xml(
        value["format"], el, "Format"
    )
    if "fields" in value:
        import aws_sdk_s3_control.types.job_manifest_field_list

        aws_sdk_s3_control.types.job_manifest_field_list.serialize_xml(
            value["fields"], el, "Fields"
        )


def deserialize_xml(el: Element) -> JobManifestSpec:
    out: JobManifestSpec = {}  # type: ignore[typeddict-item]
    child_format = el.find("Format")
    if child_format is not None:
        import aws_sdk_s3_control.types.job_manifest_format

        out["format"] = aws_sdk_s3_control.types.job_manifest_format.deserialize_xml(
            child_format
        )
    else:
        raise DeserializationError("JobManifestSpec.format required")
    child_fields = el.find("Fields")
    if child_fields is not None:
        import aws_sdk_s3_control.types.job_manifest_field_list

        out["fields"] = (
            aws_sdk_s3_control.types.job_manifest_field_list.deserialize_xml(
                child_fields
            )
        )
    return out
