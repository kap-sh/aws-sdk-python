"""Generated from Smithy shape ``com.amazonaws.networkmanager#CoreNetworkChange``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.change_action
    import capo_networkmanager.types.change_type
    import capo_networkmanager.types.constrained_string
    import capo_networkmanager.types.core_network_change_values


class CoreNetworkChange(TypedDict, closed=True):
    type: NotRequired["capo_networkmanager.types.change_type.ChangeType"]
    """<p>The type of change.</p>"""
    action: NotRequired["capo_networkmanager.types.change_action.ChangeAction"]
    """<p>The action to take for a core network.</p>"""
    identifier: NotRequired[
        "capo_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The resource identifier.</p>"""
    previous_values: NotRequired[
        "capo_networkmanager.types.core_network_change_values.CoreNetworkChangeValues"
    ]
    """<p>The previous values for a core network.</p>"""
    new_values: NotRequired[
        "capo_networkmanager.types.core_network_change_values.CoreNetworkChangeValues"
    ]
    """<p>The new value for a core network</p>"""
    identifier_path: NotRequired[
        "capo_networkmanager.types.constrained_string.ConstrainedString"
    ]
    r"""<p>Uniquely identifies the path for a change within the changeset. For example, the <code>IdentifierPath</code> for a core network segment change might be <code>\"CORE_NETWORK_SEGMENT/us-east-1/devsegment\"</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CoreNetworkChange) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_networkmanager.types.change_type

        out["Type"] = capo_networkmanager.types.change_type.serialize_json(
            value["type"]
        )
    if "action" in value:
        import capo_networkmanager.types.change_action

        out["Action"] = capo_networkmanager.types.change_action.serialize_json(
            value["action"]
        )
    if "identifier" in value:
        out["Identifier"] = value["identifier"]
    if "previous_values" in value:
        import capo_networkmanager.types.core_network_change_values

        out["PreviousValues"] = (
            capo_networkmanager.types.core_network_change_values.serialize_json(
                value["previous_values"]
            )
        )
    if "new_values" in value:
        import capo_networkmanager.types.core_network_change_values

        out["NewValues"] = (
            capo_networkmanager.types.core_network_change_values.serialize_json(
                value["new_values"]
            )
        )
    if "identifier_path" in value:
        out["IdentifierPath"] = value["identifier_path"]
    return out


def deserialize_json(data: dict) -> CoreNetworkChange:
    out: CoreNetworkChange = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import capo_networkmanager.types.change_type

        out["type"] = capo_networkmanager.types.change_type.deserialize_json(
            data["Type"]
        )
    if "Action" in data:
        import capo_networkmanager.types.change_action

        out["action"] = capo_networkmanager.types.change_action.deserialize_json(
            data["Action"]
        )
    if "Identifier" in data:
        out["identifier"] = data["Identifier"]
    if "PreviousValues" in data:
        import capo_networkmanager.types.core_network_change_values

        out["previous_values"] = (
            capo_networkmanager.types.core_network_change_values.deserialize_json(
                data["PreviousValues"]
            )
        )
    if "NewValues" in data:
        import capo_networkmanager.types.core_network_change_values

        out["new_values"] = (
            capo_networkmanager.types.core_network_change_values.deserialize_json(
                data["NewValues"]
            )
        )
    if "IdentifierPath" in data:
        out["identifier_path"] = data["IdentifierPath"]
    return out
