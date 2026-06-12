"""Generated from Smithy shape ``com.amazonaws.kendra#UpdateExperienceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kendra.types.description
    import aws_sdk_kendra.types.experience_configuration
    import aws_sdk_kendra.types.experience_id
    import aws_sdk_kendra.types.experience_name
    import aws_sdk_kendra.types.index_id
    import aws_sdk_kendra.types.role_arn


class UpdateExperienceRequest(TypedDict):
    id: "aws_sdk_kendra.types.experience_id.ExperienceId"
    """<p>The identifier of your Amazon Kendra experience you want to update.</p>"""
    name: NotRequired["aws_sdk_kendra.types.experience_name.ExperienceName"]
    """<p>A new name for your Amazon Kendra experience.</p>"""
    index_id: "aws_sdk_kendra.types.index_id.IndexId"
    """<p>The identifier of the index for your Amazon Kendra experience.</p>"""
    role_arn: NotRequired["aws_sdk_kendra.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of an IAM role with permission to access the <code>Query</code> API, <code>QuerySuggestions</code> API, <code>SubmitFeedback</code> API, and IAM Identity Center that stores your users and groups information. For more information, see <a href=\"https://docs.aws.amazon.com/kendra/latest/dg/iam-roles.html\">IAM roles for Amazon Kendra</a>.</p>"""
    configuration: NotRequired[
        "aws_sdk_kendra.types.experience_configuration.ExperienceConfiguration"
    ]
    """<p>Configuration information you want to update for your Amazon Kendra experience.</p>"""
    description: NotRequired["aws_sdk_kendra.types.description.Description"]
    """<p>A new description for your Amazon Kendra experience.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateExperienceRequest) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    out["IndexId"] = value["index_id"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "configuration" in value:
        import aws_sdk_kendra.types.experience_configuration

        out["Configuration"] = (
            aws_sdk_kendra.types.experience_configuration.serialize_aws_json_1_1(
                value["configuration"]
            )
        )
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateExperienceRequest:
    out: UpdateExperienceRequest = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("UpdateExperienceRequest.id required")
    if "Name" in data:
        out["name"] = data["Name"]
    if "IndexId" in data:
        out["index_id"] = data["IndexId"]
    else:
        raise DeserializationError("UpdateExperienceRequest.index_id required")
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    if "Configuration" in data:
        import aws_sdk_kendra.types.experience_configuration

        out["configuration"] = (
            aws_sdk_kendra.types.experience_configuration.deserialize_aws_json_1_1(
                data["Configuration"]
            )
        )
    if "Description" in data:
        out["description"] = data["Description"]
    return out
