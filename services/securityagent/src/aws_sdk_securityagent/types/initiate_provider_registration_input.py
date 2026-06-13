"""Generated from Smithy shape ``com.amazonaws.securityagent#InitiateProviderRegistrationInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_securityagent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_securityagent.types.provider


class InitiateProviderRegistrationInput(TypedDict):
    provider: "aws_sdk_securityagent.types.provider.Provider"
    """<p>The provider to initiate registration with. Currently, only GITHUB is supported.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InitiateProviderRegistrationInput) -> dict:
    out: dict = {}
    import aws_sdk_securityagent.types.provider

    out["provider"] = aws_sdk_securityagent.types.provider.serialize_json(
        value["provider"]
    )
    return out


def deserialize_json(data: dict) -> InitiateProviderRegistrationInput:
    out: InitiateProviderRegistrationInput = {}  # type: ignore[typeddict-item]
    if "provider" in data:
        import aws_sdk_securityagent.types.provider

        out["provider"] = aws_sdk_securityagent.types.provider.deserialize_json(
            data["provider"]
        )
    else:
        raise DeserializationError(
            "InitiateProviderRegistrationInput.provider required"
        )
    return out
