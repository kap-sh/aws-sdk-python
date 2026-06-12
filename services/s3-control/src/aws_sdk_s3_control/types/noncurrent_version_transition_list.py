"""Generated from Smithy shape ``com.amazonaws.s3control#NoncurrentVersionTransitionList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.noncurrent_version_transition

NoncurrentVersionTransitionList: TypeAlias = list[
    "aws_sdk_s3_control.types.noncurrent_version_transition.NoncurrentVersionTransition"
]


# --- restXml ser/de ---
def serialize_xml(
    value: NoncurrentVersionTransitionList, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import aws_sdk_s3_control.types.noncurrent_version_transition

        aws_sdk_s3_control.types.noncurrent_version_transition.serialize_xml(
            item, el, "NoncurrentVersionTransition"
        )


def deserialize_xml(el: Element) -> NoncurrentVersionTransitionList:
    import aws_sdk_s3_control.types.noncurrent_version_transition

    out: NoncurrentVersionTransitionList = []
    for child in el.findall("NoncurrentVersionTransition"):
        out.append(
            aws_sdk_s3_control.types.noncurrent_version_transition.deserialize_xml(
                child
            )
        )
    return out


def serialize_xml_flat(
    value: NoncurrentVersionTransitionList, parent: Element, tag: str
) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        import aws_sdk_s3_control.types.noncurrent_version_transition

        aws_sdk_s3_control.types.noncurrent_version_transition.serialize_xml(
            item, parent, tag
        )


def deserialize_xml_flat(parent: Element, tag: str) -> NoncurrentVersionTransitionList:
    import aws_sdk_s3_control.types.noncurrent_version_transition

    out: NoncurrentVersionTransitionList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_s3_control.types.noncurrent_version_transition.deserialize_xml(
                child
            )
        )
    return out
