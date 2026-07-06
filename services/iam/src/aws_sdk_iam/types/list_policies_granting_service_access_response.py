"""Generated from Smithy shape ``com.amazonaws.iam#ListPoliciesGrantingServiceAccessResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iam._protocol.xml import Element
from aws_sdk_iam.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iam.types.boolean_type
    import aws_sdk_iam.types.list_policy_granting_service_access_response_list_type
    import aws_sdk_iam.types.response_marker_type


class ListPoliciesGrantingServiceAccessResponse(TypedDict, closed=True):
    policies_granting_service_access: "aws_sdk_iam.types.list_policy_granting_service_access_response_list_type.listPolicyGrantingServiceAccessResponseListType"
    """<p>A <code>ListPoliciesGrantingServiceAccess</code> object that contains details about the permissions policies attached to the specified identity (user, group, or role).</p>"""
    is_truncated: "aws_sdk_iam.types.boolean_type.booleanType"
    """<p>A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent pagination request using the <code>Marker</code> request parameter to retrieve more items. We recommend that you check <code>IsTruncated</code> after every call to ensure that you receive all your results.</p>"""
    marker: NotRequired["aws_sdk_iam.types.response_marker_type.responseMarkerType"]
    """<p>When <code>IsTruncated</code> is <code>true</code>, this element is present and contains the value to use for the <code>Marker</code> parameter in a subsequent pagination request.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListPoliciesGrantingServiceAccessResponse,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    import aws_sdk_iam.types.list_policy_granting_service_access_response_list_type

    aws_sdk_iam.types.list_policy_granting_service_access_response_list_type.serialize_query(
        value["policies_granting_service_access"],
        pairs,
        f"{prefix}.PoliciesGrantingServiceAccess",
    )
    pairs.append(
        (
            f"{prefix}.IsTruncated",
            "true" if value.get("is_truncated", False) else "false",
        )
    )
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))


def deserialize_query(el: Element) -> ListPoliciesGrantingServiceAccessResponse:
    out: ListPoliciesGrantingServiceAccessResponse = {}  # type: ignore[typeddict-item]
    child_policies_granting_service_access = el.find("PoliciesGrantingServiceAccess")
    if child_policies_granting_service_access is not None:
        import aws_sdk_iam.types.list_policy_granting_service_access_response_list_type

        out["policies_granting_service_access"] = (
            aws_sdk_iam.types.list_policy_granting_service_access_response_list_type.deserialize_query(
                child_policies_granting_service_access
            )
        )
    else:
        raise DeserializationError(
            "ListPoliciesGrantingServiceAccessResponse.policies_granting_service_access required"
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
