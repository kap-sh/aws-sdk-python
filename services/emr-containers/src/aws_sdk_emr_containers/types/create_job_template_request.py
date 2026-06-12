"""Generated from Smithy shape ``com.amazonaws.emrcontainers#CreateJobTemplateRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_emr_containers.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_emr_containers.types.client_token
    import aws_sdk_emr_containers.types.job_template_data
    import aws_sdk_emr_containers.types.kms_key_arn
    import aws_sdk_emr_containers.types.resource_name_string
    import aws_sdk_emr_containers.types.tag_map


class CreateJobTemplateRequest(TypedDict):
    name: "aws_sdk_emr_containers.types.resource_name_string.ResourceNameString"
    """<p>The specified name of the job template.</p>"""
    client_token: "aws_sdk_emr_containers.types.client_token.ClientToken"
    """<p>The client token of the job template.</p>"""
    job_template_data: "aws_sdk_emr_containers.types.job_template_data.JobTemplateData"
    """<p>The job template data which holds values of StartJobRun API request.</p>"""
    tags: NotRequired["aws_sdk_emr_containers.types.tag_map.TagMap"]
    """<p>The tags that are associated with the job template.</p>"""
    kms_key_arn: NotRequired["aws_sdk_emr_containers.types.kms_key_arn.KmsKeyArn"]
    """<p>The KMS key ARN used to encrypt the job template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateJobTemplateRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["clientToken"] = value["client_token"]
    import aws_sdk_emr_containers.types.job_template_data

    out["jobTemplateData"] = (
        aws_sdk_emr_containers.types.job_template_data.serialize_json(
            value["job_template_data"]
        )
    )
    if "tags" in value:
        import aws_sdk_emr_containers.types.tag_map

        out["tags"] = aws_sdk_emr_containers.types.tag_map.serialize_json(value["tags"])
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    return out


def deserialize_json(data: dict) -> CreateJobTemplateRequest:
    out: CreateJobTemplateRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateJobTemplateRequest.name required")
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    else:
        raise DeserializationError("CreateJobTemplateRequest.client_token required")
    if "jobTemplateData" in data:
        import aws_sdk_emr_containers.types.job_template_data

        out["job_template_data"] = (
            aws_sdk_emr_containers.types.job_template_data.deserialize_json(
                data["jobTemplateData"]
            )
        )
    else:
        raise DeserializationError(
            "CreateJobTemplateRequest.job_template_data required"
        )
    if "tags" in data:
        import aws_sdk_emr_containers.types.tag_map

        out["tags"] = aws_sdk_emr_containers.types.tag_map.deserialize_json(
            data["tags"]
        )
    if "kmsKeyArn" in data:
        out["kms_key_arn"] = data["kmsKeyArn"]
    return out
