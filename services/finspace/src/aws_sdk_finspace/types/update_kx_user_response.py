"""Generated from Smithy shape ``com.amazonaws.finspace#UpdateKxUserResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_finspace.types.id_type
    import aws_sdk_finspace.types.kx_user_arn
    import aws_sdk_finspace.types.kx_user_name_string
    import aws_sdk_finspace.types.role_arn


class UpdateKxUserResponse(TypedDict):
    user_name: NotRequired[
        "aws_sdk_finspace.types.kx_user_name_string.KxUserNameString"
    ]
    """<p>A unique identifier for the user.</p>"""
    user_arn: NotRequired["aws_sdk_finspace.types.kx_user_arn.KxUserArn"]
    r"""<p> The Amazon Resource Name (ARN) that identifies the user. For more information about ARNs and how to use ARNs in policies, see <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html\">IAM Identifiers</a> in the <i>IAM User Guide</i>. </p>"""
    environment_id: NotRequired["aws_sdk_finspace.types.id_type.IdType"]
    """<p>A unique identifier for the kdb environment.</p>"""
    iam_role: NotRequired["aws_sdk_finspace.types.role_arn.RoleArn"]
    """<p>The IAM role ARN that is associated with the user.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateKxUserResponse) -> dict:
    out: dict = {}
    if "user_name" in value:
        out["userName"] = value["user_name"]
    if "user_arn" in value:
        out["userArn"] = value["user_arn"]
    if "environment_id" in value:
        out["environmentId"] = value["environment_id"]
    if "iam_role" in value:
        out["iamRole"] = value["iam_role"]
    return out


def deserialize_json(data: dict) -> UpdateKxUserResponse:
    out: UpdateKxUserResponse = {}  # type: ignore[typeddict-item]
    if "userName" in data:
        out["user_name"] = data["userName"]
    if "userArn" in data:
        out["user_arn"] = data["userArn"]
    if "environmentId" in data:
        out["environment_id"] = data["environmentId"]
    if "iamRole" in data:
        out["iam_role"] = data["iamRole"]
    return out
