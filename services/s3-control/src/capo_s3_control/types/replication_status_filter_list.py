"""Generated from Smithy shape ``com.amazonaws.s3control#ReplicationStatusFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.replication_status

ReplicationStatusFilterList: TypeAlias = list[
    "capo_s3_control.types.replication_status.ReplicationStatus"
]


# --- restXml ser/de ---
def serialize_xml(
    value: ReplicationStatusFilterList, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import capo_s3_control.types.replication_status

        capo_s3_control.types.replication_status.serialize_xml(item, el, "member")


def deserialize_xml(el: Element) -> ReplicationStatusFilterList:
    import capo_s3_control.types.replication_status

    out: ReplicationStatusFilterList = []
    for child in el.findall("member"):
        out.append(capo_s3_control.types.replication_status.deserialize_xml(child))
    return out


def serialize_xml_flat(
    value: ReplicationStatusFilterList, parent: Element, tag: str
) -> None:
    """Variant for parents with ``@xmlFlattened`` on the referencing member. Items go directly under ``parent``."""
    for item in value:
        import capo_s3_control.types.replication_status

        capo_s3_control.types.replication_status.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> ReplicationStatusFilterList:
    import capo_s3_control.types.replication_status

    out: ReplicationStatusFilterList = []
    for child in parent.findall(tag):
        out.append(capo_s3_control.types.replication_status.deserialize_xml(child))
    return out
