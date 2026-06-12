"""Generated from Smithy shape ``com.amazonaws.sagemaker#TrialSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.experiment_entity_name
    import aws_sdk_sagemaker.types.timestamp
    import aws_sdk_sagemaker.types.trial_arn
    import aws_sdk_sagemaker.types.trial_source


class TrialSummary(TypedDict):
    trial_arn: NotRequired["aws_sdk_sagemaker.types.trial_arn.TrialArn"]
    """<p>The Amazon Resource Name (ARN) of the trial.</p>"""
    trial_name: NotRequired[
        "aws_sdk_sagemaker.types.experiment_entity_name.ExperimentEntityName"
    ]
    """<p>The name of the trial.</p>"""
    display_name: NotRequired[
        "aws_sdk_sagemaker.types.experiment_entity_name.ExperimentEntityName"
    ]
    """<p>The name of the trial as displayed. If <code>DisplayName</code> isn't specified, <code>TrialName</code> is displayed.</p>"""
    trial_source: NotRequired["aws_sdk_sagemaker.types.trial_source.TrialSource"]
    creation_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>When the trial was created.</p>"""
    last_modified_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>When the trial was last modified.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrialSummary) -> dict:
    out: dict = {}
    if "trial_arn" in value:
        out["TrialArn"] = value["trial_arn"]
    if "trial_name" in value:
        out["TrialName"] = value["trial_name"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "trial_source" in value:
        import aws_sdk_sagemaker.types.trial_source

        out["TrialSource"] = (
            aws_sdk_sagemaker.types.trial_source.serialize_aws_json_1_1(
                value["trial_source"]
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


def deserialize_aws_json_1_1(data: dict) -> TrialSummary:
    out: TrialSummary = {}  # type: ignore[typeddict-item]
    if "TrialArn" in data:
        out["trial_arn"] = data["TrialArn"]
    if "TrialName" in data:
        out["trial_name"] = data["TrialName"]
    if "DisplayName" in data:
        out["display_name"] = data["DisplayName"]
    if "TrialSource" in data:
        import aws_sdk_sagemaker.types.trial_source

        out["trial_source"] = (
            aws_sdk_sagemaker.types.trial_source.deserialize_aws_json_1_1(
                data["TrialSource"]
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
