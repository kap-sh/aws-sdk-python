"""Generated from Smithy shape ``com.amazonaws.s3control#ScopePermissionList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.scope_permission

ScopePermissionList: TypeAlias = list[
    "aws_sdk_s3_control.types.scope_permission.ScopePermission"
]


# --- restXml ser/de ---
def serialize_xml(value: ScopePermissionList, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import aws_sdk_s3_control.types.scope_permission

        aws_sdk_s3_control.types.scope_permission.serialize_xml(item, el, "Permission")


def deserialize_xml(el: Element) -> ScopePermissionList:
    import aws_sdk_s3_control.types.scope_permission

    out: ScopePermissionList = []
    for child in el.findall("Permission"):
        out.append(aws_sdk_s3_control.types.scope_permission.deserialize_xml(child))
    return out


def serialize_xml_flat(value: ScopePermissionList, parent: Element, tag: str) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        import aws_sdk_s3_control.types.scope_permission

        aws_sdk_s3_control.types.scope_permission.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> ScopePermissionList:
    import aws_sdk_s3_control.types.scope_permission

    out: ScopePermissionList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_s3_control.types.scope_permission.deserialize_xml(child))
    return out
