"""Generated from Smithy shape ``com.amazonaws.securityagent#MembershipConfig``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_securityagent.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_securityagent.types.user_config


class _MembershipConfig_user(TypedDict, closed=True):
    user: "capo_securityagent.types.user_config.UserConfig"


MembershipConfig: TypeAlias = _MembershipConfig_user


# --- restJson1 ser/de ---
def serialize_json(value: MembershipConfig) -> dict:
    if "user" in value:
        import capo_securityagent.types.user_config

        return {
            "user": capo_securityagent.types.user_config.serialize_json(value["user"])
        }
    else:
        raise SerializationError("MembershipConfig: no variant present")


def deserialize_json(data: dict) -> MembershipConfig:
    if "user" in data:
        import capo_securityagent.types.user_config

        return {
            "user": capo_securityagent.types.user_config.deserialize_json(data["user"])
        }
    else:
        raise DeserializationError("MembershipConfig: no recognized variant key")
