"""Generated from Smithy shape ``com.amazonaws.cloudformation#ScanFilters``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.scan_filter

ScanFilters: TypeAlias = list["capo_cloudformation.types.scan_filter.ScanFilter"]


# --- awsQuery ser/de ---
def serialize_query(
    value: ScanFilters, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_cloudformation.types.scan_filter

    for n, item in enumerate(value, 1):
        capo_cloudformation.types.scan_filter.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> ScanFilters:
    import capo_cloudformation.types.scan_filter

    out: ScanFilters = []
    for child in el.findall("member"):
        out.append(capo_cloudformation.types.scan_filter.deserialize_query(child))
    return out


def serialize_query_flat(
    value: ScanFilters, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_cloudformation.types.scan_filter

    for n, item in enumerate(value, 1):
        capo_cloudformation.types.scan_filter.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> ScanFilters:
    import capo_cloudformation.types.scan_filter

    out: ScanFilters = []
    for child in parent.findall(tag):
        out.append(capo_cloudformation.types.scan_filter.deserialize_query(child))
    return out
