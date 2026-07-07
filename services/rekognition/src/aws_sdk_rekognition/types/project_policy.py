"""Generated from Smithy shape ``com.amazonaws.rekognition#ProjectPolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.date_time
    import aws_sdk_rekognition.types.project_arn
    import aws_sdk_rekognition.types.project_policy_document
    import aws_sdk_rekognition.types.project_policy_name
    import aws_sdk_rekognition.types.project_policy_revision_id


class ProjectPolicy(TypedDict, closed=True):
    project_arn: NotRequired["aws_sdk_rekognition.types.project_arn.ProjectArn"]
    """<p>The Amazon Resource Name (ARN) of the project to which the project policy is attached.</p>"""
    policy_name: NotRequired[
        "aws_sdk_rekognition.types.project_policy_name.ProjectPolicyName"
    ]
    """<p>The name of the project policy.</p>"""
    policy_revision_id: NotRequired[
        "aws_sdk_rekognition.types.project_policy_revision_id.ProjectPolicyRevisionId"
    ]
    """<p>The revision ID of the project policy.</p>"""
    policy_document: NotRequired[
        "aws_sdk_rekognition.types.project_policy_document.ProjectPolicyDocument"
    ]
    """<p>The JSON document for the project policy.</p>"""
    creation_timestamp: NotRequired["aws_sdk_rekognition.types.date_time.DateTime"]
    """<p>The Unix datetime for the creation of the project policy.</p>"""
    last_updated_timestamp: NotRequired["aws_sdk_rekognition.types.date_time.DateTime"]
    """<p>The Unix datetime for when the project policy was last updated. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProjectPolicy) -> dict:
    out: dict = {}
    if "project_arn" in value:
        out["ProjectArn"] = value["project_arn"]
    if "policy_name" in value:
        out["PolicyName"] = value["policy_name"]
    if "policy_revision_id" in value:
        out["PolicyRevisionId"] = value["policy_revision_id"]
    if "policy_document" in value:
        out["PolicyDocument"] = value["policy_document"]
    if "creation_timestamp" in value:
        import aws_sdk_rekognition.types.date_time

        out["CreationTimestamp"] = (
            aws_sdk_rekognition.types.date_time.serialize_aws_json_1_1(
                value["creation_timestamp"]
            )
        )
    if "last_updated_timestamp" in value:
        import aws_sdk_rekognition.types.date_time

        out["LastUpdatedTimestamp"] = (
            aws_sdk_rekognition.types.date_time.serialize_aws_json_1_1(
                value["last_updated_timestamp"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ProjectPolicy:
    out: ProjectPolicy = {}  # type: ignore[typeddict-item]
    if "ProjectArn" in data:
        out["project_arn"] = data["ProjectArn"]
    if "PolicyName" in data:
        out["policy_name"] = data["PolicyName"]
    if "PolicyRevisionId" in data:
        out["policy_revision_id"] = data["PolicyRevisionId"]
    if "PolicyDocument" in data:
        out["policy_document"] = data["PolicyDocument"]
    if "CreationTimestamp" in data:
        import aws_sdk_rekognition.types.date_time

        out["creation_timestamp"] = (
            aws_sdk_rekognition.types.date_time.deserialize_aws_json_1_1(
                data["CreationTimestamp"]
            )
        )
    if "LastUpdatedTimestamp" in data:
        import aws_sdk_rekognition.types.date_time

        out["last_updated_timestamp"] = (
            aws_sdk_rekognition.types.date_time.deserialize_aws_json_1_1(
                data["LastUpdatedTimestamp"]
            )
        )
    return out
