"""Generated from Smithy shape ``com.amazonaws.s3control#RegionalBucketList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.regional_bucket

RegionalBucketList: TypeAlias = list[
    "capo_s3_control.types.regional_bucket.RegionalBucket"
]


# --- restXml ser/de ---
def serialize_xml(value: RegionalBucketList, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import capo_s3_control.types.regional_bucket

        capo_s3_control.types.regional_bucket.serialize_xml(item, el, "RegionalBucket")


def deserialize_xml(el: Element) -> RegionalBucketList:
    import capo_s3_control.types.regional_bucket

    out: RegionalBucketList = []
    for child in el.findall("RegionalBucket"):
        out.append(capo_s3_control.types.regional_bucket.deserialize_xml(child))
    return out


def serialize_xml_flat(value: RegionalBucketList, parent: Element, tag: str) -> None:
    """Variant for parents with ``@xmlFlattened`` on the referencing member. Items go directly under ``parent``."""
    for item in value:
        import capo_s3_control.types.regional_bucket

        capo_s3_control.types.regional_bucket.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> RegionalBucketList:
    import capo_s3_control.types.regional_bucket

    out: RegionalBucketList = []
    for child in parent.findall(tag):
        out.append(capo_s3_control.types.regional_bucket.deserialize_xml(child))
    return out
