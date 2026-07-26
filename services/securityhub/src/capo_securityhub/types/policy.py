"""Generated from Smithy shape ``com.amazonaws.securityhub#Policy``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_securityhub.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_securityhub.types.security_hub_policy


class _Policy_SecurityHub(TypedDict, closed=True):
    SecurityHub: "capo_securityhub.types.security_hub_policy.SecurityHubPolicy"


Policy: TypeAlias = _Policy_SecurityHub


# --- restJson1 ser/de ---
def serialize_json(value: Policy) -> dict:
    if "SecurityHub" in value:
        import capo_securityhub.types.security_hub_policy

        return {
            "SecurityHub": capo_securityhub.types.security_hub_policy.serialize_json(
                value["SecurityHub"]
            )
        }
    else:
        raise SerializationError("Policy: no variant present")


def deserialize_json(data: dict) -> Policy:
    if "SecurityHub" in data:
        import capo_securityhub.types.security_hub_policy

        return {
            "SecurityHub": capo_securityhub.types.security_hub_policy.deserialize_json(
                data["SecurityHub"]
            )
        }
    else:
        raise DeserializationError("Policy: no recognized variant key")
