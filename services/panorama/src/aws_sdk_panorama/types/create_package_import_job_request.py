"""Generated from Smithy shape ``com.amazonaws.panorama#CreatePackageImportJobRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_panorama.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_panorama.types.client_token
    import aws_sdk_panorama.types.job_tags_list
    import aws_sdk_panorama.types.package_import_job_input_config
    import aws_sdk_panorama.types.package_import_job_output_config
    import aws_sdk_panorama.types.package_import_job_type


class CreatePackageImportJobRequest(TypedDict):
    job_type: "aws_sdk_panorama.types.package_import_job_type.PackageImportJobType"
    """<p>A job type for the package import job.</p>"""
    input_config: "aws_sdk_panorama.types.package_import_job_input_config.PackageImportJobInputConfig"
    """<p>An input config for the package import job.</p>"""
    output_config: "aws_sdk_panorama.types.package_import_job_output_config.PackageImportJobOutputConfig"
    """<p>An output config for the package import job.</p>"""
    client_token: "aws_sdk_panorama.types.client_token.ClientToken"
    """<p>A client token for the package import job.</p>"""
    job_tags: NotRequired["aws_sdk_panorama.types.job_tags_list.JobTagsList"]
    """<p>Tags for the package import job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePackageImportJobRequest) -> dict:
    out: dict = {}
    out["JobType"] = value["job_type"]
    import aws_sdk_panorama.types.package_import_job_input_config

    out["InputConfig"] = (
        aws_sdk_panorama.types.package_import_job_input_config.serialize_json(
            value["input_config"]
        )
    )
    import aws_sdk_panorama.types.package_import_job_output_config

    out["OutputConfig"] = (
        aws_sdk_panorama.types.package_import_job_output_config.serialize_json(
            value["output_config"]
        )
    )
    out["ClientToken"] = value["client_token"]
    if "job_tags" in value:
        import aws_sdk_panorama.types.job_tags_list

        out["JobTags"] = aws_sdk_panorama.types.job_tags_list.serialize_json(
            value["job_tags"]
        )
    return out


def deserialize_json(data: dict) -> CreatePackageImportJobRequest:
    out: CreatePackageImportJobRequest = {}  # type: ignore[typeddict-item]
    if "JobType" in data:
        out["job_type"] = data["JobType"]
    else:
        raise DeserializationError("CreatePackageImportJobRequest.job_type required")
    if "InputConfig" in data:
        import aws_sdk_panorama.types.package_import_job_input_config

        out["input_config"] = (
            aws_sdk_panorama.types.package_import_job_input_config.deserialize_json(
                data["InputConfig"]
            )
        )
    else:
        raise DeserializationError(
            "CreatePackageImportJobRequest.input_config required"
        )
    if "OutputConfig" in data:
        import aws_sdk_panorama.types.package_import_job_output_config

        out["output_config"] = (
            aws_sdk_panorama.types.package_import_job_output_config.deserialize_json(
                data["OutputConfig"]
            )
        )
    else:
        raise DeserializationError(
            "CreatePackageImportJobRequest.output_config required"
        )
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    else:
        raise DeserializationError(
            "CreatePackageImportJobRequest.client_token required"
        )
    if "JobTags" in data:
        import aws_sdk_panorama.types.job_tags_list

        out["job_tags"] = aws_sdk_panorama.types.job_tags_list.deserialize_json(
            data["JobTags"]
        )
    return out
