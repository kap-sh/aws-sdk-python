"""Generated from Smithy shape ``com.amazonaws.s3control#AccessGrantsLocationsList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.list_access_grants_locations_entry

AccessGrantsLocationsList: TypeAlias = list[
    "capo_s3_control.types.list_access_grants_locations_entry.ListAccessGrantsLocationsEntry"
]


# --- restXml ser/de ---
def serialize_xml(value: AccessGrantsLocationsList, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import capo_s3_control.types.list_access_grants_locations_entry

        capo_s3_control.types.list_access_grants_locations_entry.serialize_xml(
            item, el, "AccessGrantsLocation"
        )


def deserialize_xml(el: Element) -> AccessGrantsLocationsList:
    import capo_s3_control.types.list_access_grants_locations_entry

    out: AccessGrantsLocationsList = []
    for child in el.findall("AccessGrantsLocation"):
        out.append(
            capo_s3_control.types.list_access_grants_locations_entry.deserialize_xml(
                child
            )
        )
    return out


def serialize_xml_flat(
    value: AccessGrantsLocationsList, parent: Element, tag: str
) -> None:
    """Variant for parents with ``@xmlFlattened`` on the referencing member. Items go directly under ``parent``."""
    for item in value:
        import capo_s3_control.types.list_access_grants_locations_entry

        capo_s3_control.types.list_access_grants_locations_entry.serialize_xml(
            item, parent, tag
        )


def deserialize_xml_flat(parent: Element, tag: str) -> AccessGrantsLocationsList:
    import capo_s3_control.types.list_access_grants_locations_entry

    out: AccessGrantsLocationsList = []
    for child in parent.findall(tag):
        out.append(
            capo_s3_control.types.list_access_grants_locations_entry.deserialize_xml(
                child
            )
        )
    return out
