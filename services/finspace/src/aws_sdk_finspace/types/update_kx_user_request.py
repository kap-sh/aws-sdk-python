"""Generated from Smithy shape ``com.amazonaws.finspace#UpdateKxUserRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_finspace.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_finspace.types.client_token
    import aws_sdk_finspace.types.id_type
    import aws_sdk_finspace.types.kx_user_name_string
    import aws_sdk_finspace.types.role_arn


class UpdateKxUserRequest(TypedDict):
    environment_id: "aws_sdk_finspace.types.id_type.IdType"
    """<p>A unique identifier for the kdb environment.</p>"""
    user_name: "aws_sdk_finspace.types.kx_user_name_string.KxUserNameString"
    """<p>A unique identifier for the user.</p>"""
    iam_role: "aws_sdk_finspace.types.role_arn.RoleArn"
    """<p>The IAM role ARN that is associated with the user.</p>"""
    client_token: NotRequired["aws_sdk_finspace.types.client_token.ClientToken"]
    """<p>A token that ensures idempotency. This token expires in 10 minutes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateKxUserRequest) -> dict:
    out: dict = {}
    out["iamRole"] = value["iam_role"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> UpdateKxUserRequest:
    out: UpdateKxUserRequest = {}  # type: ignore[typeddict-item]
    if "iamRole" in data:
        out["iam_role"] = data["iamRole"]
    else:
        raise DeserializationError("UpdateKxUserRequest.iam_role required")
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
