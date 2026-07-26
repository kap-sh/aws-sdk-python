"""Generated from Smithy shape ``com.amazonaws.qbusiness#ActionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_qbusiness.errors import DeserializationError

if TYPE_CHECKING:
    import capo_qbusiness.types.action_filter_configuration
    import capo_qbusiness.types.q_iam_action


class ActionConfiguration(TypedDict, closed=True):
    action: "capo_qbusiness.types.q_iam_action.QIamAction"
    """<p>The Amazon Q Business action that is allowed.</p>"""
    filter_configuration: NotRequired[
        "capo_qbusiness.types.action_filter_configuration.ActionFilterConfiguration"
    ]
    """<p>The filter configuration for the action, if any.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ActionConfiguration) -> dict:
    out: dict = {}
    out["action"] = value["action"]
    if "filter_configuration" in value:
        import capo_qbusiness.types.action_filter_configuration

        out["filterConfiguration"] = (
            capo_qbusiness.types.action_filter_configuration.serialize_json(
                value["filter_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> ActionConfiguration:
    out: ActionConfiguration = {}  # type: ignore[typeddict-item]
    if "action" in data:
        out["action"] = data["action"]
    else:
        raise DeserializationError("ActionConfiguration.action required")
    if "filterConfiguration" in data:
        import capo_qbusiness.types.action_filter_configuration

        out["filter_configuration"] = (
            capo_qbusiness.types.action_filter_configuration.deserialize_json(
                data["filterConfiguration"]
            )
        )
    return out
