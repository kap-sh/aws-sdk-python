"""Generated from Smithy shape ``com.amazonaws.cloudformation#StartResourceScanOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.resource_scan_id


class StartResourceScanOutput(TypedDict, closed=True):
    resource_scan_id: NotRequired[
        "aws_sdk_cloudformation.types.resource_scan_id.ResourceScanId"
    ]
    """<p>The Amazon Resource Name (ARN) of the resource scan. The format is <code>arn:${Partition}:cloudformation:${Region}:${Account}:resourceScan/${Id}</code>. An example is <code>arn:aws:cloudformation:<i>us-east-1</i>:<i>123456789012</i>:resourceScan/<i>f5b490f7-7ed4-428a-aa06-31ff25db0772</i> </code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: StartResourceScanOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "resource_scan_id" in value:
        pairs.append((f"{prefix}.ResourceScanId", str(value["resource_scan_id"])))


def deserialize_query(el: Element) -> StartResourceScanOutput:
    out: StartResourceScanOutput = {}  # type: ignore[typeddict-item]
    child_resource_scan_id = el.find("ResourceScanId")
    if child_resource_scan_id is not None:
        out["resource_scan_id"] = str(child_resource_scan_id.text or "")
    return out
