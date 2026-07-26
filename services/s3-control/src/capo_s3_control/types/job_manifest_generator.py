"""Generated from Smithy shape ``com.amazonaws.s3control#JobManifestGenerator``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_s3_control._protocol.xml import Element, SubElement
from capo_s3_control.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_s3_control.types.s3_job_manifest_generator


class _JobManifestGenerator_S3JobManifestGenerator(TypedDict, closed=True):
    S3JobManifestGenerator: (
        "capo_s3_control.types.s3_job_manifest_generator.S3JobManifestGenerator"
    )


JobManifestGenerator: TypeAlias = _JobManifestGenerator_S3JobManifestGenerator


# --- restXml ser/de ---
def serialize_xml(value: JobManifestGenerator, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "S3JobManifestGenerator" in value:
        import capo_s3_control.types.s3_job_manifest_generator

        capo_s3_control.types.s3_job_manifest_generator.serialize_xml(
            value["S3JobManifestGenerator"], el, "S3JobManifestGenerator"
        )
    else:
        raise SerializationError("JobManifestGenerator: no variant present")


def deserialize_xml(el: Element) -> JobManifestGenerator:
    for child in el:
        if child.tag == "S3JobManifestGenerator":
            import capo_s3_control.types.s3_job_manifest_generator

            return {
                "S3JobManifestGenerator": capo_s3_control.types.s3_job_manifest_generator.deserialize_xml(
                    child
                )
            }
    raise DeserializationError("JobManifestGenerator: no recognized variant element")
