"""Generated from Smithy shape ``com.amazonaws.ec2#TagFieldSpecificationListRequest``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.tag_field_specification_request

TagFieldSpecificationListRequest: TypeAlias = list[
    "capo_ec2.types.tag_field_specification_request.TagFieldSpecificationRequest"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TagFieldSpecificationListRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.tag_field_specification_request

        capo_ec2.types.tag_field_specification_request.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> TagFieldSpecificationListRequest:
    import capo_ec2.types.tag_field_specification_request

    out: TagFieldSpecificationListRequest = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.tag_field_specification_request.deserialize_ec2_query(child)
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> TagFieldSpecificationListRequest:
    import capo_ec2.types.tag_field_specification_request

    out: TagFieldSpecificationListRequest = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.tag_field_specification_request.deserialize_ec2_query(child)
        )
    return out
