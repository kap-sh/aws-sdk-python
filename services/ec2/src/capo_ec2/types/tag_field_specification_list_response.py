"""Generated from Smithy shape ``com.amazonaws.ec2#TagFieldSpecificationListResponse``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.tag_field_specification_response

TagFieldSpecificationListResponse: TypeAlias = list[
    "capo_ec2.types.tag_field_specification_response.TagFieldSpecificationResponse"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TagFieldSpecificationListResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.tag_field_specification_response

        capo_ec2.types.tag_field_specification_response.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> TagFieldSpecificationListResponse:
    import capo_ec2.types.tag_field_specification_response

    out: TagFieldSpecificationListResponse = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.tag_field_specification_response.deserialize_ec2_query(child)
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> TagFieldSpecificationListResponse:
    import capo_ec2.types.tag_field_specification_response

    out: TagFieldSpecificationListResponse = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.tag_field_specification_response.deserialize_ec2_query(child)
        )
    return out
