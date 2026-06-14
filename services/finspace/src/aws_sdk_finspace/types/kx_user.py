"""Generated from Smithy shape ``com.amazonaws.finspace#KxUser``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_finspace.types.kx_user_arn
    import aws_sdk_finspace.types.kx_user_name_string
    import aws_sdk_finspace.types.role_arn
    import aws_sdk_finspace.types.timestamp


class KxUser(TypedDict):
    user_arn: NotRequired["aws_sdk_finspace.types.kx_user_arn.KxUserArn"]
    r"""<p> The Amazon Resource Name (ARN) that identifies the user. For more information about ARNs and how to use ARNs in policies, see <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html\">IAM Identifiers</a> in the <i>IAM User Guide</i>. </p>"""
    user_name: NotRequired[
        "aws_sdk_finspace.types.kx_user_name_string.KxUserNameString"
    ]
    """<p>A unique identifier for the user.</p>"""
    iam_role: NotRequired["aws_sdk_finspace.types.role_arn.RoleArn"]
    """<p>The IAM role ARN that is associated with the user.</p>"""
    create_timestamp: NotRequired["aws_sdk_finspace.types.timestamp.Timestamp"]
    """<p>The timestamp at which the kdb user was created. </p>"""
    update_timestamp: NotRequired["aws_sdk_finspace.types.timestamp.Timestamp"]
    """<p>The timestamp at which the kdb user was updated. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KxUser) -> dict:
    out: dict = {}
    if "user_arn" in value:
        out["userArn"] = value["user_arn"]
    if "user_name" in value:
        out["userName"] = value["user_name"]
    if "iam_role" in value:
        out["iamRole"] = value["iam_role"]
    if "create_timestamp" in value:
        import aws_sdk_finspace.types.timestamp

        out["createTimestamp"] = aws_sdk_finspace.types.timestamp.serialize_json(
            value["create_timestamp"]
        )
    if "update_timestamp" in value:
        import aws_sdk_finspace.types.timestamp

        out["updateTimestamp"] = aws_sdk_finspace.types.timestamp.serialize_json(
            value["update_timestamp"]
        )
    return out


def deserialize_json(data: dict) -> KxUser:
    out: KxUser = {}  # type: ignore[typeddict-item]
    if "userArn" in data:
        out["user_arn"] = data["userArn"]
    if "userName" in data:
        out["user_name"] = data["userName"]
    if "iamRole" in data:
        out["iam_role"] = data["iamRole"]
    if "createTimestamp" in data:
        import aws_sdk_finspace.types.timestamp

        out["create_timestamp"] = aws_sdk_finspace.types.timestamp.deserialize_json(
            data["createTimestamp"]
        )
    if "updateTimestamp" in data:
        import aws_sdk_finspace.types.timestamp

        out["update_timestamp"] = aws_sdk_finspace.types.timestamp.deserialize_json(
            data["updateTimestamp"]
        )
    return out
