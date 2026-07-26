"""Generated from Smithy shape ``com.amazonaws.sagemaker#CompilationJobSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.compilation_job_arn
    import capo_sagemaker.types.compilation_job_status
    import capo_sagemaker.types.creation_time
    import capo_sagemaker.types.entity_name
    import capo_sagemaker.types.last_modified_time
    import capo_sagemaker.types.target_device
    import capo_sagemaker.types.target_platform_accelerator
    import capo_sagemaker.types.target_platform_arch
    import capo_sagemaker.types.target_platform_os
    import capo_sagemaker.types.timestamp


class CompilationJobSummary(TypedDict, closed=True):
    compilation_job_name: NotRequired["capo_sagemaker.types.entity_name.EntityName"]
    """<p>The name of the model compilation job that you want a summary for.</p>"""
    compilation_job_arn: NotRequired[
        "capo_sagemaker.types.compilation_job_arn.CompilationJobArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the model compilation job.</p>"""
    creation_time: NotRequired["capo_sagemaker.types.creation_time.CreationTime"]
    """<p>The time when the model compilation job was created.</p>"""
    compilation_start_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The time when the model compilation job started.</p>"""
    compilation_end_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The time when the model compilation job completed.</p>"""
    compilation_target_device: NotRequired[
        "capo_sagemaker.types.target_device.TargetDevice"
    ]
    """<p>The type of device that the model will run on after the compilation job has completed.</p>"""
    compilation_target_platform_os: NotRequired[
        "capo_sagemaker.types.target_platform_os.TargetPlatformOs"
    ]
    """<p>The type of OS that the model will run on after the compilation job has completed.</p>"""
    compilation_target_platform_arch: NotRequired[
        "capo_sagemaker.types.target_platform_arch.TargetPlatformArch"
    ]
    """<p>The type of architecture that the model will run on after the compilation job has completed.</p>"""
    compilation_target_platform_accelerator: NotRequired[
        "capo_sagemaker.types.target_platform_accelerator.TargetPlatformAccelerator"
    ]
    """<p>The type of accelerator that the model will run on after the compilation job has completed.</p>"""
    last_modified_time: NotRequired[
        "capo_sagemaker.types.last_modified_time.LastModifiedTime"
    ]
    """<p>The time when the model compilation job was last modified.</p>"""
    compilation_job_status: NotRequired[
        "capo_sagemaker.types.compilation_job_status.CompilationJobStatus"
    ]
    """<p>The status of the model compilation job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CompilationJobSummary) -> dict:
    out: dict = {}
    if "compilation_job_name" in value:
        out["CompilationJobName"] = value["compilation_job_name"]
    if "compilation_job_arn" in value:
        out["CompilationJobArn"] = value["compilation_job_arn"]
    if "creation_time" in value:
        import capo_sagemaker.types.creation_time

        out["CreationTime"] = capo_sagemaker.types.creation_time.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "compilation_start_time" in value:
        import capo_sagemaker.types.timestamp

        out["CompilationStartTime"] = (
            capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["compilation_start_time"]
            )
        )
    if "compilation_end_time" in value:
        import capo_sagemaker.types.timestamp

        out["CompilationEndTime"] = (
            capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["compilation_end_time"]
            )
        )
    if "compilation_target_device" in value:
        import capo_sagemaker.types.target_device

        out["CompilationTargetDevice"] = (
            capo_sagemaker.types.target_device.serialize_aws_json_1_1(
                value["compilation_target_device"]
            )
        )
    if "compilation_target_platform_os" in value:
        import capo_sagemaker.types.target_platform_os

        out["CompilationTargetPlatformOs"] = (
            capo_sagemaker.types.target_platform_os.serialize_aws_json_1_1(
                value["compilation_target_platform_os"]
            )
        )
    if "compilation_target_platform_arch" in value:
        import capo_sagemaker.types.target_platform_arch

        out["CompilationTargetPlatformArch"] = (
            capo_sagemaker.types.target_platform_arch.serialize_aws_json_1_1(
                value["compilation_target_platform_arch"]
            )
        )
    if "compilation_target_platform_accelerator" in value:
        import capo_sagemaker.types.target_platform_accelerator

        out["CompilationTargetPlatformAccelerator"] = (
            capo_sagemaker.types.target_platform_accelerator.serialize_aws_json_1_1(
                value["compilation_target_platform_accelerator"]
            )
        )
    if "last_modified_time" in value:
        import capo_sagemaker.types.last_modified_time

        out["LastModifiedTime"] = (
            capo_sagemaker.types.last_modified_time.serialize_aws_json_1_1(
                value["last_modified_time"]
            )
        )
    if "compilation_job_status" in value:
        import capo_sagemaker.types.compilation_job_status

        out["CompilationJobStatus"] = (
            capo_sagemaker.types.compilation_job_status.serialize_aws_json_1_1(
                value["compilation_job_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CompilationJobSummary:
    out: CompilationJobSummary = {}  # type: ignore[typeddict-item]
    if "CompilationJobName" in data:
        out["compilation_job_name"] = data["CompilationJobName"]
    if "CompilationJobArn" in data:
        out["compilation_job_arn"] = data["CompilationJobArn"]
    if "CreationTime" in data:
        import capo_sagemaker.types.creation_time

        out["creation_time"] = (
            capo_sagemaker.types.creation_time.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if "CompilationStartTime" in data:
        import capo_sagemaker.types.timestamp

        out["compilation_start_time"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CompilationStartTime"]
            )
        )
    if "CompilationEndTime" in data:
        import capo_sagemaker.types.timestamp

        out["compilation_end_time"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CompilationEndTime"]
            )
        )
    if "CompilationTargetDevice" in data:
        import capo_sagemaker.types.target_device

        out["compilation_target_device"] = (
            capo_sagemaker.types.target_device.deserialize_aws_json_1_1(
                data["CompilationTargetDevice"]
            )
        )
    if "CompilationTargetPlatformOs" in data:
        import capo_sagemaker.types.target_platform_os

        out["compilation_target_platform_os"] = (
            capo_sagemaker.types.target_platform_os.deserialize_aws_json_1_1(
                data["CompilationTargetPlatformOs"]
            )
        )
    if "CompilationTargetPlatformArch" in data:
        import capo_sagemaker.types.target_platform_arch

        out["compilation_target_platform_arch"] = (
            capo_sagemaker.types.target_platform_arch.deserialize_aws_json_1_1(
                data["CompilationTargetPlatformArch"]
            )
        )
    if "CompilationTargetPlatformAccelerator" in data:
        import capo_sagemaker.types.target_platform_accelerator

        out["compilation_target_platform_accelerator"] = (
            capo_sagemaker.types.target_platform_accelerator.deserialize_aws_json_1_1(
                data["CompilationTargetPlatformAccelerator"]
            )
        )
    if "LastModifiedTime" in data:
        import capo_sagemaker.types.last_modified_time

        out["last_modified_time"] = (
            capo_sagemaker.types.last_modified_time.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if "CompilationJobStatus" in data:
        import capo_sagemaker.types.compilation_job_status

        out["compilation_job_status"] = (
            capo_sagemaker.types.compilation_job_status.deserialize_aws_json_1_1(
                data["CompilationJobStatus"]
            )
        )
    return out
