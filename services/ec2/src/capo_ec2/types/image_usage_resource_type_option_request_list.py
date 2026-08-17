"""Generated from Smithy shape ``com.amazonaws.ec2#ImageUsageResourceTypeOptionRequestList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.image_usage_resource_type_option_request

ImageUsageResourceTypeOptionRequestList: TypeAlias = list[
    "capo_ec2.types.image_usage_resource_type_option_request.ImageUsageResourceTypeOptionRequest"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ImageUsageResourceTypeOptionRequestList,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.image_usage_resource_type_option_request

        capo_ec2.types.image_usage_resource_type_option_request.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> ImageUsageResourceTypeOptionRequestList:
    import capo_ec2.types.image_usage_resource_type_option_request

    out: ImageUsageResourceTypeOptionRequestList = []
    for child in el.findall("member"):
        out.append(
            capo_ec2.types.image_usage_resource_type_option_request.deserialize_ec2_query(
                child
            )
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> ImageUsageResourceTypeOptionRequestList:
    import capo_ec2.types.image_usage_resource_type_option_request

    out: ImageUsageResourceTypeOptionRequestList = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.image_usage_resource_type_option_request.deserialize_ec2_query(
                child
            )
        )
    return out
