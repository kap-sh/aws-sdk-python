"""Generated from Smithy shape ``com.amazonaws.datazone#UserProfileDetails``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_datazone.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.iam_user_profile_details
    import aws_sdk_datazone.types.sso_user_profile_details


class _UserProfileDetails_iam(TypedDict):
    iam: "aws_sdk_datazone.types.iam_user_profile_details.IamUserProfileDetails"


class _UserProfileDetails_sso(TypedDict):
    sso: "aws_sdk_datazone.types.sso_user_profile_details.SsoUserProfileDetails"


UserProfileDetails: TypeAlias = _UserProfileDetails_iam | _UserProfileDetails_sso


# --- restJson1 ser/de ---
def serialize_json(value: UserProfileDetails) -> dict:
    if "iam" in value:
        import aws_sdk_datazone.types.iam_user_profile_details

        return {
            "iam": aws_sdk_datazone.types.iam_user_profile_details.serialize_json(
                value["iam"]
            )
        }
    elif "sso" in value:
        import aws_sdk_datazone.types.sso_user_profile_details

        return {
            "sso": aws_sdk_datazone.types.sso_user_profile_details.serialize_json(
                value["sso"]
            )
        }
    else:
        raise SerializationError("UserProfileDetails: no variant present")


def deserialize_json(data: dict) -> UserProfileDetails:
    if "iam" in data:
        import aws_sdk_datazone.types.iam_user_profile_details

        return {
            "iam": aws_sdk_datazone.types.iam_user_profile_details.deserialize_json(
                data["iam"]
            )
        }
    elif "sso" in data:
        import aws_sdk_datazone.types.sso_user_profile_details

        return {
            "sso": aws_sdk_datazone.types.sso_user_profile_details.deserialize_json(
                data["sso"]
            )
        }
    else:
        raise DeserializationError("UserProfileDetails: no recognized variant key")
