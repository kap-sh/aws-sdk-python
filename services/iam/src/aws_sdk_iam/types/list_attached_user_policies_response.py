"""Generated from Smithy shape ``com.amazonaws.iam#ListAttachedUserPoliciesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iam._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_iam.types.attached_policies_list_type
    import aws_sdk_iam.types.boolean_type
    import aws_sdk_iam.types.response_marker_type


class ListAttachedUserPoliciesResponse(TypedDict):
    attached_policies: NotRequired[
        "aws_sdk_iam.types.attached_policies_list_type.attachedPoliciesListType"
    ]
    """<p>A list of the attached policies.</p>"""
    is_truncated: "aws_sdk_iam.types.boolean_type.booleanType"
    """<p>A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent pagination request using the <code>Marker</code> request parameter to retrieve more items. Note that IAM might return fewer than the <code>MaxItems</code> number of results even when there are more results available. We recommend that you check <code>IsTruncated</code> after every call to ensure that you receive all your results.</p>"""
    marker: NotRequired["aws_sdk_iam.types.response_marker_type.responseMarkerType"]
    """<p>When <code>IsTruncated</code> is <code>true</code>, this element is present and contains the value to use for the <code>Marker</code> parameter in a subsequent pagination request.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListAttachedUserPoliciesResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "attached_policies" in value:
        import aws_sdk_iam.types.attached_policies_list_type

        aws_sdk_iam.types.attached_policies_list_type.serialize_query(
            value["attached_policies"], pairs, f"{prefix}.AttachedPolicies"
        )
    pairs.append(
        (
            f"{prefix}.IsTruncated",
            "true" if value.get("is_truncated", False) else "false",
        )
    )
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))


def deserialize_query(el: Element) -> ListAttachedUserPoliciesResponse:
    out: ListAttachedUserPoliciesResponse = {}  # type: ignore[typeddict-item]
    child_attached_policies = el.find("AttachedPolicies")
    if child_attached_policies is not None:
        import aws_sdk_iam.types.attached_policies_list_type

        out["attached_policies"] = (
            aws_sdk_iam.types.attached_policies_list_type.deserialize_query(
                child_attached_policies
            )
        )
    child_is_truncated = el.find("IsTruncated")
    if child_is_truncated is not None:
        out["is_truncated"] = (child_is_truncated.text or "").lower() == "true"
    else:
        out["is_truncated"] = False
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    return out
