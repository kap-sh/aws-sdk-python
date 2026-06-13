"""Generated from Smithy shape ``com.amazonaws.quicksight#ReadClientCredentialsDetails``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_quicksight.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.read_client_credentials_grant_details


class _ReadClientCredentialsDetails_ReadClientCredentialsGrantDetails(TypedDict):
    ReadClientCredentialsGrantDetails: "aws_sdk_quicksight.types.read_client_credentials_grant_details.ReadClientCredentialsGrantDetails"


ReadClientCredentialsDetails: TypeAlias = (
    _ReadClientCredentialsDetails_ReadClientCredentialsGrantDetails
)


# --- restJson1 ser/de ---
def serialize_json(value: ReadClientCredentialsDetails) -> dict:
    if "ReadClientCredentialsGrantDetails" in value:
        import aws_sdk_quicksight.types.read_client_credentials_grant_details

        return {
            "ReadClientCredentialsGrantDetails": aws_sdk_quicksight.types.read_client_credentials_grant_details.serialize_json(
                value["ReadClientCredentialsGrantDetails"]
            )
        }
    else:
        raise SerializationError("ReadClientCredentialsDetails: no variant present")


def deserialize_json(data: dict) -> ReadClientCredentialsDetails:
    if "ReadClientCredentialsGrantDetails" in data:
        import aws_sdk_quicksight.types.read_client_credentials_grant_details

        return {
            "ReadClientCredentialsGrantDetails": aws_sdk_quicksight.types.read_client_credentials_grant_details.deserialize_json(
                data["ReadClientCredentialsGrantDetails"]
            )
        }
    else:
        raise DeserializationError(
            "ReadClientCredentialsDetails: no recognized variant key"
        )
