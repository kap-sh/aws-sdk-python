"""Generated from Smithy shape ``com.amazonaws.sagemaker#QualityCheckStepMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.boolean
    import aws_sdk_sagemaker.types.string256
    import aws_sdk_sagemaker.types.string1024


class QualityCheckStepMetadata(TypedDict, closed=True):
    check_type: NotRequired["aws_sdk_sagemaker.types.string256.String256"]
    """<p>The type of the Quality check step.</p>"""
    baseline_used_for_drift_check_statistics: NotRequired[
        "aws_sdk_sagemaker.types.string1024.String1024"
    ]
    """<p>The Amazon S3 URI of the baseline statistics file used for the drift check.</p>"""
    baseline_used_for_drift_check_constraints: NotRequired[
        "aws_sdk_sagemaker.types.string1024.String1024"
    ]
    """<p>The Amazon S3 URI of the baseline constraints file used for the drift check.</p>"""
    calculated_baseline_statistics: NotRequired[
        "aws_sdk_sagemaker.types.string1024.String1024"
    ]
    """<p>The Amazon S3 URI of the newly calculated baseline statistics file.</p>"""
    calculated_baseline_constraints: NotRequired[
        "aws_sdk_sagemaker.types.string1024.String1024"
    ]
    """<p>The Amazon S3 URI of the newly calculated baseline constraints file.</p>"""
    model_package_group_name: NotRequired["aws_sdk_sagemaker.types.string256.String256"]
    """<p>The model package group name.</p>"""
    violation_report: NotRequired["aws_sdk_sagemaker.types.string1024.String1024"]
    """<p>The Amazon S3 URI of violation report if violations are detected.</p>"""
    check_job_arn: NotRequired["aws_sdk_sagemaker.types.string256.String256"]
    """<p>The Amazon Resource Name (ARN) of the Quality check processing job that was run by this step execution.</p>"""
    skip_check: NotRequired["aws_sdk_sagemaker.types.boolean.Boolean"]
    """<p>This flag indicates if the drift check against the previous baseline will be skipped or not. If it is set to <code>False</code>, the previous baseline of the configured check type must be available.</p>"""
    register_new_baseline: NotRequired["aws_sdk_sagemaker.types.boolean.Boolean"]
    """<p>This flag indicates if a newly calculated baseline can be accessed through step properties <code>BaselineUsedForDriftCheckConstraints</code> and <code>BaselineUsedForDriftCheckStatistics</code>. If it is set to <code>False</code>, the previous baseline of the configured check type must also be available. These can be accessed through the <code>BaselineUsedForDriftCheckConstraints</code> and <code> BaselineUsedForDriftCheckStatistics</code> properties. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QualityCheckStepMetadata) -> dict:
    out: dict = {}
    if "check_type" in value:
        out["CheckType"] = value["check_type"]
    if "baseline_used_for_drift_check_statistics" in value:
        out["BaselineUsedForDriftCheckStatistics"] = value[
            "baseline_used_for_drift_check_statistics"
        ]
    if "baseline_used_for_drift_check_constraints" in value:
        out["BaselineUsedForDriftCheckConstraints"] = value[
            "baseline_used_for_drift_check_constraints"
        ]
    if "calculated_baseline_statistics" in value:
        out["CalculatedBaselineStatistics"] = value["calculated_baseline_statistics"]
    if "calculated_baseline_constraints" in value:
        out["CalculatedBaselineConstraints"] = value["calculated_baseline_constraints"]
    if "model_package_group_name" in value:
        out["ModelPackageGroupName"] = value["model_package_group_name"]
    if "violation_report" in value:
        out["ViolationReport"] = value["violation_report"]
    if "check_job_arn" in value:
        out["CheckJobArn"] = value["check_job_arn"]
    if "skip_check" in value:
        out["SkipCheck"] = value["skip_check"]
    if "register_new_baseline" in value:
        out["RegisterNewBaseline"] = value["register_new_baseline"]
    return out


def deserialize_aws_json_1_1(data: dict) -> QualityCheckStepMetadata:
    out: QualityCheckStepMetadata = {}  # type: ignore[typeddict-item]
    if "CheckType" in data:
        out["check_type"] = data["CheckType"]
    if "BaselineUsedForDriftCheckStatistics" in data:
        out["baseline_used_for_drift_check_statistics"] = data[
            "BaselineUsedForDriftCheckStatistics"
        ]
    if "BaselineUsedForDriftCheckConstraints" in data:
        out["baseline_used_for_drift_check_constraints"] = data[
            "BaselineUsedForDriftCheckConstraints"
        ]
    if "CalculatedBaselineStatistics" in data:
        out["calculated_baseline_statistics"] = data["CalculatedBaselineStatistics"]
    if "CalculatedBaselineConstraints" in data:
        out["calculated_baseline_constraints"] = data["CalculatedBaselineConstraints"]
    if "ModelPackageGroupName" in data:
        out["model_package_group_name"] = data["ModelPackageGroupName"]
    if "ViolationReport" in data:
        out["violation_report"] = data["ViolationReport"]
    if "CheckJobArn" in data:
        out["check_job_arn"] = data["CheckJobArn"]
    if "SkipCheck" in data:
        out["skip_check"] = data["SkipCheck"]
    if "RegisterNewBaseline" in data:
        out["register_new_baseline"] = data["RegisterNewBaseline"]
    return out
