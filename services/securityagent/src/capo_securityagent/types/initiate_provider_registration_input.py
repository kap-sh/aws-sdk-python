"""Generated from Smithy shape ``com.amazonaws.securityagent#InitiateProviderRegistrationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_securityagent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_securityagent.types.provider


class InitiateProviderRegistrationInput(TypedDict, closed=True):
    provider: "capo_securityagent.types.provider.Provider"
    """<p>The provider to initiate registration with. Currently, only GITHUB is supported.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InitiateProviderRegistrationInput) -> dict:
    out: dict = {}
    import capo_securityagent.types.provider

    out["provider"] = capo_securityagent.types.provider.serialize_json(
        value["provider"]
    )
    return out


def deserialize_json(data: dict) -> InitiateProviderRegistrationInput:
    out: InitiateProviderRegistrationInput = {}  # type: ignore[typeddict-item]
    if "provider" in data:
        import capo_securityagent.types.provider

        out["provider"] = capo_securityagent.types.provider.deserialize_json(
            data["provider"]
        )
    else:
        raise DeserializationError(
            "InitiateProviderRegistrationInput.provider required"
        )
    return out
