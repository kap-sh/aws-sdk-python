"""Generated from Smithy shape ``com.amazonaws.devopsagent#AdditionalServiceRegistrationStep``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_devops_agent.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_devops_agent.types.o_auth_additional_step_details


class _AdditionalServiceRegistrationStep_oauth(TypedDict, closed=True):
    oauth: "capo_devops_agent.types.o_auth_additional_step_details.OAuthAdditionalStepDetails"


AdditionalServiceRegistrationStep: TypeAlias = _AdditionalServiceRegistrationStep_oauth


# --- restJson1 ser/de ---
def serialize_json(value: AdditionalServiceRegistrationStep) -> dict:
    if "oauth" in value:
        import capo_devops_agent.types.o_auth_additional_step_details

        return {
            "oauth": capo_devops_agent.types.o_auth_additional_step_details.serialize_json(
                value["oauth"]
            )
        }
    else:
        raise SerializationError(
            "AdditionalServiceRegistrationStep: no variant present"
        )


def deserialize_json(data: dict) -> AdditionalServiceRegistrationStep:
    if "oauth" in data:
        import capo_devops_agent.types.o_auth_additional_step_details

        return {
            "oauth": capo_devops_agent.types.o_auth_additional_step_details.deserialize_json(
                data["oauth"]
            )
        }
    else:
        raise DeserializationError(
            "AdditionalServiceRegistrationStep: no recognized variant key"
        )
