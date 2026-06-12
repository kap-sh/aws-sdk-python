"""Generated from Smithy shape ``com.amazonaws.s3control#S3GrantList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.s3_grant

S3GrantList: TypeAlias = list["aws_sdk_s3_control.types.s3_grant.S3Grant"]


# --- restXml ser/de ---
def serialize_xml(value: S3GrantList, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import aws_sdk_s3_control.types.s3_grant

        aws_sdk_s3_control.types.s3_grant.serialize_xml(item, el, "member")


def deserialize_xml(el: Element) -> S3GrantList:
    import aws_sdk_s3_control.types.s3_grant

    out: S3GrantList = []
    for child in el.findall("member"):
        out.append(aws_sdk_s3_control.types.s3_grant.deserialize_xml(child))
    return out


def serialize_xml_flat(value: S3GrantList, parent: Element, tag: str) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        import aws_sdk_s3_control.types.s3_grant

        aws_sdk_s3_control.types.s3_grant.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> S3GrantList:
    import aws_sdk_s3_control.types.s3_grant

    out: S3GrantList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_s3_control.types.s3_grant.deserialize_xml(child))
    return out
