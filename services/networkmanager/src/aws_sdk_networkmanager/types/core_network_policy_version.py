"""Generated from Smithy shape ``com.amazonaws.networkmanager#CoreNetworkPolicyVersion``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.change_set_state
    import aws_sdk_networkmanager.types.constrained_string
    import aws_sdk_networkmanager.types.core_network_id
    import aws_sdk_networkmanager.types.core_network_policy_alias
    import aws_sdk_networkmanager.types.date_time
    import aws_sdk_networkmanager.types.integer


class CoreNetworkPolicyVersion(TypedDict, closed=True):
    core_network_id: NotRequired[
        "aws_sdk_networkmanager.types.core_network_id.CoreNetworkId"
    ]
    """<p>The ID of a core network.</p>"""
    policy_version_id: NotRequired["aws_sdk_networkmanager.types.integer.Integer"]
    """<p>The ID of the policy version.</p>"""
    alias: NotRequired[
        "aws_sdk_networkmanager.types.core_network_policy_alias.CoreNetworkPolicyAlias"
    ]
    """<p>Whether a core network policy is the current policy or the most recently submitted policy.</p>"""
    description: NotRequired[
        "aws_sdk_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The description of a core network policy version.</p>"""
    created_at: NotRequired["aws_sdk_networkmanager.types.date_time.DateTime"]
    """<p>The timestamp when a core network policy version was created.</p>"""
    change_set_state: NotRequired[
        "aws_sdk_networkmanager.types.change_set_state.ChangeSetState"
    ]
    """<p>The status of the policy version change set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CoreNetworkPolicyVersion) -> dict:
    out: dict = {}
    if "core_network_id" in value:
        out["CoreNetworkId"] = value["core_network_id"]
    if "policy_version_id" in value:
        out["PolicyVersionId"] = value["policy_version_id"]
    if "alias" in value:
        import aws_sdk_networkmanager.types.core_network_policy_alias

        out["Alias"] = (
            aws_sdk_networkmanager.types.core_network_policy_alias.serialize_json(
                value["alias"]
            )
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "created_at" in value:
        import aws_sdk_networkmanager.types.date_time

        out["CreatedAt"] = aws_sdk_networkmanager.types.date_time.serialize_json(
            value["created_at"]
        )
    if "change_set_state" in value:
        import aws_sdk_networkmanager.types.change_set_state

        out["ChangeSetState"] = (
            aws_sdk_networkmanager.types.change_set_state.serialize_json(
                value["change_set_state"]
            )
        )
    return out


def deserialize_json(data: dict) -> CoreNetworkPolicyVersion:
    out: CoreNetworkPolicyVersion = {}  # type: ignore[typeddict-item]
    if "CoreNetworkId" in data:
        out["core_network_id"] = data["CoreNetworkId"]
    if "PolicyVersionId" in data:
        out["policy_version_id"] = data["PolicyVersionId"]
    if "Alias" in data:
        import aws_sdk_networkmanager.types.core_network_policy_alias

        out["alias"] = (
            aws_sdk_networkmanager.types.core_network_policy_alias.deserialize_json(
                data["Alias"]
            )
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "CreatedAt" in data:
        import aws_sdk_networkmanager.types.date_time

        out["created_at"] = aws_sdk_networkmanager.types.date_time.deserialize_json(
            data["CreatedAt"]
        )
    if "ChangeSetState" in data:
        import aws_sdk_networkmanager.types.change_set_state

        out["change_set_state"] = (
            aws_sdk_networkmanager.types.change_set_state.deserialize_json(
                data["ChangeSetState"]
            )
        )
    return out
