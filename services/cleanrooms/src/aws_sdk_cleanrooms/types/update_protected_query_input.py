"""Generated from Smithy shape ``com.amazonaws.cleanrooms#UpdateProtectedQueryInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.membership_identifier
    import aws_sdk_cleanrooms.types.protected_query_identifier
    import aws_sdk_cleanrooms.types.target_protected_query_status


class UpdateProtectedQueryInput(TypedDict):
    membership_identifier: (
        "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier"
    )
    """<p>The identifier for a member of a protected query instance.</p>"""
    protected_query_identifier: (
        "aws_sdk_cleanrooms.types.protected_query_identifier.ProtectedQueryIdentifier"
    )
    """<p>The identifier for a protected query instance.</p>"""
    target_status: "aws_sdk_cleanrooms.types.target_protected_query_status.TargetProtectedQueryStatus"
    """<p>The target status of a query. Used to update the execution status of a currently running query.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateProtectedQueryInput) -> dict:
    out: dict = {}
    out["targetStatus"] = value["target_status"]
    return out


def deserialize_json(data: dict) -> UpdateProtectedQueryInput:
    out: UpdateProtectedQueryInput = {}  # type: ignore[typeddict-item]
    if "targetStatus" in data:
        out["target_status"] = data["targetStatus"]
    else:
        raise DeserializationError("UpdateProtectedQueryInput.target_status required")
    return out
