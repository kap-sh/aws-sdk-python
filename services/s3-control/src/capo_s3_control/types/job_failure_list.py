"""Generated from Smithy shape ``com.amazonaws.s3control#JobFailureList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.job_failure

JobFailureList: TypeAlias = list["capo_s3_control.types.job_failure.JobFailure"]


# --- restXml ser/de ---
def serialize_xml(value: JobFailureList, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import capo_s3_control.types.job_failure

        capo_s3_control.types.job_failure.serialize_xml(item, el, "member")


def deserialize_xml(el: Element) -> JobFailureList:
    import capo_s3_control.types.job_failure

    out: JobFailureList = []
    for child in el.findall("member"):
        out.append(capo_s3_control.types.job_failure.deserialize_xml(child))
    return out


def serialize_xml_flat(value: JobFailureList, parent: Element, tag: str) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        import capo_s3_control.types.job_failure

        capo_s3_control.types.job_failure.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> JobFailureList:
    import capo_s3_control.types.job_failure

    out: JobFailureList = []
    for child in parent.findall(tag):
        out.append(capo_s3_control.types.job_failure.deserialize_xml(child))
    return out
