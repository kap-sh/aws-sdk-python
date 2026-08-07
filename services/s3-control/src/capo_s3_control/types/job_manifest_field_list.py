"""Generated from Smithy shape ``com.amazonaws.s3control#JobManifestFieldList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.job_manifest_field_name

JobManifestFieldList: TypeAlias = list[
    "capo_s3_control.types.job_manifest_field_name.JobManifestFieldName"
]


# --- restXml ser/de ---
def serialize_xml(value: JobManifestFieldList, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import capo_s3_control.types.job_manifest_field_name

        capo_s3_control.types.job_manifest_field_name.serialize_xml(item, el, "member")


def deserialize_xml(el: Element) -> JobManifestFieldList:
    import capo_s3_control.types.job_manifest_field_name

    out: JobManifestFieldList = []
    for child in el.findall("member"):
        out.append(capo_s3_control.types.job_manifest_field_name.deserialize_xml(child))
    return out


def serialize_xml_flat(value: JobManifestFieldList, parent: Element, tag: str) -> None:
    """Variant for parents with ``@xmlFlattened`` on the referencing member. Items go directly under ``parent``."""
    for item in value:
        import capo_s3_control.types.job_manifest_field_name

        capo_s3_control.types.job_manifest_field_name.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> JobManifestFieldList:
    import capo_s3_control.types.job_manifest_field_name

    out: JobManifestFieldList = []
    for child in parent.findall(tag):
        out.append(capo_s3_control.types.job_manifest_field_name.deserialize_xml(child))
    return out
