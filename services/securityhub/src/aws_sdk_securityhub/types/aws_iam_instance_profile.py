"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsIamInstanceProfile``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_iam_instance_profile_roles
    import aws_sdk_securityhub.types.non_empty_string


class AwsIamInstanceProfile(TypedDict):
    arn: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The ARN of the instance profile.</p>"""
    create_date: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>Indicates when the instance profile was created.</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href=\"https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps\">Timestamps</a>.</p>"""
    instance_profile_id: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The identifier of the instance profile.</p>"""
    instance_profile_name: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The name of the instance profile.</p>"""
    path: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The path to the instance profile.</p>"""
    roles: NotRequired[
        "aws_sdk_securityhub.types.aws_iam_instance_profile_roles.AwsIamInstanceProfileRoles"
    ]
    """<p>The roles associated with the instance profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsIamInstanceProfile) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "create_date" in value:
        out["CreateDate"] = value["create_date"]
    if "instance_profile_id" in value:
        out["InstanceProfileId"] = value["instance_profile_id"]
    if "instance_profile_name" in value:
        out["InstanceProfileName"] = value["instance_profile_name"]
    if "path" in value:
        out["Path"] = value["path"]
    if "roles" in value:
        import aws_sdk_securityhub.types.aws_iam_instance_profile_roles

        out["Roles"] = (
            aws_sdk_securityhub.types.aws_iam_instance_profile_roles.serialize_json(
                value["roles"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsIamInstanceProfile:
    out: AwsIamInstanceProfile = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "CreateDate" in data:
        out["create_date"] = data["CreateDate"]
    if "InstanceProfileId" in data:
        out["instance_profile_id"] = data["InstanceProfileId"]
    if "InstanceProfileName" in data:
        out["instance_profile_name"] = data["InstanceProfileName"]
    if "Path" in data:
        out["path"] = data["Path"]
    if "Roles" in data:
        import aws_sdk_securityhub.types.aws_iam_instance_profile_roles

        out["roles"] = (
            aws_sdk_securityhub.types.aws_iam_instance_profile_roles.deserialize_json(
                data["Roles"]
            )
        )
    return out
