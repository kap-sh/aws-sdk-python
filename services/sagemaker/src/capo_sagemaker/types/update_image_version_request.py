"""Generated from Smithy shape ``com.amazonaws.sagemaker#UpdateImageVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.horovod
    import capo_sagemaker.types.image_name
    import capo_sagemaker.types.image_version_number
    import capo_sagemaker.types.job_type
    import capo_sagemaker.types.ml_framework
    import capo_sagemaker.types.processor
    import capo_sagemaker.types.programming_lang
    import capo_sagemaker.types.release_notes
    import capo_sagemaker.types.sage_maker_image_version_alias
    import capo_sagemaker.types.sage_maker_image_version_aliases
    import capo_sagemaker.types.vendor_guidance


class UpdateImageVersionRequest(TypedDict, closed=True):
    image_name: NotRequired["capo_sagemaker.types.image_name.ImageName"]
    """<p>The name of the image.</p>"""
    alias: NotRequired[
        "capo_sagemaker.types.sage_maker_image_version_alias.SageMakerImageVersionAlias"
    ]
    """<p>The alias of the image version.</p>"""
    version: NotRequired["capo_sagemaker.types.image_version_number.ImageVersionNumber"]
    """<p>The version of the image.</p>"""
    aliases_to_add: NotRequired[
        "capo_sagemaker.types.sage_maker_image_version_aliases.SageMakerImageVersionAliases"
    ]
    """<p>A list of aliases to add.</p>"""
    aliases_to_delete: NotRequired[
        "capo_sagemaker.types.sage_maker_image_version_aliases.SageMakerImageVersionAliases"
    ]
    """<p>A list of aliases to delete.</p>"""
    vendor_guidance: NotRequired["capo_sagemaker.types.vendor_guidance.VendorGuidance"]
    """<p>The availability of the image version specified by the maintainer.</p> <ul> <li> <p> <code>NOT_PROVIDED</code>: The maintainers did not provide a status for image version stability.</p> </li> <li> <p> <code>STABLE</code>: The image version is stable.</p> </li> <li> <p> <code>TO_BE_ARCHIVED</code>: The image version is set to be archived. Custom image versions that are set to be archived are automatically archived after three months.</p> </li> <li> <p> <code>ARCHIVED</code>: The image version is archived. Archived image versions are not searchable and are no longer actively supported. </p> </li> </ul>"""
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
def serialize_aws_json_1_1(value: UpdateImageVersionRequest) -> dict:
    out: dict = {}
    if "image_name" in value:
        out["ImageName"] = value["image_name"]
    if "alias" in value:
        out["Alias"] = value["alias"]
    if "version" in value:
        out["Version"] = value["version"]
    if "aliases_to_add" in value:
        import capo_sagemaker.types.sage_maker_image_version_aliases

        out["AliasesToAdd"] = (
            capo_sagemaker.types.sage_maker_image_version_aliases.serialize_aws_json_1_1(
                value["aliases_to_add"]
            )
        )
    if "aliases_to_delete" in value:
        import capo_sagemaker.types.sage_maker_image_version_aliases

        out["AliasesToDelete"] = (
            capo_sagemaker.types.sage_maker_image_version_aliases.serialize_aws_json_1_1(
                value["aliases_to_delete"]
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


def deserialize_aws_json_1_1(data: dict) -> UpdateImageVersionRequest:
    out: UpdateImageVersionRequest = {}  # type: ignore[typeddict-item]
    if "ImageName" in data:
        out["image_name"] = data["ImageName"]
    if "Alias" in data:
        out["alias"] = data["Alias"]
    if "Version" in data:
        out["version"] = data["Version"]
    if "AliasesToAdd" in data:
        import capo_sagemaker.types.sage_maker_image_version_aliases

        out["aliases_to_add"] = (
            capo_sagemaker.types.sage_maker_image_version_aliases.deserialize_aws_json_1_1(
                data["AliasesToAdd"]
            )
        )
    if "AliasesToDelete" in data:
        import capo_sagemaker.types.sage_maker_image_version_aliases

        out["aliases_to_delete"] = (
            capo_sagemaker.types.sage_maker_image_version_aliases.deserialize_aws_json_1_1(
                data["AliasesToDelete"]
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
