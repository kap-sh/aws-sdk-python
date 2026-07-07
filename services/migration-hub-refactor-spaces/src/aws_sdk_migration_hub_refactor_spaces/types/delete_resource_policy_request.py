"""Generated from Smithy shape ``com.amazonaws.migrationhubrefactorspaces#DeleteResourcePolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_migration_hub_refactor_spaces.types.resource_policy_identifier


class DeleteResourcePolicyRequest(TypedDict, closed=True):
    identifier: "aws_sdk_migration_hub_refactor_spaces.types.resource_policy_identifier.ResourcePolicyIdentifier"
    """<p>Amazon Resource Name (ARN) of the resource associated with the policy. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteResourcePolicyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteResourcePolicyRequest:
    out: DeleteResourcePolicyRequest = {}  # type: ignore[typeddict-item]
    return out
