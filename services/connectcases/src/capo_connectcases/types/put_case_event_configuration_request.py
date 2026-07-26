"""Generated from Smithy shape ``com.amazonaws.connectcases#PutCaseEventConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_connectcases.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connectcases.types.domain_id
    import capo_connectcases.types.event_bridge_configuration


class PutCaseEventConfigurationRequest(TypedDict, closed=True):
    domain_id: "capo_connectcases.types.domain_id.DomainId"
    """<p>The unique identifier of the Cases domain. </p>"""
    event_bridge: (
        "capo_connectcases.types.event_bridge_configuration.EventBridgeConfiguration"
    )
    """<p>Configuration to enable EventBridge case event delivery and determine what data is delivered.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutCaseEventConfigurationRequest) -> dict:
    out: dict = {}
    import capo_connectcases.types.event_bridge_configuration

    out["eventBridge"] = (
        capo_connectcases.types.event_bridge_configuration.serialize_json(
            value["event_bridge"]
        )
    )
    return out


def deserialize_json(data: dict) -> PutCaseEventConfigurationRequest:
    out: PutCaseEventConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "eventBridge" in data:
        import capo_connectcases.types.event_bridge_configuration

        out["event_bridge"] = (
            capo_connectcases.types.event_bridge_configuration.deserialize_json(
                data["eventBridge"]
            )
        )
    else:
        raise DeserializationError(
            "PutCaseEventConfigurationRequest.event_bridge required"
        )
    return out
