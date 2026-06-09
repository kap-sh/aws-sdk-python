"""Generated from Smithy shape ``com.amazonaws.iam#ListDelegationRequestsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iam._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_iam.types.marker_type
    import aws_sdk_iam.types.max_items_type
    import aws_sdk_iam.types.owner_id_type


class ListDelegationRequestsRequest(TypedDict):
    owner_id: NotRequired["aws_sdk_iam.types.owner_id_type.ownerIdType"]
    """<p>The owner ID to filter delegation requests by.</p>"""
    marker: NotRequired["aws_sdk_iam.types.marker_type.markerType"]
    """<p>Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the <code>Marker</code> element in the response that you received to indicate where the next call should start. </p>"""
    max_items: NotRequired["aws_sdk_iam.types.max_items_type.maxItemsType"]
    """<p>Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the <code>IsTruncated</code> response element is <code>true</code>. </p> <p>If you do not include this parameter, the number of items defaults to 100. Note that IAM may return fewer results, even when there are more results available. In that case, the <code>IsTruncated</code> response element returns <code>true</code>, and <code>Marker</code> contains a value to include in the subsequent call that tells the service where to continue from. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListDelegationRequestsRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "owner_id" in value:
        pairs.append((f"{prefix}.OwnerId", str(value["owner_id"])))
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))
    if "max_items" in value:
        pairs.append((f"{prefix}.MaxItems", str(value["max_items"])))


def deserialize_query(el: Element) -> ListDelegationRequestsRequest:
    out: ListDelegationRequestsRequest = {}  # type: ignore[typeddict-item]
    child_owner_id = el.find("OwnerId")
    if child_owner_id is not None:
        out["owner_id"] = str(child_owner_id.text or "")
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_max_items = el.find("MaxItems")
    if child_max_items is not None:
        out["max_items"] = int(child_max_items.text or "")
    return out
