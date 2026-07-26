"""Generated from Smithy shape ``com.amazonaws.qbusiness#Principal``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_qbusiness.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_qbusiness.types.principal_group
    import capo_qbusiness.types.principal_user


class _Principal_user(TypedDict, closed=True):
    user: "capo_qbusiness.types.principal_user.PrincipalUser"


class _Principal_group(TypedDict, closed=True):
    group: "capo_qbusiness.types.principal_group.PrincipalGroup"


Principal: TypeAlias = _Principal_user | _Principal_group


# --- restJson1 ser/de ---
def serialize_json(value: Principal) -> dict:
    if "user" in value:
        import capo_qbusiness.types.principal_user

        return {
            "user": capo_qbusiness.types.principal_user.serialize_json(value["user"])
        }
    elif "group" in value:
        import capo_qbusiness.types.principal_group

        return {
            "group": capo_qbusiness.types.principal_group.serialize_json(value["group"])
        }
    else:
        raise SerializationError("Principal: no variant present")


def deserialize_json(data: dict) -> Principal:
    if "user" in data:
        import capo_qbusiness.types.principal_user

        return {
            "user": capo_qbusiness.types.principal_user.deserialize_json(data["user"])
        }
    elif "group" in data:
        import capo_qbusiness.types.principal_group

        return {
            "group": capo_qbusiness.types.principal_group.deserialize_json(
                data["group"]
            )
        }
    else:
        raise DeserializationError("Principal: no recognized variant key")
