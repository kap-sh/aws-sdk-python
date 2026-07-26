"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateImageVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.client_token
    import capo_sagemaker.types.horovod
    import capo_sagemaker.types.image_base_image
    import capo_sagemaker.types.image_name
    import capo_sagemaker.types.job_type
    import capo_sagemaker.types.ml_framework
    import capo_sagemaker.types.processor
    import capo_sagemaker.types.programming_lang
    import capo_sagemaker.types.release_notes
    import capo_sagemaker.types.sage_maker_image_version_aliases
    import capo_sagemaker.types.vendor_guidance


class CreateImageVersionRequest(TypedDict, closed=True):
    base_image: NotRequired["capo_sagemaker.types.image_base_image.ImageBaseImage"]
    """<p>The registry path of the container image to use as the starting point for this version. The path is an Amazon ECR URI in the following format:</p> <p> <code>&lt;acct-id&gt;.dkr.ecr.&lt;region&gt;.amazonaws.com/&lt;repo-name[:tag] or [@digest]&gt;</code> </p>"""
    client_token: NotRequired["capo_sagemaker.types.client_token.ClientToken"]
    """<p>A unique ID. If not specified, the Amazon Web Services CLI and Amazon Web Services SDKs, such as the SDK for Python (Boto3), add a unique value to the call.</p>"""
    image_name: NotRequired["capo_sagemaker.types.image_name.ImageName"]
    """<p>The <code>ImageName</code> of the <code>Image</code> to create a version of.</p>"""
    aliases: NotRequired[
        "capo_sagemaker.types.sage_maker_image_version_aliases.SageMakerImageVersionAliases"
    ]
    """<p>A list of aliases created with the image version.</p>"""
    vendor_guidance: NotRequired["capo_sagemaker.types.vendor_guidance.VendorGuidance"]
    """<p>The stability of the image version, specified by the maintainer.</p> <ul> <li> <p> <code>NOT_PROVIDED</code>: The maintainers did not provide a status for image version stability.</p> </li> <li> <p> <code>STABLE</code>: The image version is stable.</p> </li> <li> <p> <code>TO_BE_ARCHIVED</code>: The image version is set to be archived. Custom image versions that are set to be archived are automatically archived after three months.</p> </li> <li> <p> <code>ARCHIVED</code>: The image version is archived. Archived image versions are not searchable and are no longer actively supported. </p> </li> </ul>"""
    job_type: NotRequired["capo_sagemaker.types.job_type.JobType"]
    """<p>Indicates SageMaker AI job type compatibility.</p> <ul> <li> <p> <code>TRAINING</code>: The image version is compatible with SageMaker AI training jobs.</p> </li> <li> <p> <code>INFERENCE</code>: The image version is compatible with SageMaker AI inference jobs.</p> </li> <li> <p> <code>NOTEBOOK_KERNEL</code>: The image version is compatible with SageMaker AI notebook kernels.</p> </li> </ul>"""
    ml_framework: NotRequired["capo_sagemaker.types.ml_framework.MLFramework"]
    """<p>The machine learning framework vended in the image version.</p>"""
    programming_lang: NotRequired[
        "capo_sagemaker.types.programming_lang.ProgrammingLang"
    ]
    """<p>The supported programming language and its version.</p>"""
    processor: NotRequired["capo_sagemaker.types.processor.Processor"]
    """<p>Indicates CPU or GPU compatibility.</p> <ul> <li> <p> <code>CPU</code>: The image version is compatible with CPU.</p> </li> <li> <p> <code>GPU</code>: The image version is compatible with GPU.</p> </li> </ul>"""
    horovod: NotRequired["capo_sagemaker.types.horovod.Horovod"]
    """<p>Indicates Horovod compatibility.</p>"""
    release_notes: NotRequired["capo_sagemaker.types.release_notes.ReleaseNotes"]
    """<p>The maintainer description of the image version.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateImageVersionRequest) -> dict:
    out: dict = {}
    if "base_image" in value:
        out["BaseImage"] = value["base_image"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    if "image_name" in value:
        out["ImageName"] = value["image_name"]
    if "aliases" in value:
        import capo_sagemaker.types.sage_maker_image_version_aliases

        out["Aliases"] = (
            capo_sagemaker.types.sage_maker_image_version_aliases.serialize_aws_json_1_1(
                value["aliases"]
            )
        )
    if "vendor_guidance" in value:
        import capo_sagemaker.types.vendor_guidance

        out["VendorGuidance"] = (
            capo_sagemaker.types.vendor_guidance.serialize_aws_json_1_1(
                value["vendor_guidance"]
            )
        )
    if "job_type" in value:
        import capo_sagemaker.types.job_type

        out["JobType"] = capo_sagemaker.types.job_type.serialize_aws_json_1_1(
            value["job_type"]
        )
    if "ml_framework" in value:
        out["MLFramework"] = value["ml_framework"]
    if "programming_lang" in value:
        out["ProgrammingLang"] = value["programming_lang"]
    if "processor" in value:
        import capo_sagemaker.types.processor

        out["Processor"] = capo_sagemaker.types.processor.serialize_aws_json_1_1(
            value["processor"]
        )
    if "horovod" in value:
        out["Horovod"] = value["horovod"]
    if "release_notes" in value:
        out["ReleaseNotes"] = value["release_notes"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateImageVersionRequest:
    out: CreateImageVersionRequest = {}  # type: ignore[typeddict-item]
    if "BaseImage" in data:
        out["base_image"] = data["BaseImage"]
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    if "ImageName" in data:
        out["image_name"] = data["ImageName"]
    if "Aliases" in data:
        import capo_sagemaker.types.sage_maker_image_version_aliases

        out["aliases"] = (
            capo_sagemaker.types.sage_maker_image_version_aliases.deserialize_aws_json_1_1(
                data["Aliases"]
            )
        )
    if "VendorGuidance" in data:
        import capo_sagemaker.types.vendor_guidance

        out["vendor_guidance"] = (
            capo_sagemaker.types.vendor_guidance.deserialize_aws_json_1_1(
                data["VendorGuidance"]
            )
        )
    if "JobType" in data:
        import capo_sagemaker.types.job_type

        out["job_type"] = capo_sagemaker.types.job_type.deserialize_aws_json_1_1(
            data["JobType"]
        )
    if "MLFramework" in data:
        out["ml_framework"] = data["MLFramework"]
    if "ProgrammingLang" in data:
        out["programming_lang"] = data["ProgrammingLang"]
    if "Processor" in data:
        import capo_sagemaker.types.processor

        out["processor"] = capo_sagemaker.types.processor.deserialize_aws_json_1_1(
            data["Processor"]
        )
    if "Horovod" in data:
        out["horovod"] = data["Horovod"]
    if "ReleaseNotes" in data:
        out["release_notes"] = data["ReleaseNotes"]
    return out
