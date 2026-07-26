"""Generated from Smithy shape ``com.amazonaws.networkmanager#CoreNetworkPolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.change_set_state
    import capo_networkmanager.types.constrained_string
    import capo_networkmanager.types.core_network_id
    import capo_networkmanager.types.core_network_policy_alias
    import capo_networkmanager.types.core_network_policy_error_list
    import capo_networkmanager.types.date_time
    import capo_networkmanager.types.integer
    import capo_networkmanager.types.synthesized_json_core_network_policy_document


class CoreNetworkPolicy(TypedDict, closed=True):
    core_network_id: NotRequired[
        "capo_networkmanager.types.core_network_id.CoreNetworkId"
    ]
    """<p>The ID of a core network.</p>"""
    policy_version_id: NotRequired["capo_networkmanager.types.integer.Integer"]
    """<p>The ID of the policy version.</p>"""
    alias: NotRequired[
        "capo_networkmanager.types.core_network_policy_alias.CoreNetworkPolicyAlias"
    ]
    """<p>Whether a core network policy is the current LIVE policy or the most recently submitted policy.</p>"""
    description: NotRequired[
        "capo_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The description of a core network policy.</p>"""
    created_at: NotRequired["capo_networkmanager.types.date_time.DateTime"]
    """<p>The timestamp when a core network policy was created.</p>"""
    change_set_state: NotRequired[
        "capo_networkmanager.types.change_set_state.ChangeSetState"
    ]
    """<p>The state of a core network policy.</p>"""
    policy_errors: NotRequired[
        "capo_networkmanager.types.core_network_policy_error_list.CoreNetworkPolicyErrorList"
    ]
    """<p>Describes any errors in a core network policy.</p>"""
    policy_document: NotRequired[
        "capo_networkmanager.types.synthesized_json_core_network_policy_document.SynthesizedJsonCoreNetworkPolicyDocument"
    ]
    """<p>Describes a core network policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CoreNetworkPolicy) -> dict:
    out: dict = {}
    if "core_network_id" in value:
        out["CoreNetworkId"] = value["core_network_id"]
    if "policy_version_id" in value:
        out["PolicyVersionId"] = value["policy_version_id"]
    if "alias" in value:
        import capo_networkmanager.types.core_network_policy_alias

        out["Alias"] = (
            capo_networkmanager.types.core_network_policy_alias.serialize_json(
                value["alias"]
            )
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "created_at" in value:
        import capo_networkmanager.types.date_time

        out["CreatedAt"] = capo_networkmanager.types.date_time.serialize_json(
            value["created_at"]
        )
    if "change_set_state" in value:
        import capo_networkmanager.types.change_set_state

        out["ChangeSetState"] = (
            capo_networkmanager.types.change_set_state.serialize_json(
                value["change_set_state"]
            )
        )
    if "policy_errors" in value:
        import capo_networkmanager.types.core_network_policy_error_list

        out["PolicyErrors"] = (
            capo_networkmanager.types.core_network_policy_error_list.serialize_json(
                value["policy_errors"]
            )
        )
    if "policy_document" in value:
        out["PolicyDocument"] = value["policy_document"]
    return out


def deserialize_json(data: dict) -> CoreNetworkPolicy:
    out: CoreNetworkPolicy = {}  # type: ignore[typeddict-item]
    if "CoreNetworkId" in data:
        out["core_network_id"] = data["CoreNetworkId"]
    if "PolicyVersionId" in data:
        out["policy_version_id"] = data["PolicyVersionId"]
    if "Alias" in data:
        import capo_networkmanager.types.core_network_policy_alias

        out["alias"] = (
            capo_networkmanager.types.core_network_policy_alias.deserialize_json(
                data["Alias"]
            )
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "CreatedAt" in data:
        import capo_networkmanager.types.date_time

        out["created_at"] = capo_networkmanager.types.date_time.deserialize_json(
            data["CreatedAt"]
        )
    if "ChangeSetState" in data:
        import capo_networkmanager.types.change_set_state

        out["change_set_state"] = (
            capo_networkmanager.types.change_set_state.deserialize_json(
                data["ChangeSetState"]
            )
        )
    if "PolicyErrors" in data:
        import capo_networkmanager.types.core_network_policy_error_list

        out["policy_errors"] = (
            capo_networkmanager.types.core_network_policy_error_list.deserialize_json(
                data["PolicyErrors"]
            )
        )
    if "PolicyDocument" in data:
        out["policy_document"] = data["PolicyDocument"]
    return out
