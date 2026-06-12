"""Generated from Smithy shape ``com.amazonaws.rekognition#ProjectDescription``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.customization_feature
    import aws_sdk_rekognition.types.dataset_metadata_list
    import aws_sdk_rekognition.types.date_time
    import aws_sdk_rekognition.types.project_arn
    import aws_sdk_rekognition.types.project_auto_update
    import aws_sdk_rekognition.types.project_status


class ProjectDescription(TypedDict):
    project_arn: NotRequired["aws_sdk_rekognition.types.project_arn.ProjectArn"]
    """<p>The Amazon Resource Name (ARN) of the project.</p>"""
    creation_timestamp: NotRequired["aws_sdk_rekognition.types.date_time.DateTime"]
    """<p>The Unix timestamp for the date and time that the project was created.</p>"""
    status: NotRequired["aws_sdk_rekognition.types.project_status.ProjectStatus"]
    """<p>The current status of the project.</p>"""
    datasets: NotRequired[
        "aws_sdk_rekognition.types.dataset_metadata_list.DatasetMetadataList"
    ]
    """<p> Information about the training and test datasets in the project. </p>"""
    feature: NotRequired[
        "aws_sdk_rekognition.types.customization_feature.CustomizationFeature"
    ]
    """<p>Specifies the project that is being customized.</p>"""
    auto_update: NotRequired[
        "aws_sdk_rekognition.types.project_auto_update.ProjectAutoUpdate"
    ]
    """<p>Indicates whether automatic retraining will be attempted for the versions of the project. Applies only to adapters. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProjectDescription) -> dict:
    out: dict = {}
    if "project_arn" in value:
        out["ProjectArn"] = value["project_arn"]
    if "creation_timestamp" in value:
        import aws_sdk_rekognition.types.date_time

        out["CreationTimestamp"] = (
            aws_sdk_rekognition.types.date_time.serialize_aws_json_1_1(
                value["creation_timestamp"]
            )
        )
    if "status" in value:
        import aws_sdk_rekognition.types.project_status

        out["Status"] = aws_sdk_rekognition.types.project_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "datasets" in value:
        import aws_sdk_rekognition.types.dataset_metadata_list

        out["Datasets"] = (
            aws_sdk_rekognition.types.dataset_metadata_list.serialize_aws_json_1_1(
                value["datasets"]
            )
        )
    if "feature" in value:
        import aws_sdk_rekognition.types.customization_feature

        out["Feature"] = (
            aws_sdk_rekognition.types.customization_feature.serialize_aws_json_1_1(
                value["feature"]
            )
        )
    if "auto_update" in value:
        import aws_sdk_rekognition.types.project_auto_update

        out["AutoUpdate"] = (
            aws_sdk_rekognition.types.project_auto_update.serialize_aws_json_1_1(
                value["auto_update"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ProjectDescription:
    out: ProjectDescription = {}  # type: ignore[typeddict-item]
    if "ProjectArn" in data:
        out["project_arn"] = data["ProjectArn"]
    if "CreationTimestamp" in data:
        import aws_sdk_rekognition.types.date_time

        out["creation_timestamp"] = (
            aws_sdk_rekognition.types.date_time.deserialize_aws_json_1_1(
                data["CreationTimestamp"]
            )
        )
    if "Status" in data:
        import aws_sdk_rekognition.types.project_status

        out["status"] = (
            aws_sdk_rekognition.types.project_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "Datasets" in data:
        import aws_sdk_rekognition.types.dataset_metadata_list

        out["datasets"] = (
            aws_sdk_rekognition.types.dataset_metadata_list.deserialize_aws_json_1_1(
                data["Datasets"]
            )
        )
    if "Feature" in data:
        import aws_sdk_rekognition.types.customization_feature

        out["feature"] = (
            aws_sdk_rekognition.types.customization_feature.deserialize_aws_json_1_1(
                data["Feature"]
            )
        )
    if "AutoUpdate" in data:
        import aws_sdk_rekognition.types.project_auto_update

        out["auto_update"] = (
            aws_sdk_rekognition.types.project_auto_update.deserialize_aws_json_1_1(
                data["AutoUpdate"]
            )
        )
    return out
