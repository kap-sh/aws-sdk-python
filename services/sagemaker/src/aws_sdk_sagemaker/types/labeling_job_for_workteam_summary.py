"""Generated from Smithy shape ``com.amazonaws.sagemaker#LabelingJobForWorkteamSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.account_id
    import aws_sdk_sagemaker.types.job_reference_code
    import aws_sdk_sagemaker.types.label_counters_for_workteam
    import aws_sdk_sagemaker.types.labeling_job_name
    import aws_sdk_sagemaker.types.number_of_human_workers_per_data_object
    import aws_sdk_sagemaker.types.timestamp


class LabelingJobForWorkteamSummary(TypedDict, closed=True):
    labeling_job_name: NotRequired[
        "aws_sdk_sagemaker.types.labeling_job_name.LabelingJobName"
    ]
    """<p>The name of the labeling job that the work team is assigned to.</p>"""
    job_reference_code: NotRequired[
        "aws_sdk_sagemaker.types.job_reference_code.JobReferenceCode"
    ]
    """<p>A unique identifier for a labeling job. You can use this to refer to a specific labeling job.</p>"""
    work_requester_account_id: NotRequired[
        "aws_sdk_sagemaker.types.account_id.AccountId"
    ]
    """<p>The Amazon Web Services account ID of the account used to start the labeling job.</p>"""
    creation_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>The date and time that the labeling job was created.</p>"""
    label_counters: NotRequired[
        "aws_sdk_sagemaker.types.label_counters_for_workteam.LabelCountersForWorkteam"
    ]
    """<p>Provides information about the progress of a labeling job.</p>"""
    number_of_human_workers_per_data_object: NotRequired[
        "aws_sdk_sagemaker.types.number_of_human_workers_per_data_object.NumberOfHumanWorkersPerDataObject"
    ]
    """<p>The configured number of workers per data object.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LabelingJobForWorkteamSummary) -> dict:
    out: dict = {}
    if "labeling_job_name" in value:
        out["LabelingJobName"] = value["labeling_job_name"]
    if "job_reference_code" in value:
        out["JobReferenceCode"] = value["job_reference_code"]
    if "work_requester_account_id" in value:
        out["WorkRequesterAccountId"] = value["work_requester_account_id"]
    if "creation_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["CreationTime"] = aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "label_counters" in value:
        import aws_sdk_sagemaker.types.label_counters_for_workteam

        out["LabelCounters"] = (
            aws_sdk_sagemaker.types.label_counters_for_workteam.serialize_aws_json_1_1(
                value["label_counters"]
            )
        )
    if "number_of_human_workers_per_data_object" in value:
        out["NumberOfHumanWorkersPerDataObject"] = value[
            "number_of_human_workers_per_data_object"
        ]
    return out


def deserialize_aws_json_1_1(data: dict) -> LabelingJobForWorkteamSummary:
    out: LabelingJobForWorkteamSummary = {}  # type: ignore[typeddict-item]
    if "LabelingJobName" in data:
        out["labeling_job_name"] = data["LabelingJobName"]
    if "JobReferenceCode" in data:
        out["job_reference_code"] = data["JobReferenceCode"]
    if "WorkRequesterAccountId" in data:
        out["work_requester_account_id"] = data["WorkRequesterAccountId"]
    if "CreationTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["creation_time"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if "LabelCounters" in data:
        import aws_sdk_sagemaker.types.label_counters_for_workteam

        out["label_counters"] = (
            aws_sdk_sagemaker.types.label_counters_for_workteam.deserialize_aws_json_1_1(
                data["LabelCounters"]
            )
        )
    if "NumberOfHumanWorkersPerDataObject" in data:
        out["number_of_human_workers_per_data_object"] = data[
            "NumberOfHumanWorkersPerDataObject"
        ]
    return out
