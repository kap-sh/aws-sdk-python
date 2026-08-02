"""Generated from Smithy shape ``com.amazonaws.iam#GetDelegationRequestResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.delegation_request
    import capo_iam.types.permission_check_result_type
    import capo_iam.types.permission_check_status_type


class GetDelegationRequestResponse(TypedDict, closed=True):
    delegation_request: NotRequired[
        "capo_iam.types.delegation_request.DelegationRequest"
    ]
    """<p>The delegation request object containing all details about the request.</p>"""
    permission_check_status: NotRequired[
        "capo_iam.types.permission_check_status_type.permissionCheckStatusType"
    ]
    """<p>The status of the permission check for the delegation request.</p> <p>This value indicates the status of the process to check whether the caller has sufficient permissions to cover the requested actions in the delegation request. Since this is an asynchronous process, there are three potential values:</p> <ul> <li> <p> <code>IN_PROGRESS</code> : The permission check process has started.</p> </li> <li> <p> <code>COMPLETED</code> : The permission check process has completed. The <code>PermissionCheckResult</code> will include the result.</p> </li> <li> <p> <code>FAILED</code> : The permission check process has failed.</p> </li> </ul>"""
    permission_check_result: NotRequired[
        "capo_iam.types.permission_check_result_type.permissionCheckResultType"
    ]
    """<p>The result of the permission check, indicating whether the caller has sufficient permissions to cover the requested permissions. This is an approximate result.</p> <ul> <li> <p> <code>ALLOWED</code> : The caller has sufficient permissions cover all the requested permissions.</p> </li> <li> <p> <code>DENIED</code> : The caller does not have sufficient permissions to cover all the requested permissions.</p> </li> <li> <p> <code>UNSURE</code> : It is not possible to determine whether the caller has all the permissions needed. This output is most likely for cases when the caller has permissions with conditions.</p> </li> </ul>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetDelegationRequestResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "delegation_request" in value:
        import capo_iam.types.delegation_request

        capo_iam.types.delegation_request.serialize_query(
            value["delegation_request"], pairs, f"{key_prefix}DelegationRequest"
        )
    if "permission_check_status" in value:
        import capo_iam.types.permission_check_status_type

        capo_iam.types.permission_check_status_type.serialize_query(
            value["permission_check_status"],
            pairs,
            f"{key_prefix}PermissionCheckStatus",
        )
    if "permission_check_result" in value:
        import capo_iam.types.permission_check_result_type

        capo_iam.types.permission_check_result_type.serialize_query(
            value["permission_check_result"],
            pairs,
            f"{key_prefix}PermissionCheckResult",
        )


def deserialize_query(el: Element) -> GetDelegationRequestResponse:
    out: GetDelegationRequestResponse = {}  # type: ignore[typeddict-item]
    child_delegation_request = el.find("DelegationRequest")
    if child_delegation_request is not None:
        import capo_iam.types.delegation_request

        out["delegation_request"] = capo_iam.types.delegation_request.deserialize_query(
            child_delegation_request
        )
    child_permission_check_status = el.find("PermissionCheckStatus")
    if child_permission_check_status is not None:
        import capo_iam.types.permission_check_status_type

        out["permission_check_status"] = (
            capo_iam.types.permission_check_status_type.deserialize_query(
                child_permission_check_status
            )
        )
    child_permission_check_result = el.find("PermissionCheckResult")
    if child_permission_check_result is not None:
        import capo_iam.types.permission_check_result_type

        out["permission_check_result"] = (
            capo_iam.types.permission_check_result_type.deserialize_query(
                child_permission_check_result
            )
        )
    return out
