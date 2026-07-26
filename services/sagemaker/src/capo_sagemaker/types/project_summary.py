"""Generated from Smithy shape ``com.amazonaws.sagemaker#ProjectSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.entity_description
    import capo_sagemaker.types.project_arn
    import capo_sagemaker.types.project_entity_name
    import capo_sagemaker.types.project_id
    import capo_sagemaker.types.project_status
    import capo_sagemaker.types.timestamp


class ProjectSummary(TypedDict, closed=True):
    project_name: NotRequired[
        "capo_sagemaker.types.project_entity_name.ProjectEntityName"
    ]
    """<p>The name of the project.</p>"""
    project_description: NotRequired[
        "capo_sagemaker.types.entity_description.EntityDescription"
    ]
    """<p>The description of the project.</p>"""
    project_arn: NotRequired["capo_sagemaker.types.project_arn.ProjectArn"]
    """<p>The Amazon Resource Name (ARN) of the project.</p>"""
    project_id: NotRequired["capo_sagemaker.types.project_id.ProjectId"]
    """<p>The ID of the project.</p>"""
    creation_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The time that the project was created.</p>"""
    project_status: NotRequired["capo_sagemaker.types.project_status.ProjectStatus"]
    """<p>The status of the project.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProjectSummary) -> dict:
    out: dict = {}
    if "project_name" in value:
        out["ProjectName"] = value["project_name"]
    if "project_description" in value:
        out["ProjectDescription"] = value["project_description"]
    if "project_arn" in value:
        out["ProjectArn"] = value["project_arn"]
    if "project_id" in value:
        out["ProjectId"] = value["project_id"]
    if "creation_time" in value:
        import capo_sagemaker.types.timestamp

        out["CreationTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "project_status" in value:
        import capo_sagemaker.types.project_status

        out["ProjectStatus"] = (
            capo_sagemaker.types.project_status.serialize_aws_json_1_1(
                value["project_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ProjectSummary:
    out: ProjectSummary = {}  # type: ignore[typeddict-item]
    if "ProjectName" in data:
        out["project_name"] = data["ProjectName"]
    if "ProjectDescription" in data:
        out["project_description"] = data["ProjectDescription"]
    if "ProjectArn" in data:
        out["project_arn"] = data["ProjectArn"]
    if "ProjectId" in data:
        out["project_id"] = data["ProjectId"]
    if "CreationTime" in data:
        import capo_sagemaker.types.timestamp

        out["creation_time"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if "ProjectStatus" in data:
        import capo_sagemaker.types.project_status

        out["project_status"] = (
            capo_sagemaker.types.project_status.deserialize_aws_json_1_1(
                data["ProjectStatus"]
            )
        )
    return out
