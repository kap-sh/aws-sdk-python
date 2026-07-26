"""Generated from Smithy shape ``com.amazonaws.ssmincidents#Action``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_ssm_incidents.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_ssm_incidents.types.ssm_automation


class _Action_ssmAutomation(TypedDict, closed=True):
    ssmAutomation: "capo_ssm_incidents.types.ssm_automation.SsmAutomation"


Action: TypeAlias = _Action_ssmAutomation


# --- restJson1 ser/de ---
def serialize_json(value: Action) -> dict:
    if "ssmAutomation" in value:
        import capo_ssm_incidents.types.ssm_automation

        return {
            "ssmAutomation": capo_ssm_incidents.types.ssm_automation.serialize_json(
                value["ssmAutomation"]
            )
        }
    else:
        raise SerializationError("Action: no variant present")


def deserialize_json(data: dict) -> Action:
    if "ssmAutomation" in data:
        import capo_ssm_incidents.types.ssm_automation

        return {
            "ssmAutomation": capo_ssm_incidents.types.ssm_automation.deserialize_json(
                data["ssmAutomation"]
            )
        }
    else:
        raise DeserializationError("Action: no recognized variant key")
