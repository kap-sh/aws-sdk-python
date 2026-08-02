"""Generated from Smithy shape ``com.amazonaws.iam#GetAccountAuthorizationDetailsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.entity_list_type
    import capo_iam.types.marker_type
    import capo_iam.types.max_items_type


class GetAccountAuthorizationDetailsRequest(TypedDict, closed=True):
    filter: NotRequired["capo_iam.types.entity_list_type.entityListType"]
    """<p>A list of entity types used to filter the results. Only the entities that match the types you specify are included in the output. Use the value <code>LocalManagedPolicy</code> to include customer managed policies.</p> <p>The format for this parameter is a comma-separated (if more than one) list of strings. Each string value in the list must be one of the valid values listed below.</p>"""
    max_items: NotRequired["capo_iam.types.max_items_type.maxItemsType"]
    """<p>Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the <code>IsTruncated</code> response element is <code>true</code>.</p> <p>If you do not include this parameter, the number of items defaults to 100. Note that IAM might return fewer results, even when there are more results available. In that case, the <code>IsTruncated</code> response element returns <code>true</code>, and <code>Marker</code> contains a value to include in the subsequent call that tells the service where to continue from.</p>"""
    marker: NotRequired["capo_iam.types.marker_type.markerType"]
    """<p>Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the <code>Marker</code> element in the response that you received to indicate where the next call should start.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetAccountAuthorizationDetailsRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "filter" in value:
        import capo_iam.types.entity_list_type

        capo_iam.types.entity_list_type.serialize_query(
            value["filter"], pairs, f"{key_prefix}Filter"
        )
    if "max_items" in value:
        pairs.append((f"{key_prefix}MaxItems", str(value["max_items"])))
    if "marker" in value:
        pairs.append((f"{key_prefix}Marker", str(value["marker"])))


def deserialize_query(el: Element) -> GetAccountAuthorizationDetailsRequest:
    out: GetAccountAuthorizationDetailsRequest = {}  # type: ignore[typeddict-item]
    child_filter = el.find("Filter")
    if child_filter is not None:
        import capo_iam.types.entity_list_type

        out["filter"] = capo_iam.types.entity_list_type.deserialize_query(child_filter)
    child_max_items = el.find("MaxItems")
    if child_max_items is not None:
        out["max_items"] = int(child_max_items.text or "")
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    return out
