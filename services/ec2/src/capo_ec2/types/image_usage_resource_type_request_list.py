"""Generated from Smithy shape ``com.amazonaws.ec2#ImageUsageResourceTypeRequestList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.image_usage_resource_type_request

ImageUsageResourceTypeRequestList: TypeAlias = list[
    "capo_ec2.types.image_usage_resource_type_request.ImageUsageResourceTypeRequest"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ImageUsageResourceTypeRequestList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.image_usage_resource_type_request

        capo_ec2.types.image_usage_resource_type_request.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(
    parent: Element, tag: str
) -> ImageUsageResourceTypeRequestList:
    import capo_ec2.types.image_usage_resource_type_request

    out: ImageUsageResourceTypeRequestList = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.image_usage_resource_type_request.deserialize_ec2_query(
                child
            )
        )
    return out
