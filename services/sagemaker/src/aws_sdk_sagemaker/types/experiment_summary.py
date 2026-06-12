"""Generated from Smithy shape ``com.amazonaws.sagemaker#ExperimentSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.experiment_arn
    import aws_sdk_sagemaker.types.experiment_entity_name
    import aws_sdk_sagemaker.types.experiment_source
    import aws_sdk_sagemaker.types.timestamp


class ExperimentSummary(TypedDict):
    experiment_arn: NotRequired["aws_sdk_sagemaker.types.experiment_arn.ExperimentArn"]
    """<p>The Amazon Resource Name (ARN) of the experiment.</p>"""
    experiment_name: NotRequired[
        "aws_sdk_sagemaker.types.experiment_entity_name.ExperimentEntityName"
    ]
    """<p>The name of the experiment.</p>"""
    display_name: NotRequired[
        "aws_sdk_sagemaker.types.experiment_entity_name.ExperimentEntityName"
    ]
    """<p>The name of the experiment as displayed. If <code>DisplayName</code> isn't specified, <code>ExperimentName</code> is displayed.</p>"""
    experiment_source: NotRequired[
        "aws_sdk_sagemaker.types.experiment_source.ExperimentSource"
    ]
    creation_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>When the experiment was created.</p>"""
    last_modified_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>When the experiment was last modified.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExperimentSummary) -> dict:
    out: dict = {}
    if "experiment_arn" in value:
        out["ExperimentArn"] = value["experiment_arn"]
    if "experiment_name" in value:
        out["ExperimentName"] = value["experiment_name"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "experiment_source" in value:
        import aws_sdk_sagemaker.types.experiment_source

        out["ExperimentSource"] = (
            aws_sdk_sagemaker.types.experiment_source.serialize_aws_json_1_1(
                value["experiment_source"]
            )
        )
    if "creation_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["CreationTime"] = aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "last_modified_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["LastModifiedTime"] = (
            aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["last_modified_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ExperimentSummary:
    out: ExperimentSummary = {}  # type: ignore[typeddict-item]
    if "ExperimentArn" in data:
        out["experiment_arn"] = data["ExperimentArn"]
    if "ExperimentName" in data:
        out["experiment_name"] = data["ExperimentName"]
    if "DisplayName" in data:
        out["display_name"] = data["DisplayName"]
    if "ExperimentSource" in data:
        import aws_sdk_sagemaker.types.experiment_source

        out["experiment_source"] = (
            aws_sdk_sagemaker.types.experiment_source.deserialize_aws_json_1_1(
                data["ExperimentSource"]
            )
        )
    if "CreationTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["creation_time"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if "LastModifiedTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["last_modified_time"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    return out
