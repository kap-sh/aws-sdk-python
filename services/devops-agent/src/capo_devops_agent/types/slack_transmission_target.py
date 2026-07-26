"""Generated from Smithy shape ``com.amazonaws.devopsagent#SlackTransmissionTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_devops_agent.types.slack_channel


class SlackTransmissionTarget(TypedDict, closed=True):
    ops_oncall_target: "capo_devops_agent.types.slack_channel.SlackChannel"
    """<p>Destination for On-call Agent (Ops1)</p>"""
    ops_sre_target: NotRequired["capo_devops_agent.types.slack_channel.SlackChannel"]
    """<p>Destination for SRE Agent (Ops1.5)</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SlackTransmissionTarget) -> dict:
    out: dict = {}
    import capo_devops_agent.types.slack_channel

    out["opsOncallTarget"] = capo_devops_agent.types.slack_channel.serialize_json(
        value["ops_oncall_target"]
    )
    if "ops_sre_target" in value:
        import capo_devops_agent.types.slack_channel

        out["opsSRETarget"] = capo_devops_agent.types.slack_channel.serialize_json(
            value["ops_sre_target"]
        )
    return out


def deserialize_json(data: dict) -> SlackTransmissionTarget:
    out: SlackTransmissionTarget = {}  # type: ignore[typeddict-item]
    if "opsOncallTarget" in data:
        import capo_devops_agent.types.slack_channel

        out["ops_oncall_target"] = (
            capo_devops_agent.types.slack_channel.deserialize_json(
                data["opsOncallTarget"]
            )
        )
    else:
        raise DeserializationError("SlackTransmissionTarget.ops_oncall_target required")
    if "opsSRETarget" in data:
        import capo_devops_agent.types.slack_channel

        out["ops_sre_target"] = capo_devops_agent.types.slack_channel.deserialize_json(
            data["opsSRETarget"]
        )
    return out
