"""Generated from Smithy shape ``com.amazonaws.cloudformation#ResourceChangeDetails``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.resource_change_detail

ResourceChangeDetails: TypeAlias = list[
    "capo_cloudformation.types.resource_change_detail.ResourceChangeDetail"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: ResourceChangeDetails, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_cloudformation.types.resource_change_detail

    for n, item in enumerate(value, 1):
        capo_cloudformation.types.resource_change_detail.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> ResourceChangeDetails:
    import capo_cloudformation.types.resource_change_detail

    out: ResourceChangeDetails = []
    for child in el.findall("member"):
        out.append(
            capo_cloudformation.types.resource_change_detail.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: ResourceChangeDetails, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_cloudformation.types.resource_change_detail

    for n, item in enumerate(value, 1):
        capo_cloudformation.types.resource_change_detail.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> ResourceChangeDetails:
    import capo_cloudformation.types.resource_change_detail

    out: ResourceChangeDetails = []
    for child in parent.findall(tag):
        out.append(
            capo_cloudformation.types.resource_change_detail.deserialize_query(child)
        )
    return out
