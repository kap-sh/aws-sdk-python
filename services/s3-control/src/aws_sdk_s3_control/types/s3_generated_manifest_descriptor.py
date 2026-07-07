"""Generated from Smithy shape ``com.amazonaws.s3control#S3GeneratedManifestDescriptor``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.generated_manifest_format
    import aws_sdk_s3_control.types.job_manifest_location


class S3GeneratedManifestDescriptor(TypedDict, closed=True):
    format: NotRequired[
        "aws_sdk_s3_control.types.generated_manifest_format.GeneratedManifestFormat"
    ]
    """<p>The format of the generated manifest.</p>"""
    location: NotRequired[
        "aws_sdk_s3_control.types.job_manifest_location.JobManifestLocation"
    ]


# --- restXml ser/de ---
def serialize_xml(
    value: S3GeneratedManifestDescriptor, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "format" in value:
        import aws_sdk_s3_control.types.generated_manifest_format

        aws_sdk_s3_control.types.generated_manifest_format.serialize_xml(
            value["format"], el, "Format"
        )
    if "location" in value:
        import aws_sdk_s3_control.types.job_manifest_location

        aws_sdk_s3_control.types.job_manifest_location.serialize_xml(
            value["location"], el, "Location"
        )


def deserialize_xml(el: Element) -> S3GeneratedManifestDescriptor:
    out: S3GeneratedManifestDescriptor = {}  # type: ignore[typeddict-item]
    child_format = el.find("Format")
    if child_format is not None:
        import aws_sdk_s3_control.types.generated_manifest_format

        out["format"] = (
            aws_sdk_s3_control.types.generated_manifest_format.deserialize_xml(
                child_format
            )
        )
    child_location = el.find("Location")
    if child_location is not None:
        import aws_sdk_s3_control.types.job_manifest_location

        out["location"] = (
            aws_sdk_s3_control.types.job_manifest_location.deserialize_xml(
                child_location
            )
        )
    return out
