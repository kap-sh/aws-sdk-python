"""Generated from Smithy shape ``com.amazonaws.securityagent#ProviderInput``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_securityagent.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_securityagent.types.git_hub_integration_input


class _ProviderInput_github(TypedDict, closed=True):
    github: "capo_securityagent.types.git_hub_integration_input.GitHubIntegrationInput"


ProviderInput: TypeAlias = _ProviderInput_github


# --- restJson1 ser/de ---
def serialize_json(value: ProviderInput) -> dict:
    if "github" in value:
        import capo_securityagent.types.git_hub_integration_input

        return {
            "github": capo_securityagent.types.git_hub_integration_input.serialize_json(
                value["github"]
            )
        }
    else:
        raise SerializationError("ProviderInput: no variant present")


def deserialize_json(data: dict) -> ProviderInput:
    if "github" in data:
        import capo_securityagent.types.git_hub_integration_input

        return {
            "github": capo_securityagent.types.git_hub_integration_input.deserialize_json(
                data["github"]
            )
        }
    else:
        raise DeserializationError("ProviderInput: no recognized variant key")
