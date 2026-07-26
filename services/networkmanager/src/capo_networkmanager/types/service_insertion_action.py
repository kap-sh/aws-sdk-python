"""Generated from Smithy shape ``com.amazonaws.networkmanager#ServiceInsertionAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.segment_action_service_insertion
    import capo_networkmanager.types.send_via_mode
    import capo_networkmanager.types.via
    import capo_networkmanager.types.when_sent_to


class ServiceInsertionAction(TypedDict, closed=True):
    action: NotRequired[
        "capo_networkmanager.types.segment_action_service_insertion.SegmentActionServiceInsertion"
    ]
    """<p>The action the service insertion takes for traffic. <code>send-via</code> sends east-west traffic between attachments. <code>send-to</code> sends north-south traffic to the security appliance, and then from that to either the Internet or to an on-premesis location. </p>"""
    mode: NotRequired["capo_networkmanager.types.send_via_mode.SendViaMode"]
    """<p>Describes the mode packets take for the <code>send-via</code> action. This is not used when the action is <code>send-to</code>. <code>dual-hop</code> packets traverse attachments in both the source to the destination core network edges. This mode requires that an inspection attachment must be present in all Regions of the service insertion-enabled segments. For <code>single-hop</code>, packets traverse a single intermediate inserted attachment. You can use <code>EdgeOverride</code> to specify a specific edge to use. </p>"""
    when_sent_to: NotRequired["capo_networkmanager.types.when_sent_to.WhenSentTo"]
    """<p>The list of destination segments if the service insertion action is <code>send-via</code>.</p>"""
    via: NotRequired["capo_networkmanager.types.via.Via"]
    """<p>The list of network function groups and any edge overrides for the chosen service insertion action. Used for both <code>send-to</code> or <code>send-via</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceInsertionAction) -> dict:
    out: dict = {}
    if "action" in value:
        import capo_networkmanager.types.segment_action_service_insertion

        out["Action"] = (
            capo_networkmanager.types.segment_action_service_insertion.serialize_json(
                value["action"]
            )
        )
    if "mode" in value:
        import capo_networkmanager.types.send_via_mode

        out["Mode"] = capo_networkmanager.types.send_via_mode.serialize_json(
            value["mode"]
        )
    if "when_sent_to" in value:
        import capo_networkmanager.types.when_sent_to

        out["WhenSentTo"] = capo_networkmanager.types.when_sent_to.serialize_json(
            value["when_sent_to"]
        )
    if "via" in value:
        import capo_networkmanager.types.via

        out["Via"] = capo_networkmanager.types.via.serialize_json(value["via"])
    return out


def deserialize_json(data: dict) -> ServiceInsertionAction:
    out: ServiceInsertionAction = {}  # type: ignore[typeddict-item]
    if "Action" in data:
        import capo_networkmanager.types.segment_action_service_insertion

        out["action"] = (
            capo_networkmanager.types.segment_action_service_insertion.deserialize_json(
                data["Action"]
            )
        )
    if "Mode" in data:
        import capo_networkmanager.types.send_via_mode

        out["mode"] = capo_networkmanager.types.send_via_mode.deserialize_json(
            data["Mode"]
        )
    if "WhenSentTo" in data:
        import capo_networkmanager.types.when_sent_to

        out["when_sent_to"] = capo_networkmanager.types.when_sent_to.deserialize_json(
            data["WhenSentTo"]
        )
    if "Via" in data:
        import capo_networkmanager.types.via

        out["via"] = capo_networkmanager.types.via.deserialize_json(data["Via"])
    return out
