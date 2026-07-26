"""Generated from Smithy shape ``com.amazonaws.datazone#UserProfileDetails``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_datazone.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_datazone.types.iam_user_profile_details
    import capo_datazone.types.sso_user_profile_details


class _UserProfileDetails_iam(TypedDict, closed=True):
    iam: "capo_datazone.types.iam_user_profile_details.IamUserProfileDetails"


class _UserProfileDetails_sso(TypedDict, closed=True):
    sso: "capo_datazone.types.sso_user_profile_details.SsoUserProfileDetails"


UserProfileDetails: TypeAlias = _UserProfileDetails_iam | _UserProfileDetails_sso


# --- restJson1 ser/de ---
def serialize_json(value: UserProfileDetails) -> dict:
    if "iam" in value:
        import capo_datazone.types.iam_user_profile_details

        return {
            "iam": capo_datazone.types.iam_user_profile_details.serialize_json(
                value["iam"]
            )
        }
    elif "sso" in value:
        import capo_datazone.types.sso_user_profile_details

        return {
            "sso": capo_datazone.types.sso_user_profile_details.serialize_json(
                value["sso"]
            )
        }
    else:
        raise SerializationError("UserProfileDetails: no variant present")


def deserialize_json(data: dict) -> UserProfileDetails:
    if "iam" in data:
        import capo_datazone.types.iam_user_profile_details

        return {
            "iam": capo_datazone.types.iam_user_profile_details.deserialize_json(
                data["iam"]
            )
        }
    elif "sso" in data:
        import capo_datazone.types.sso_user_profile_details

        return {
            "sso": capo_datazone.types.sso_user_profile_details.deserialize_json(
                data["sso"]
            )
        }
    else:
        raise DeserializationError("UserProfileDetails: no recognized variant key")
