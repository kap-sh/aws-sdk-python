"""Generated from Smithy shape ``com.amazonaws.mpa#CreateApprovalTeamRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_mpa.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mpa.types.approval_strategy
    import aws_sdk_mpa.types.approval_team_name
    import aws_sdk_mpa.types.approval_team_request_approvers
    import aws_sdk_mpa.types.description
    import aws_sdk_mpa.types.policies_references
    import aws_sdk_mpa.types.tags
    import aws_sdk_mpa.types.token


class CreateApprovalTeamRequest(TypedDict):
    client_token: NotRequired["aws_sdk_mpa.types.token.Token"]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services populates this field.</p> <note> <p> <b>What is idempotency?</b> </p> <p>When you make a mutating API request, the request typically returns a result before the operation's asynchronous workflows have completed. Operations might also time out or encounter other server issues before they complete, even though the request has already returned a result. This could make it difficult to determine whether the request succeeded or not, and could lead to multiple retries to ensure that the operation completes successfully. However, if the original request and the subsequent retries are successful, the operation is completed multiple times. This means that you might create more resources than you intended.</p> <p> <i>Idempotency</i> ensures that an API request completes no more than one time. With an idempotent request, if the original request completes successfully, any subsequent retries complete successfully without performing any further actions.</p> </note>"""
    approval_strategy: "aws_sdk_mpa.types.approval_strategy.ApprovalStrategy"
    """<p>An <code>ApprovalStrategy</code> object. Contains details for how the team grants approval.</p>"""
    approvers: (
        "aws_sdk_mpa.types.approval_team_request_approvers.ApprovalTeamRequestApprovers"
    )
    """<p>An array of <code>ApprovalTeamRequesterApprovers</code> objects. Contains details for the approvers in the team.</p>"""
    description: "aws_sdk_mpa.types.description.Description"
    """<p>Description for the team.</p>"""
    policies: "aws_sdk_mpa.types.policies_references.PoliciesReferences"
    """<p>An array of <code>PolicyReference</code> objects. Contains a list of policies that define the permissions for team resources.</p>"""
    name: "aws_sdk_mpa.types.approval_team_name.ApprovalTeamName"
    """<p>Name of the team.</p>"""
    tags: NotRequired["aws_sdk_mpa.types.tags.Tags"]
    """<p>Tags you want to attach to the team.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateApprovalTeamRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    import aws_sdk_mpa.types.approval_strategy

    out["ApprovalStrategy"] = aws_sdk_mpa.types.approval_strategy.serialize_json(
        value["approval_strategy"]
    )
    import aws_sdk_mpa.types.approval_team_request_approvers

    out["Approvers"] = aws_sdk_mpa.types.approval_team_request_approvers.serialize_json(
        value["approvers"]
    )
    out["Description"] = value["description"]
    import aws_sdk_mpa.types.policies_references

    out["Policies"] = aws_sdk_mpa.types.policies_references.serialize_json(
        value["policies"]
    )
    out["Name"] = value["name"]
    if "tags" in value:
        import aws_sdk_mpa.types.tags

        out["Tags"] = aws_sdk_mpa.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateApprovalTeamRequest:
    out: CreateApprovalTeamRequest = {}  # type: ignore[typeddict-item]
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    if "ApprovalStrategy" in data:
        import aws_sdk_mpa.types.approval_strategy

        out["approval_strategy"] = aws_sdk_mpa.types.approval_strategy.deserialize_json(
            data["ApprovalStrategy"]
        )
    else:
        raise DeserializationError(
            "CreateApprovalTeamRequest.approval_strategy required"
        )
    if "Approvers" in data:
        import aws_sdk_mpa.types.approval_team_request_approvers

        out["approvers"] = (
            aws_sdk_mpa.types.approval_team_request_approvers.deserialize_json(
                data["Approvers"]
            )
        )
    else:
        raise DeserializationError("CreateApprovalTeamRequest.approvers required")
    if "Description" in data:
        out["description"] = data["Description"]
    else:
        raise DeserializationError("CreateApprovalTeamRequest.description required")
    if "Policies" in data:
        import aws_sdk_mpa.types.policies_references

        out["policies"] = aws_sdk_mpa.types.policies_references.deserialize_json(
            data["Policies"]
        )
    else:
        raise DeserializationError("CreateApprovalTeamRequest.policies required")
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateApprovalTeamRequest.name required")
    if "Tags" in data:
        import aws_sdk_mpa.types.tags

        out["tags"] = aws_sdk_mpa.types.tags.deserialize_json(data["Tags"])
    return out
