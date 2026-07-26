"""Generated from Smithy shape ``com.amazonaws.s3control#AccessGrantsInstancesList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.list_access_grants_instance_entry

AccessGrantsInstancesList: TypeAlias = list[
    "capo_s3_control.types.list_access_grants_instance_entry.ListAccessGrantsInstanceEntry"
]


# --- restXml ser/de ---
def serialize_xml(value: AccessGrantsInstancesList, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import capo_s3_control.types.list_access_grants_instance_entry

        capo_s3_control.types.list_access_grants_instance_entry.serialize_xml(
            item, el, "AccessGrantsInstance"
        )


def deserialize_xml(el: Element) -> AccessGrantsInstancesList:
    import capo_s3_control.types.list_access_grants_instance_entry

    out: AccessGrantsInstancesList = []
    for child in el.findall("AccessGrantsInstance"):
        out.append(
            capo_s3_control.types.list_access_grants_instance_entry.deserialize_xml(
                child
            )
        )
    return out


def serialize_xml_flat(
    value: AccessGrantsInstancesList, parent: Element, tag: str
) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        import capo_s3_control.types.list_access_grants_instance_entry

        capo_s3_control.types.list_access_grants_instance_entry.serialize_xml(
            item, parent, tag
        )


def deserialize_xml_flat(parent: Element, tag: str) -> AccessGrantsInstancesList:
    import capo_s3_control.types.list_access_grants_instance_entry

    out: AccessGrantsInstancesList = []
    for child in parent.findall(tag):
        out.append(
            capo_s3_control.types.list_access_grants_instance_entry.deserialize_xml(
                child
            )
        )
    return out
