"""Generated from Smithy shape ``com.amazonaws.sagemaker#IamIdentity``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.string


class IamIdentity(TypedDict):
    arn: NotRequired["aws_sdk_sagemaker.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the IAM identity.</p>"""
    principal_id: NotRequired["aws_sdk_sagemaker.types.string.String"]
    """<p>The ID of the principal that assumes the IAM identity.</p>"""
    source_identity: NotRequired["aws_sdk_sagemaker.types.string.String"]
    """<p>The person or application which assumes the IAM identity.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IamIdentity) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "principal_id" in value:
        out["PrincipalId"] = value["principal_id"]
    if "source_identity" in value:
        out["SourceIdentity"] = value["source_identity"]
    return out


def deserialize_aws_json_1_1(data: dict) -> IamIdentity:
    out: IamIdentity = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "PrincipalId" in data:
        out["principal_id"] = data["PrincipalId"]
    if "SourceIdentity" in data:
        out["source_identity"] = data["SourceIdentity"]
    return out
