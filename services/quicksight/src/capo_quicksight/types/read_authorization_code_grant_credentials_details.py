"""Generated from Smithy shape ``com.amazonaws.quicksight#ReadAuthorizationCodeGrantCredentialsDetails``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_quicksight.types.read_authorization_code_grant_details


class _ReadAuthorizationCodeGrantCredentialsDetails_ReadAuthorizationCodeGrantDetails(
    TypedDict, closed=True
):
    ReadAuthorizationCodeGrantDetails: "capo_quicksight.types.read_authorization_code_grant_details.ReadAuthorizationCodeGrantDetails"


ReadAuthorizationCodeGrantCredentialsDetails: TypeAlias = (
    _ReadAuthorizationCodeGrantCredentialsDetails_ReadAuthorizationCodeGrantDetails
)


# --- restJson1 ser/de ---
def serialize_json(value: ReadAuthorizationCodeGrantCredentialsDetails) -> dict:
    if "ReadAuthorizationCodeGrantDetails" in value:
        import capo_quicksight.types.read_authorization_code_grant_details

        return {
            "ReadAuthorizationCodeGrantDetails": capo_quicksight.types.read_authorization_code_grant_details.serialize_json(
                value["ReadAuthorizationCodeGrantDetails"]
            )
        }
    else:
        raise SerializationError(
            "ReadAuthorizationCodeGrantCredentialsDetails: no variant present"
        )


def deserialize_json(data: dict) -> ReadAuthorizationCodeGrantCredentialsDetails:
    if "ReadAuthorizationCodeGrantDetails" in data:
        import capo_quicksight.types.read_authorization_code_grant_details

        return {
            "ReadAuthorizationCodeGrantDetails": capo_quicksight.types.read_authorization_code_grant_details.deserialize_json(
                data["ReadAuthorizationCodeGrantDetails"]
            )
        }
    else:
        raise DeserializationError(
            "ReadAuthorizationCodeGrantCredentialsDetails: no recognized variant key"
        )
