"""Generated from Smithy shape ``com.amazonaws.migrationhubrefactorspaces#GetResourcePolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_migration_hub_refactor_spaces.types.resource_policy_identifier


class GetResourcePolicyRequest(TypedDict):
    identifier: "aws_sdk_migration_hub_refactor_spaces.types.resource_policy_identifier.ResourcePolicyIdentifier"
    """<p>The Amazon Resource Name (ARN) of the resource associated with the policy. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetResourcePolicyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetResourcePolicyRequest:
    out: GetResourcePolicyRequest = {}  # type: ignore[typeddict-item]
    return out
