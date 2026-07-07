"""Generated from Smithy shape ``com.amazonaws.sagemaker#UserContext``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.iam_identity
    import aws_sdk_sagemaker.types.string


class UserContext(TypedDict, closed=True):
    user_profile_arn: NotRequired["aws_sdk_sagemaker.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the user's profile.</p>"""
    user_profile_name: NotRequired["aws_sdk_sagemaker.types.string.String"]
    """<p>The name of the user's profile.</p>"""
    domain_id: NotRequired["aws_sdk_sagemaker.types.string.String"]
    """<p>The domain associated with the user.</p>"""
    iam_identity: NotRequired["aws_sdk_sagemaker.types.iam_identity.IamIdentity"]
    """<p>The IAM Identity details associated with the user. These details are associated with model package groups, model packages, and project entities only.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UserContext) -> dict:
    out: dict = {}
    if "user_profile_arn" in value:
        out["UserProfileArn"] = value["user_profile_arn"]
    if "user_profile_name" in value:
        out["UserProfileName"] = value["user_profile_name"]
    if "domain_id" in value:
        out["DomainId"] = value["domain_id"]
    if "iam_identity" in value:
        import aws_sdk_sagemaker.types.iam_identity

        out["IamIdentity"] = (
            aws_sdk_sagemaker.types.iam_identity.serialize_aws_json_1_1(
                value["iam_identity"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UserContext:
    out: UserContext = {}  # type: ignore[typeddict-item]
    if "UserProfileArn" in data:
        out["user_profile_arn"] = data["UserProfileArn"]
    if "UserProfileName" in data:
        out["user_profile_name"] = data["UserProfileName"]
    if "DomainId" in data:
        out["domain_id"] = data["DomainId"]
    if "IamIdentity" in data:
        import aws_sdk_sagemaker.types.iam_identity

        out["iam_identity"] = (
            aws_sdk_sagemaker.types.iam_identity.deserialize_aws_json_1_1(
                data["IamIdentity"]
            )
        )
    return out
