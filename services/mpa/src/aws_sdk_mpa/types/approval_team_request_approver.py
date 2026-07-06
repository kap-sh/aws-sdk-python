"""Generated from Smithy shape ``com.amazonaws.mpa#ApprovalTeamRequestApprover``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_mpa.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mpa.types.identity_id
    import aws_sdk_mpa.types.string


class ApprovalTeamRequestApprover(TypedDict, closed=True):
    primary_identity_id: "aws_sdk_mpa.types.identity_id.IdentityId"
    """<p>ID for the user.</p>"""
    primary_identity_source_arn: "aws_sdk_mpa.types.string.String"
    """<p>Amazon Resource Name (ARN) for the identity source. The identity source manages the user authentication for approvers.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ApprovalTeamRequestApprover) -> dict:
    out: dict = {}
    out["PrimaryIdentityId"] = value["primary_identity_id"]
    out["PrimaryIdentitySourceArn"] = value["primary_identity_source_arn"]
    return out


def deserialize_json(data: dict) -> ApprovalTeamRequestApprover:
    out: ApprovalTeamRequestApprover = {}  # type: ignore[typeddict-item]
    if "PrimaryIdentityId" in data:
        out["primary_identity_id"] = data["PrimaryIdentityId"]
    else:
        raise DeserializationError(
            "ApprovalTeamRequestApprover.primary_identity_id required"
        )
    if "PrimaryIdentitySourceArn" in data:
        out["primary_identity_source_arn"] = data["PrimaryIdentitySourceArn"]
    else:
        raise DeserializationError(
            "ApprovalTeamRequestApprover.primary_identity_source_arn required"
        )
    return out
