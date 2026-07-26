"""Generated from Smithy shape ``com.amazonaws.datazone#MemberDetails``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_datazone.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_datazone.types.group_details
    import capo_datazone.types.user_details


class _MemberDetails_user(TypedDict, closed=True):
    user: "capo_datazone.types.user_details.UserDetails"


class _MemberDetails_group(TypedDict, closed=True):
    group: "capo_datazone.types.group_details.GroupDetails"


MemberDetails: TypeAlias = _MemberDetails_user | _MemberDetails_group


# --- restJson1 ser/de ---
def serialize_json(value: MemberDetails) -> dict:
    if "user" in value:
        import capo_datazone.types.user_details

        return {"user": capo_datazone.types.user_details.serialize_json(value["user"])}
    elif "group" in value:
        import capo_datazone.types.group_details

        return {
            "group": capo_datazone.types.group_details.serialize_json(value["group"])
        }
    else:
        raise SerializationError("MemberDetails: no variant present")


def deserialize_json(data: dict) -> MemberDetails:
    if "user" in data:
        import capo_datazone.types.user_details

        return {"user": capo_datazone.types.user_details.deserialize_json(data["user"])}
    elif "group" in data:
        import capo_datazone.types.group_details

        return {
            "group": capo_datazone.types.group_details.deserialize_json(data["group"])
        }
    else:
        raise DeserializationError("MemberDetails: no recognized variant key")
