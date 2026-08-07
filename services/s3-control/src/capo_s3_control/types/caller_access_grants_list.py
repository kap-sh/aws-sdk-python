"""Generated from Smithy shape ``com.amazonaws.s3control#CallerAccessGrantsList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.list_caller_access_grants_entry

CallerAccessGrantsList: TypeAlias = list[
    "capo_s3_control.types.list_caller_access_grants_entry.ListCallerAccessGrantsEntry"
]


# --- restXml ser/de ---
def serialize_xml(value: CallerAccessGrantsList, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import capo_s3_control.types.list_caller_access_grants_entry

        capo_s3_control.types.list_caller_access_grants_entry.serialize_xml(
            item, el, "AccessGrant"
        )


def deserialize_xml(el: Element) -> CallerAccessGrantsList:
    import capo_s3_control.types.list_caller_access_grants_entry

    out: CallerAccessGrantsList = []
    for child in el.findall("AccessGrant"):
        out.append(
            capo_s3_control.types.list_caller_access_grants_entry.deserialize_xml(child)
        )
    return out


def serialize_xml_flat(
    value: CallerAccessGrantsList, parent: Element, tag: str
) -> None:
    """Variant for parents with ``@xmlFlattened`` on the referencing member. Items go directly under ``parent``."""
    for item in value:
        import capo_s3_control.types.list_caller_access_grants_entry

        capo_s3_control.types.list_caller_access_grants_entry.serialize_xml(
            item, parent, tag
        )


def deserialize_xml_flat(parent: Element, tag: str) -> CallerAccessGrantsList:
    import capo_s3_control.types.list_caller_access_grants_entry

    out: CallerAccessGrantsList = []
    for child in parent.findall(tag):
        out.append(
            capo_s3_control.types.list_caller_access_grants_entry.deserialize_xml(child)
        )
    return out
