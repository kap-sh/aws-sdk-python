"""Generated from Smithy shape ``com.amazonaws.quicksight#ClientCredentialsDetails``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_quicksight.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.client_credentials_grant_details


class _ClientCredentialsDetails_ClientCredentialsGrantDetails(TypedDict, closed=True):
    ClientCredentialsGrantDetails: "aws_sdk_quicksight.types.client_credentials_grant_details.ClientCredentialsGrantDetails"


ClientCredentialsDetails: TypeAlias = (
    _ClientCredentialsDetails_ClientCredentialsGrantDetails
)


# --- restJson1 ser/de ---
def serialize_json(value: ClientCredentialsDetails) -> dict:
    if "ClientCredentialsGrantDetails" in value:
        import aws_sdk_quicksight.types.client_credentials_grant_details

        return {
            "ClientCredentialsGrantDetails": aws_sdk_quicksight.types.client_credentials_grant_details.serialize_json(
                value["ClientCredentialsGrantDetails"]
            )
        }
    else:
        raise SerializationError("ClientCredentialsDetails: no variant present")


def deserialize_json(data: dict) -> ClientCredentialsDetails:
    if "ClientCredentialsGrantDetails" in data:
        import aws_sdk_quicksight.types.client_credentials_grant_details

        return {
            "ClientCredentialsGrantDetails": aws_sdk_quicksight.types.client_credentials_grant_details.deserialize_json(
                data["ClientCredentialsGrantDetails"]
            )
        }
    else:
        raise DeserializationError(
            "ClientCredentialsDetails: no recognized variant key"
        )
