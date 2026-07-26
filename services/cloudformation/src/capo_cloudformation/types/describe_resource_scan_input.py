"""Generated from Smithy shape ``com.amazonaws.cloudformation#DescribeResourceScanInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.resource_scan_id


class DescribeResourceScanInput(TypedDict, closed=True):
    resource_scan_id: NotRequired[
        "capo_cloudformation.types.resource_scan_id.ResourceScanId"
    ]
    """<p>The Amazon Resource Name (ARN) of the resource scan.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeResourceScanInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "resource_scan_id" in value:
        pairs.append((f"{prefix}.ResourceScanId", str(value["resource_scan_id"])))


def deserialize_query(el: Element) -> DescribeResourceScanInput:
    out: DescribeResourceScanInput = {}  # type: ignore[typeddict-item]
    child_resource_scan_id = el.find("ResourceScanId")
    if child_resource_scan_id is not None:
        out["resource_scan_id"] = str(child_resource_scan_id.text or "")
    return out
