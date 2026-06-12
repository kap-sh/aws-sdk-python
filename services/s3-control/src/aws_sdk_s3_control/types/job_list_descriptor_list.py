"""Generated from Smithy shape ``com.amazonaws.s3control#JobListDescriptorList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.job_list_descriptor

JobListDescriptorList: TypeAlias = list[
    "aws_sdk_s3_control.types.job_list_descriptor.JobListDescriptor"
]


# --- restXml ser/de ---
def serialize_xml(value: JobListDescriptorList, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import aws_sdk_s3_control.types.job_list_descriptor

        aws_sdk_s3_control.types.job_list_descriptor.serialize_xml(item, el, "member")


def deserialize_xml(el: Element) -> JobListDescriptorList:
    import aws_sdk_s3_control.types.job_list_descriptor

    out: JobListDescriptorList = []
    for child in el.findall("member"):
        out.append(aws_sdk_s3_control.types.job_list_descriptor.deserialize_xml(child))
    return out


def serialize_xml_flat(value: JobListDescriptorList, parent: Element, tag: str) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        import aws_sdk_s3_control.types.job_list_descriptor

        aws_sdk_s3_control.types.job_list_descriptor.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> JobListDescriptorList:
    import aws_sdk_s3_control.types.job_list_descriptor

    out: JobListDescriptorList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_s3_control.types.job_list_descriptor.deserialize_xml(child))
    return out
