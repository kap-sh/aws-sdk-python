"""Generated from Smithy shape ``com.amazonaws.emrcontainers#JobTemplate``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_emr_containers.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_emr_containers.types.date
    import aws_sdk_emr_containers.types.job_template_arn
    import aws_sdk_emr_containers.types.job_template_data
    import aws_sdk_emr_containers.types.kms_key_arn
    import aws_sdk_emr_containers.types.request_identity_user_arn
    import aws_sdk_emr_containers.types.resource_id_string
    import aws_sdk_emr_containers.types.resource_name_string
    import aws_sdk_emr_containers.types.string2048
    import aws_sdk_emr_containers.types.tag_map


class JobTemplate(TypedDict):
    name: NotRequired[
        "aws_sdk_emr_containers.types.resource_name_string.ResourceNameString"
    ]
    """<p>The name of the job template.</p>"""
    id: NotRequired["aws_sdk_emr_containers.types.resource_id_string.ResourceIdString"]
    """<p>The ID of the job template.</p>"""
    arn: NotRequired["aws_sdk_emr_containers.types.job_template_arn.JobTemplateArn"]
    """<p>The ARN of the job template.</p>"""
    created_at: NotRequired["aws_sdk_emr_containers.types.date.Date"]
    """<p> The date and time when the job template was created.</p>"""
    created_by: NotRequired[
        "aws_sdk_emr_containers.types.request_identity_user_arn.RequestIdentityUserArn"
    ]
    """<p> The user who created the job template.</p>"""
    tags: NotRequired["aws_sdk_emr_containers.types.tag_map.TagMap"]
    """<p>The tags assigned to the job template.</p>"""
    job_template_data: "aws_sdk_emr_containers.types.job_template_data.JobTemplateData"
    """<p>The job template data which holds values of StartJobRun API request.</p>"""
    kms_key_arn: NotRequired["aws_sdk_emr_containers.types.kms_key_arn.KmsKeyArn"]
    """<p> The KMS key ARN used to encrypt the job template.</p>"""
    decryption_error: NotRequired["aws_sdk_emr_containers.types.string2048.String2048"]
    """<p>The error message in case the decryption of job template fails.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobTemplate) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "id" in value:
        out["id"] = value["id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "created_at" in value:
        import aws_sdk_emr_containers.types.date

        out["createdAt"] = aws_sdk_emr_containers.types.date.serialize_json(
            value["created_at"]
        )
    if "created_by" in value:
        out["createdBy"] = value["created_by"]
    if "tags" in value:
        import aws_sdk_emr_containers.types.tag_map

        out["tags"] = aws_sdk_emr_containers.types.tag_map.serialize_json(value["tags"])
    import aws_sdk_emr_containers.types.job_template_data

    out["jobTemplateData"] = (
        aws_sdk_emr_containers.types.job_template_data.serialize_json(
            value["job_template_data"]
        )
    )
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    if "decryption_error" in value:
        out["decryptionError"] = value["decryption_error"]
    return out


def deserialize_json(data: dict) -> JobTemplate:
    out: JobTemplate = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "id" in data:
        out["id"] = data["id"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "createdAt" in data:
        import aws_sdk_emr_containers.types.date

        out["created_at"] = aws_sdk_emr_containers.types.date.deserialize_json(
            data["createdAt"]
        )
    if "createdBy" in data:
        out["created_by"] = data["createdBy"]
    if "tags" in data:
        import aws_sdk_emr_containers.types.tag_map

        out["tags"] = aws_sdk_emr_containers.types.tag_map.deserialize_json(
            data["tags"]
        )
    if "jobTemplateData" in data:
        import aws_sdk_emr_containers.types.job_template_data

        out["job_template_data"] = (
            aws_sdk_emr_containers.types.job_template_data.deserialize_json(
                data["jobTemplateData"]
            )
        )
    else:
        raise DeserializationError("JobTemplate.job_template_data required")
    if "kmsKeyArn" in data:
        out["kms_key_arn"] = data["kmsKeyArn"]
    if "decryptionError" in data:
        out["decryption_error"] = data["decryptionError"]
    return out
