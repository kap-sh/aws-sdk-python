"""Generated from Smithy shape ``com.amazonaws.cloudformation#ResourcesToImport``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.resource_to_import

ResourcesToImport: TypeAlias = list[
    "capo_cloudformation.types.resource_to_import.ResourceToImport"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: ResourcesToImport, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_cloudformation.types.resource_to_import

    for n, item in enumerate(value, 1):
        capo_cloudformation.types.resource_to_import.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> ResourcesToImport:
    import capo_cloudformation.types.resource_to_import

    out: ResourcesToImport = []
    for child in el.findall("member"):
        out.append(
            capo_cloudformation.types.resource_to_import.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: ResourcesToImport, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_cloudformation.types.resource_to_import

    for n, item in enumerate(value, 1):
        capo_cloudformation.types.resource_to_import.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> ResourcesToImport:
    import capo_cloudformation.types.resource_to_import

    out: ResourcesToImport = []
    for child in parent.findall(tag):
        out.append(
            capo_cloudformation.types.resource_to_import.deserialize_query(child)
        )
    return out
