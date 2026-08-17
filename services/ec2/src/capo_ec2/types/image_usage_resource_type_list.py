"""Generated from Smithy shape ``com.amazonaws.ec2#ImageUsageResourceTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.image_usage_resource_type

ImageUsageResourceTypeList: TypeAlias = list[
    "capo_ec2.types.image_usage_resource_type.ImageUsageResourceType"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ImageUsageResourceTypeList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.image_usage_resource_type

        capo_ec2.types.image_usage_resource_type.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> ImageUsageResourceTypeList:
    import capo_ec2.types.image_usage_resource_type

    out: ImageUsageResourceTypeList = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.image_usage_resource_type.deserialize_ec2_query(child)
        )
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> ImageUsageResourceTypeList:
    import capo_ec2.types.image_usage_resource_type

    out: ImageUsageResourceTypeList = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.image_usage_resource_type.deserialize_ec2_query(child)
        )
    return out
