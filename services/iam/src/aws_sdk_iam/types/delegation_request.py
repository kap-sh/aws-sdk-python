"""Generated from Smithy shape ``com.amazonaws.iam#DelegationRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_iam._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_iam.types.account_id_type
    import aws_sdk_iam.types.arn_type
    import aws_sdk_iam.types.boolean_type
    import aws_sdk_iam.types.date_type
    import aws_sdk_iam.types.delegation_permission
    import aws_sdk_iam.types.delegation_request_description_type
    import aws_sdk_iam.types.delegation_request_id_type
    import aws_sdk_iam.types.notes_type
    import aws_sdk_iam.types.owner_id_type
    import aws_sdk_iam.types.permission_type
    import aws_sdk_iam.types.redirect_url_type
    import aws_sdk_iam.types.request_message_type
    import aws_sdk_iam.types.requestor_name_type
    import aws_sdk_iam.types.role_permission_restriction_arn_list_type
    import aws_sdk_iam.types.session_duration_type
    import aws_sdk_iam.types.state_type


class DelegationRequest(TypedDict):
    delegation_request_id: NotRequired[
        "aws_sdk_iam.types.delegation_request_id_type.delegationRequestIdType"
    ]
    """<p>The unique identifier for the delegation request.</p>"""
    owner_account_id: NotRequired["aws_sdk_iam.types.account_id_type.accountIdType"]
    """<p>Amazon Web Services account ID of the owner of the delegation request.</p>"""
    description: NotRequired[
        "aws_sdk_iam.types.delegation_request_description_type.delegationRequestDescriptionType"
    ]
    """<p>Description of the delegation request. This is a message that is provided by the Amazon Web Services partner that filed the delegation request.</p>"""
    request_message: NotRequired[
        "aws_sdk_iam.types.request_message_type.requestMessageType"
    ]
    """<p>A custom message that is added to the delegation request by the partner.</p> <p>This element is different from the <code>Description</code> element such that this is a request specific message injected by the partner. The <code>Description</code> is typically a generic explanation of what the delegation request is targeted to do.</p>"""
    permissions: NotRequired[
        "aws_sdk_iam.types.delegation_permission.DelegationPermission"
    ]
    permission_policy: NotRequired["aws_sdk_iam.types.permission_type.permissionType"]
    """<p>JSON content of the associated permission policy of this delegation request.</p>"""
    role_permission_restriction_arns: NotRequired[
        "aws_sdk_iam.types.role_permission_restriction_arn_list_type.rolePermissionRestrictionArnListType"
    ]
    """<p>If the <code>PermissionPolicy</code> includes role creation permissions, this element will include the list of permissions boundary policies associated with the role creation. See <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html\">Permissions boundaries for IAM entities</a> for more details about IAM permission boundaries. </p>"""
    owner_id: NotRequired["aws_sdk_iam.types.owner_id_type.ownerIdType"]
    """<p>ARN of the owner of this delegation request.</p>"""
    approver_id: NotRequired["aws_sdk_iam.types.arn_type.arnType"]
    state: NotRequired["aws_sdk_iam.types.state_type.stateType"]
    """<p>The state of this delegation request.</p> <p>See the <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/temporary-delegation-building-integration.html#temporary-delegation-request-lifecycle\">Understanding the Request Lifecycle</a> for an explanation of how these states are transitioned. </p>"""
    expiration_time: NotRequired["aws_sdk_iam.types.date_type.dateType"]
    """<p>The expiry time of this delegation request</p> <p>See the <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/temporary-delegation-building-integration.html#temporary-delegation-request-lifecycle\">Understanding the Request Lifecycle</a> for details on the life time of a delegation request at each state.</p>"""
    requestor_id: NotRequired["aws_sdk_iam.types.account_id_type.accountIdType"]
    """<p>Identity of the requestor of this delegation request. This will be an Amazon Web Services account ID.</p>"""
    requestor_name: NotRequired[
        "aws_sdk_iam.types.requestor_name_type.requestorNameType"
    ]
    """<p>A friendly name of the requestor.</p>"""
    create_date: NotRequired["aws_sdk_iam.types.date_type.dateType"]
    """<p>Creation date (timestamp) of this delegation request.</p>"""
    session_duration: NotRequired[
        "aws_sdk_iam.types.session_duration_type.sessionDurationType"
    ]
    """<p>The life-time of the requested session credential.</p>"""
    redirect_url: NotRequired["aws_sdk_iam.types.redirect_url_type.redirectUrlType"]
    """<p>A URL to be redirected to once the delegation request is approved. Partners provide this URL when creating the delegation request.</p>"""
    notes: NotRequired["aws_sdk_iam.types.notes_type.notesType"]
    """<p>Notes added to this delegation request, if this request was updated via the <a href=\"https://docs.aws.amazon.com/IAM/latest/APIReference/API_UpdateDelegationRequest.html\">UpdateDelegationRequest</a> API.</p>"""
    rejection_reason: NotRequired["aws_sdk_iam.types.notes_type.notesType"]
    """<p>Reasons for rejecting this delegation request, if this request was rejected. See also <a href=\"https://docs.aws.amazon.com/IAM/latest/APIReference/API_RejectDelegationRequest.html\">RejectDelegationRequest</a> API documentation. </p>"""
    only_send_by_owner: "aws_sdk_iam.types.boolean_type.booleanType"
    """<p>A flag indicating whether the <a href=\"https://docs.aws.amazon.com/IAM/latest/APIReference/API_SendDelegationToken.html\">SendDelegationToken</a> must be called by the owner of this delegation request. This is set by the requesting partner.</p>"""
    updated_time: NotRequired["aws_sdk_iam.types.date_type.dateType"]
    """<p>Last updated timestamp of the request.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DelegationRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "delegation_request_id" in value:
        pairs.append(
            (f"{prefix}.DelegationRequestId", str(value["delegation_request_id"]))
        )
    if "owner_account_id" in value:
        pairs.append((f"{prefix}.OwnerAccountId", str(value["owner_account_id"])))
    if "description" in value:
        pairs.append((f"{prefix}.Description", str(value["description"])))
    if "request_message" in value:
        pairs.append((f"{prefix}.RequestMessage", str(value["request_message"])))
    if "permissions" in value:
        import aws_sdk_iam.types.delegation_permission

        aws_sdk_iam.types.delegation_permission.serialize_query(
            value["permissions"], pairs, f"{prefix}.Permissions"
        )
    if "permission_policy" in value:
        pairs.append((f"{prefix}.PermissionPolicy", str(value["permission_policy"])))
    if "role_permission_restriction_arns" in value:
        import aws_sdk_iam.types.role_permission_restriction_arn_list_type

        aws_sdk_iam.types.role_permission_restriction_arn_list_type.serialize_query(
            value["role_permission_restriction_arns"],
            pairs,
            f"{prefix}.RolePermissionRestrictionArns",
        )
    if "owner_id" in value:
        pairs.append((f"{prefix}.OwnerId", str(value["owner_id"])))
    if "approver_id" in value:
        pairs.append((f"{prefix}.ApproverId", str(value["approver_id"])))
    if "state" in value:
        import aws_sdk_iam.types.state_type

        aws_sdk_iam.types.state_type.serialize_query(
            value["state"], pairs, f"{prefix}.State"
        )
    if "expiration_time" in value:
        import aws_sdk_iam.types.date_type

        aws_sdk_iam.types.date_type.serialize_query(
            value["expiration_time"], pairs, f"{prefix}.ExpirationTime"
        )
    if "requestor_id" in value:
        pairs.append((f"{prefix}.RequestorId", str(value["requestor_id"])))
    if "requestor_name" in value:
        pairs.append((f"{prefix}.RequestorName", str(value["requestor_name"])))
    if "create_date" in value:
        import aws_sdk_iam.types.date_type

        aws_sdk_iam.types.date_type.serialize_query(
            value["create_date"], pairs, f"{prefix}.CreateDate"
        )
    if "session_duration" in value:
        pairs.append((f"{prefix}.SessionDuration", str(value["session_duration"])))
    if "redirect_url" in value:
        pairs.append((f"{prefix}.RedirectUrl", str(value["redirect_url"])))
    if "notes" in value:
        pairs.append((f"{prefix}.Notes", str(value["notes"])))
    if "rejection_reason" in value:
        pairs.append((f"{prefix}.RejectionReason", str(value["rejection_reason"])))
    pairs.append(
        (
            f"{prefix}.OnlySendByOwner",
            "true" if value.get("only_send_by_owner", False) else "false",
        )
    )
    if "updated_time" in value:
        import aws_sdk_iam.types.date_type

        aws_sdk_iam.types.date_type.serialize_query(
            value["updated_time"], pairs, f"{prefix}.UpdatedTime"
        )


def deserialize_query(el: Element) -> DelegationRequest:
    out: DelegationRequest = {}  # type: ignore[typeddict-item]
    child_delegation_request_id = el.find("DelegationRequestId")
    if child_delegation_request_id is not None:
        out["delegation_request_id"] = str(child_delegation_request_id.text or "")
    child_owner_account_id = el.find("OwnerAccountId")
    if child_owner_account_id is not None:
        out["owner_account_id"] = str(child_owner_account_id.text or "")
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_request_message = el.find("RequestMessage")
    if child_request_message is not None:
        out["request_message"] = str(child_request_message.text or "")
    child_permissions = el.find("Permissions")
    if child_permissions is not None:
        import aws_sdk_iam.types.delegation_permission

        out["permissions"] = aws_sdk_iam.types.delegation_permission.deserialize_query(
            child_permissions
        )
    child_permission_policy = el.find("PermissionPolicy")
    if child_permission_policy is not None:
        out["permission_policy"] = str(child_permission_policy.text or "")
    child_role_permission_restriction_arns = el.find("RolePermissionRestrictionArns")
    if child_role_permission_restriction_arns is not None:
        import aws_sdk_iam.types.role_permission_restriction_arn_list_type

        out["role_permission_restriction_arns"] = (
            aws_sdk_iam.types.role_permission_restriction_arn_list_type.deserialize_query(
                child_role_permission_restriction_arns
            )
        )
    child_owner_id = el.find("OwnerId")
    if child_owner_id is not None:
        out["owner_id"] = str(child_owner_id.text or "")
    child_approver_id = el.find("ApproverId")
    if child_approver_id is not None:
        out["approver_id"] = str(child_approver_id.text or "")
    child_state = el.find("State")
    if child_state is not None:
        import aws_sdk_iam.types.state_type

        out["state"] = aws_sdk_iam.types.state_type.deserialize_query(child_state)
    child_expiration_time = el.find("ExpirationTime")
    if child_expiration_time is not None:
        import aws_sdk_iam.types.date_type

        out["expiration_time"] = aws_sdk_iam.types.date_type.deserialize_query(
            child_expiration_time
        )
    child_requestor_id = el.find("RequestorId")
    if child_requestor_id is not None:
        out["requestor_id"] = str(child_requestor_id.text or "")
    child_requestor_name = el.find("RequestorName")
    if child_requestor_name is not None:
        out["requestor_name"] = str(child_requestor_name.text or "")
    child_create_date = el.find("CreateDate")
    if child_create_date is not None:
        import aws_sdk_iam.types.date_type

        out["create_date"] = aws_sdk_iam.types.date_type.deserialize_query(
            child_create_date
        )
    child_session_duration = el.find("SessionDuration")
    if child_session_duration is not None:
        out["session_duration"] = int(child_session_duration.text or "")
    child_redirect_url = el.find("RedirectUrl")
    if child_redirect_url is not None:
        out["redirect_url"] = str(child_redirect_url.text or "")
    child_notes = el.find("Notes")
    if child_notes is not None:
        out["notes"] = str(child_notes.text or "")
    child_rejection_reason = el.find("RejectionReason")
    if child_rejection_reason is not None:
        out["rejection_reason"] = str(child_rejection_reason.text or "")
    child_only_send_by_owner = el.find("OnlySendByOwner")
    if child_only_send_by_owner is not None:
        out["only_send_by_owner"] = (
            child_only_send_by_owner.text or ""
        ).lower() == "true"
    else:
        out["only_send_by_owner"] = False
    child_updated_time = el.find("UpdatedTime")
    if child_updated_time is not None:
        import aws_sdk_iam.types.date_type

        out["updated_time"] = aws_sdk_iam.types.date_type.deserialize_query(
            child_updated_time
        )
    return out
