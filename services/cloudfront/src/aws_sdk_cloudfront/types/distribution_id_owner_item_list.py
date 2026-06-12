"""Generated from Smithy shape ``com.amazonaws.cloudfront#DistributionIdOwnerItemList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.distribution_id_owner

DistributionIdOwnerItemList: TypeAlias = list[
    "aws_sdk_cloudfront.types.distribution_id_owner.DistributionIdOwner"
]


# --- restXml ser/de ---
def serialize_xml(
    value: DistributionIdOwnerItemList, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import aws_sdk_cloudfront.types.distribution_id_owner

        aws_sdk_cloudfront.types.distribution_id_owner.serialize_xml(
            item, el, "DistributionIdOwner"
        )


def deserialize_xml(el: Element) -> DistributionIdOwnerItemList:
    import aws_sdk_cloudfront.types.distribution_id_owner

    out: DistributionIdOwnerItemList = []
    for child in el.findall("DistributionIdOwner"):
        out.append(
            aws_sdk_cloudfront.types.distribution_id_owner.deserialize_xml(child)
        )
    return out


def serialize_xml_flat(
    value: DistributionIdOwnerItemList, parent: Element, tag: str
) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        import aws_sdk_cloudfront.types.distribution_id_owner

        aws_sdk_cloudfront.types.distribution_id_owner.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> DistributionIdOwnerItemList:
    import aws_sdk_cloudfront.types.distribution_id_owner

    out: DistributionIdOwnerItemList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_cloudfront.types.distribution_id_owner.deserialize_xml(child)
        )
    return out
