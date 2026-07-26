"""Generated from Smithy shape ``com.amazonaws.cloudformation#PropertyDifferences``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.property_difference

PropertyDifferences: TypeAlias = list[
    "capo_cloudformation.types.property_difference.PropertyDifference"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: PropertyDifferences, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_cloudformation.types.property_difference

    for n, item in enumerate(value, 1):
        capo_cloudformation.types.property_difference.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> PropertyDifferences:
    import capo_cloudformation.types.property_difference

    out: PropertyDifferences = []
    for child in el.findall("member"):
        out.append(
            capo_cloudformation.types.property_difference.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: PropertyDifferences, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_cloudformation.types.property_difference

    for n, item in enumerate(value, 1):
        capo_cloudformation.types.property_difference.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> PropertyDifferences:
    import capo_cloudformation.types.property_difference

    out: PropertyDifferences = []
    for child in parent.findall(tag):
        out.append(
            capo_cloudformation.types.property_difference.deserialize_query(child)
        )
    return out
