"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeImageVersionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.failure_reason
    import aws_sdk_sagemaker.types.horovod
    import aws_sdk_sagemaker.types.image_arn
    import aws_sdk_sagemaker.types.image_base_image
    import aws_sdk_sagemaker.types.image_container_image
    import aws_sdk_sagemaker.types.image_version_arn
    import aws_sdk_sagemaker.types.image_version_number
    import aws_sdk_sagemaker.types.image_version_status
    import aws_sdk_sagemaker.types.job_type
    import aws_sdk_sagemaker.types.ml_framework
    import aws_sdk_sagemaker.types.processor
    import aws_sdk_sagemaker.types.programming_lang
    import aws_sdk_sagemaker.types.release_notes
    import aws_sdk_sagemaker.types.timestamp
    import aws_sdk_sagemaker.types.vendor_guidance


class DescribeImageVersionResponse(TypedDict):
    base_image: NotRequired["aws_sdk_sagemaker.types.image_base_image.ImageBaseImage"]
    """<p>The registry path of the container image on which this image version is based.</p>"""
    container_image: NotRequired[
        "aws_sdk_sagemaker.types.image_container_image.ImageContainerImage"
    ]
    """<p>The registry path of the container image that contains this image version.</p>"""
    creation_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>When the version was created.</p>"""
    failure_reason: NotRequired["aws_sdk_sagemaker.types.failure_reason.FailureReason"]
    """<p>When a create or delete operation fails, the reason for the failure.</p>"""
    image_arn: NotRequired["aws_sdk_sagemaker.types.image_arn.ImageArn"]
    """<p>The ARN of the image the version is based on.</p>"""
    image_version_arn: NotRequired[
        "aws_sdk_sagemaker.types.image_version_arn.ImageVersionArn"
    ]
    """<p>The ARN of the version.</p>"""
    image_version_status: NotRequired[
        "aws_sdk_sagemaker.types.image_version_status.ImageVersionStatus"
    ]
    """<p>The status of the version.</p>"""
    last_modified_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>When the version was last modified.</p>"""
    version: NotRequired[
        "aws_sdk_sagemaker.types.image_version_number.ImageVersionNumber"
    ]
    """<p>The version number.</p>"""
    vendor_guidance: NotRequired[
        "aws_sdk_sagemaker.types.vendor_guidance.VendorGuidance"
    ]
    """<p>The stability of the image version specified by the maintainer.</p> <ul> <li> <p> <code>NOT_PROVIDED</code>: The maintainers did not provide a status for image version stability.</p> </li> <li> <p> <code>STABLE</code>: The image version is stable.</p> </li> <li> <p> <code>TO_BE_ARCHIVED</code>: The image version is set to be archived. Custom image versions that are set to be archived are automatically archived after three months.</p> </li> <li> <p> <code>ARCHIVED</code>: The image version is archived. Archived image versions are not searchable and are no longer actively supported. </p> </li> </ul>"""
    job_type: NotRequired["aws_sdk_sagemaker.types.job_type.JobType"]
    """<p>Indicates SageMaker AI job type compatibility.</p> <ul> <li> <p> <code>TRAINING</code>: The image version is compatible with SageMaker AI training jobs.</p> </li> <li> <p> <code>INFERENCE</code>: The image version is compatible with SageMaker AI inference jobs.</p> </li> <li> <p> <code>NOTEBOOK_KERNEL</code>: The image version is compatible with SageMaker AI notebook kernels.</p> </li> </ul>"""
    ml_framework: NotRequired["aws_sdk_sagemaker.types.ml_framework.MLFramework"]
    """<p>The machine learning framework vended in the image version.</p>"""
    programming_lang: NotRequired[
        "aws_sdk_sagemaker.types.programming_lang.ProgrammingLang"
    ]
    """<p>The supported programming language and its version.</p>"""
    processor: NotRequired["aws_sdk_sagemaker.types.processor.Processor"]
    """<p>Indicates CPU or GPU compatibility.</p> <ul> <li> <p> <code>CPU</code>: The image version is compatible with CPU.</p> </li> <li> <p> <code>GPU</code>: The image version is compatible with GPU.</p> </li> </ul>"""
    horovod: NotRequired["aws_sdk_sagemaker.types.horovod.Horovod"]
    """<p>Indicates Horovod compatibility.</p>"""
    release_notes: NotRequired["aws_sdk_sagemaker.types.release_notes.ReleaseNotes"]
    """<p>The maintainer description of the image version.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeImageVersionResponse) -> dict:
    out: dict = {}
    if "base_image" in value:
        out["BaseImage"] = value["base_image"]
    if "container_image" in value:
        out["ContainerImage"] = value["container_image"]
    if "creation_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["CreationTime"] = aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    if "image_arn" in value:
        out["ImageArn"] = value["image_arn"]
    if "image_version_arn" in value:
        out["ImageVersionArn"] = value["image_version_arn"]
    if "image_version_status" in value:
        import aws_sdk_sagemaker.types.image_version_status

        out["ImageVersionStatus"] = (
            aws_sdk_sagemaker.types.image_version_status.serialize_aws_json_1_1(
                value["image_version_status"]
            )
        )
    if "last_modified_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["LastModifiedTime"] = (
            aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["last_modified_time"]
            )
        )
    if "version" in value:
        out["Version"] = value["version"]
    if "vendor_guidance" in value:
        import aws_sdk_sagemaker.types.vendor_guidance

        out["VendorGuidance"] = (
            aws_sdk_sagemaker.types.vendor_guidance.serialize_aws_json_1_1(
                value["vendor_guidance"]
            )
        )
    if "job_type" in value:
        import aws_sdk_sagemaker.types.job_type

        out["JobType"] = aws_sdk_sagemaker.types.job_type.serialize_aws_json_1_1(
            value["job_type"]
        )
    if "ml_framework" in value:
        out["MLFramework"] = value["ml_framework"]
    if "programming_lang" in value:
        out["ProgrammingLang"] = value["programming_lang"]
    if "processor" in value:
        import aws_sdk_sagemaker.types.processor

        out["Processor"] = aws_sdk_sagemaker.types.processor.serialize_aws_json_1_1(
            value["processor"]
        )
    if "horovod" in value:
        out["Horovod"] = value["horovod"]
    if "release_notes" in value:
        out["ReleaseNotes"] = value["release_notes"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeImageVersionResponse:
    out: DescribeImageVersionResponse = {}  # type: ignore[typeddict-item]
    if "BaseImage" in data:
        out["base_image"] = data["BaseImage"]
    if "ContainerImage" in data:
        out["container_image"] = data["ContainerImage"]
    if "CreationTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["creation_time"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if "FailureReason" in data:
        out["failure_reason"] = data["FailureReason"]
    if "ImageArn" in data:
        out["image_arn"] = data["ImageArn"]
    if "ImageVersionArn" in data:
        out["image_version_arn"] = data["ImageVersionArn"]
    if "ImageVersionStatus" in data:
        import aws_sdk_sagemaker.types.image_version_status

        out["image_version_status"] = (
            aws_sdk_sagemaker.types.image_version_status.deserialize_aws_json_1_1(
                data["ImageVersionStatus"]
            )
        )
    if "LastModifiedTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["last_modified_time"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if "Version" in data:
        out["version"] = data["Version"]
    if "VendorGuidance" in data:
        import aws_sdk_sagemaker.types.vendor_guidance

        out["vendor_guidance"] = (
            aws_sdk_sagemaker.types.vendor_guidance.deserialize_aws_json_1_1(
                data["VendorGuidance"]
            )
        )
    if "JobType" in data:
        import aws_sdk_sagemaker.types.job_type

        out["job_type"] = aws_sdk_sagemaker.types.job_type.deserialize_aws_json_1_1(
            data["JobType"]
        )
    if "MLFramework" in data:
        out["ml_framework"] = data["MLFramework"]
    if "ProgrammingLang" in data:
        out["programming_lang"] = data["ProgrammingLang"]
    if "Processor" in data:
        import aws_sdk_sagemaker.types.processor

        out["processor"] = aws_sdk_sagemaker.types.processor.deserialize_aws_json_1_1(
            data["Processor"]
        )
    if "Horovod" in data:
        out["horovod"] = data["Horovod"]
    if "ReleaseNotes" in data:
        out["release_notes"] = data["ReleaseNotes"]
    return out
