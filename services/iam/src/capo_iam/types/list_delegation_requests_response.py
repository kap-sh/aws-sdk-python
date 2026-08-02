"""Generated from Smithy shape ``com.amazonaws.iam#ListDelegationRequestsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.boolean_type
    import capo_iam.types.delegation_requests_list_type
    import capo_iam.types.marker_type


class ListDelegationRequestsResponse(TypedDict, closed=True):
    delegation_requests: NotRequired[
        "capo_iam.types.delegation_requests_list_type.delegationRequestsListType"
    ]
    """<p>A list of delegation requests that match the specified criteria.</p>"""
    marker: NotRequired["capo_iam.types.marker_type.markerType"]
    """<p>When <code>isTruncated</code> is <code>true</code>, this element is present and contains the value to use for the <code>Marker</code> parameter in a subsequent pagination request.</p>"""
    is_truncated: "capo_iam.types.boolean_type.booleanType"
    """<p>A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent pagination request using the <code>Marker</code> request parameter to retrieve more items.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListDelegationRequestsResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "delegation_requests" in value:
        import capo_iam.types.delegation_requests_list_type

        capo_iam.types.delegation_requests_list_type.serialize_query(
            value["delegation_requests"], pairs, f"{key_prefix}DelegationRequests"
        )
    if "marker" in value:
        pairs.append((f"{key_prefix}Marker", str(value["marker"])))
    pairs.append(
        (
            f"{key_prefix}isTruncated",
            "true" if value.get("is_truncated", False) else "false",
        )
    )


def deserialize_query(el: Element) -> ListDelegationRequestsResponse:
    out: ListDelegationRequestsResponse = {}  # type: ignore[typeddict-item]
    child_delegation_requests = el.find("DelegationRequests")
    if child_delegation_requests is not None:
        import capo_iam.types.delegation_requests_list_type

        out["delegation_requests"] = (
            capo_iam.types.delegation_requests_list_type.deserialize_query(
                child_delegation_requests
            )
        )
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_is_truncated = el.find("isTruncated")
    if child_is_truncated is not None:
        out["is_truncated"] = (child_is_truncated.text or "").lower() == "true"
    else:
        out["is_truncated"] = False
    return out
