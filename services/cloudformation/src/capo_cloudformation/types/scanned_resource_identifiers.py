"""Generated from Smithy shape ``com.amazonaws.cloudformation#ScannedResourceIdentifiers``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.scanned_resource_identifier

ScannedResourceIdentifiers: TypeAlias = list[
    "capo_cloudformation.types.scanned_resource_identifier.ScannedResourceIdentifier"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: ScannedResourceIdentifiers, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_cloudformation.types.scanned_resource_identifier

    for n, item in enumerate(value, 1):
        capo_cloudformation.types.scanned_resource_identifier.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> ScannedResourceIdentifiers:
    import capo_cloudformation.types.scanned_resource_identifier

    out: ScannedResourceIdentifiers = []
    for child in el.findall("member"):
        out.append(
            capo_cloudformation.types.scanned_resource_identifier.deserialize_query(
                child
            )
        )
    return out


def serialize_query_flat(
    value: ScannedResourceIdentifiers, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_cloudformation.types.scanned_resource_identifier

    for n, item in enumerate(value, 1):
        capo_cloudformation.types.scanned_resource_identifier.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> ScannedResourceIdentifiers:
    import capo_cloudformation.types.scanned_resource_identifier

    out: ScannedResourceIdentifiers = []
    for child in parent.findall(tag):
        out.append(
            capo_cloudformation.types.scanned_resource_identifier.deserialize_query(
                child
            )
        )
    return out
