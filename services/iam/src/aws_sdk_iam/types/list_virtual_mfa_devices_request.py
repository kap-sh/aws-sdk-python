"""Generated from Smithy shape ``com.amazonaws.iam#ListVirtualMFADevicesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iam._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_iam.types.assignment_status_type
    import aws_sdk_iam.types.marker_type
    import aws_sdk_iam.types.max_items_type


class ListVirtualMFADevicesRequest(TypedDict, closed=True):
    assignment_status: NotRequired[
        "aws_sdk_iam.types.assignment_status_type.assignmentStatusType"
    ]
    """<p> The status (<code>Unassigned</code> or <code>Assigned</code>) of the devices to list. If you do not specify an <code>AssignmentStatus</code>, the operation defaults to <code>Any</code>, which lists both assigned and unassigned virtual MFA devices.,</p>"""
    marker: NotRequired["aws_sdk_iam.types.marker_type.markerType"]
    """<p>Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the <code>Marker</code> element in the response that you received to indicate where the next call should start.</p>"""
    max_items: NotRequired["aws_sdk_iam.types.max_items_type.maxItemsType"]
    """<p>Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the <code>IsTruncated</code> response element is <code>true</code>.</p> <p>If you do not include this parameter, the number of items defaults to 100. Note that IAM might return fewer results, even when there are more results available. In that case, the <code>IsTruncated</code> response element returns <code>true</code>, and <code>Marker</code> contains a value to include in the subsequent call that tells the service where to continue from.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListVirtualMFADevicesRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "assignment_status" in value:
        import aws_sdk_iam.types.assignment_status_type

        aws_sdk_iam.types.assignment_status_type.serialize_query(
            value["assignment_status"], pairs, f"{prefix}.AssignmentStatus"
        )
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))
    if "max_items" in value:
        pairs.append((f"{prefix}.MaxItems", str(value["max_items"])))


def deserialize_query(el: Element) -> ListVirtualMFADevicesRequest:
    out: ListVirtualMFADevicesRequest = {}  # type: ignore[typeddict-item]
    child_assignment_status = el.find("AssignmentStatus")
    if child_assignment_status is not None:
        import aws_sdk_iam.types.assignment_status_type

        out["assignment_status"] = (
            aws_sdk_iam.types.assignment_status_type.deserialize_query(
                child_assignment_status
            )
        )
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_max_items = el.find("MaxItems")
    if child_max_items is not None:
        out["max_items"] = int(child_max_items.text or "")
    return out
