"""Generated from Smithy shape ``com.amazonaws.athena#CreatePresignedNotebookUrlResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_athena.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_athena.types.auth_token
    import aws_sdk_athena.types.long
    import aws_sdk_athena.types.string


class CreatePresignedNotebookUrlResponse(TypedDict, closed=True):
    notebook_url: "aws_sdk_athena.types.string.String"
    """<p>The URL of the notebook. The URL includes the authentication token and notebook file name and points directly to the opened notebook.</p>"""
    auth_token: "aws_sdk_athena.types.auth_token.AuthToken"
    """<p>The authentication token for the notebook.</p>"""
    auth_token_expiration_time: "aws_sdk_athena.types.long.Long"
    """<p>The UTC epoch time when the authentication token expires.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreatePresignedNotebookUrlResponse) -> dict:
    out: dict = {}
    out["NotebookUrl"] = value["notebook_url"]
    out["AuthToken"] = value["auth_token"]
    out["AuthTokenExpirationTime"] = value["auth_token_expiration_time"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreatePresignedNotebookUrlResponse:
    out: CreatePresignedNotebookUrlResponse = {}  # type: ignore[typeddict-item]
    if "NotebookUrl" in data:
        out["notebook_url"] = data["NotebookUrl"]
    else:
        raise DeserializationError(
            "CreatePresignedNotebookUrlResponse.notebook_url required"
        )
    if "AuthToken" in data:
        out["auth_token"] = data["AuthToken"]
    else:
        raise DeserializationError(
            "CreatePresignedNotebookUrlResponse.auth_token required"
        )
    if "AuthTokenExpirationTime" in data:
        out["auth_token_expiration_time"] = data["AuthTokenExpirationTime"]
    else:
        raise DeserializationError(
            "CreatePresignedNotebookUrlResponse.auth_token_expiration_time required"
        )
    return out
