"""Generated from Smithy shape ``com.amazonaws.sagemaker#TrialComponentSourceDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.processing_job
    import capo_sagemaker.types.training_job
    import capo_sagemaker.types.transform_job
    import capo_sagemaker.types.trial_component_source_arn


class TrialComponentSourceDetail(TypedDict, closed=True):
    source_arn: NotRequired[
        "capo_sagemaker.types.trial_component_source_arn.TrialComponentSourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the source.</p>"""
    training_job: NotRequired["capo_sagemaker.types.training_job.TrainingJob"]
    """<p>Information about a training job that's the source of a trial component.</p>"""
    processing_job: NotRequired["capo_sagemaker.types.processing_job.ProcessingJob"]
    """<p>Information about a processing job that's the source of a trial component.</p>"""
    transform_job: NotRequired["capo_sagemaker.types.transform_job.TransformJob"]
    """<p>Information about a transform job that's the source of a trial component.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrialComponentSourceDetail) -> dict:
    out: dict = {}
    if "source_arn" in value:
        out["SourceArn"] = value["source_arn"]
    if "training_job" in value:
        import capo_sagemaker.types.training_job

        out["TrainingJob"] = capo_sagemaker.types.training_job.serialize_aws_json_1_1(
            value["training_job"]
        )
    if "processing_job" in value:
        import capo_sagemaker.types.processing_job

        out["ProcessingJob"] = (
            capo_sagemaker.types.processing_job.serialize_aws_json_1_1(
                value["processing_job"]
            )
        )
    if "transform_job" in value:
        import capo_sagemaker.types.transform_job

        out["TransformJob"] = capo_sagemaker.types.transform_job.serialize_aws_json_1_1(
            value["transform_job"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TrialComponentSourceDetail:
    out: TrialComponentSourceDetail = {}  # type: ignore[typeddict-item]
    if "SourceArn" in data:
        out["source_arn"] = data["SourceArn"]
    if "TrainingJob" in data:
        import capo_sagemaker.types.training_job

        out["training_job"] = (
            capo_sagemaker.types.training_job.deserialize_aws_json_1_1(
                data["TrainingJob"]
            )
        )
    if "ProcessingJob" in data:
        import capo_sagemaker.types.processing_job

        out["processing_job"] = (
            capo_sagemaker.types.processing_job.deserialize_aws_json_1_1(
                data["ProcessingJob"]
            )
        )
    if "TransformJob" in data:
        import capo_sagemaker.types.transform_job

        out["transform_job"] = (
            capo_sagemaker.types.transform_job.deserialize_aws_json_1_1(
                data["TransformJob"]
            )
        )
    return out
