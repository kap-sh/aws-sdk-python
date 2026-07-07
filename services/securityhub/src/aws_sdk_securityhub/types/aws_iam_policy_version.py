"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsIamPolicyVersion``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.boolean
    import aws_sdk_securityhub.types.non_empty_string


class AwsIamPolicyVersion(TypedDict, closed=True):
    version_id: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The identifier of the policy version.</p>"""
    is_default_version: NotRequired["aws_sdk_securityhub.types.boolean.Boolean"]
    """<p>Whether the version is the default version.</p>"""
    create_date: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    r"""<p>Indicates when the version was created.</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href=\"https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps\">Timestamps</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsIamPolicyVersion) -> dict:
    out: dict = {}
    if "version_id" in value:
        out["VersionId"] = value["version_id"]
    if "is_default_version" in value:
        out["IsDefaultVersion"] = value["is_default_version"]
    if "create_date" in value:
        out["CreateDate"] = value["create_date"]
    return out


def deserialize_json(data: dict) -> AwsIamPolicyVersion:
    out: AwsIamPolicyVersion = {}  # type: ignore[typeddict-item]
    if "VersionId" in data:
        out["version_id"] = data["VersionId"]
    if "IsDefaultVersion" in data:
        out["is_default_version"] = data["IsDefaultVersion"]
    if "CreateDate" in data:
        out["create_date"] = data["CreateDate"]
    return out
