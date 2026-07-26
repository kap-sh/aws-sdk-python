"""Generated from Smithy shape ``com.amazonaws.s3control#AccessGrantsList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.list_access_grant_entry

AccessGrantsList: TypeAlias = list[
    "capo_s3_control.types.list_access_grant_entry.ListAccessGrantEntry"
]


# --- restXml ser/de ---
def serialize_xml(value: AccessGrantsList, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import capo_s3_control.types.list_access_grant_entry

        capo_s3_control.types.list_access_grant_entry.serialize_xml(
            item, el, "AccessGrant"
        )


def deserialize_xml(el: Element) -> AccessGrantsList:
    import capo_s3_control.types.list_access_grant_entry

    out: AccessGrantsList = []
    for child in el.findall("AccessGrant"):
        out.append(capo_s3_control.types.list_access_grant_entry.deserialize_xml(child))
    return out


def serialize_xml_flat(value: AccessGrantsList, parent: Element, tag: str) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        import capo_s3_control.types.list_access_grant_entry

        capo_s3_control.types.list_access_grant_entry.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> AccessGrantsList:
    import capo_s3_control.types.list_access_grant_entry

    out: AccessGrantsList = []
    for child in parent.findall(tag):
        out.append(capo_s3_control.types.list_access_grant_entry.deserialize_xml(child))
    return out
