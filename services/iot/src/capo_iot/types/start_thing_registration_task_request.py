"""Generated from Smithy shape ``com.amazonaws.iot#StartThingRegistrationTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iot.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iot.types.registry_s3_bucket_name
    import capo_iot.types.registry_s3_key_name
    import capo_iot.types.role_arn
    import capo_iot.types.template_body


class StartThingRegistrationTaskRequest(TypedDict, closed=True):
    template_body: "capo_iot.types.template_body.TemplateBody"
    """<p>The provisioning template.</p>"""
    input_file_bucket: "capo_iot.types.registry_s3_bucket_name.RegistryS3BucketName"
    """<p>The S3 bucket that contains the input file.</p>"""
    input_file_key: "capo_iot.types.registry_s3_key_name.RegistryS3KeyName"
    """<p>The name of input file within the S3 bucket. This file contains a newline delimited JSON file. Each line contains the parameter values to provision one device (thing).</p>"""
    role_arn: "capo_iot.types.role_arn.RoleArn"
    """<p>The IAM role ARN that grants permission the input file.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartThingRegistrationTaskRequest) -> dict:
    out: dict = {}
    out["templateBody"] = value["template_body"]
    out["inputFileBucket"] = value["input_file_bucket"]
    out["inputFileKey"] = value["input_file_key"]
    out["roleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> StartThingRegistrationTaskRequest:
    out: StartThingRegistrationTaskRequest = {}  # type: ignore[typeddict-item]
    if "templateBody" in data:
        out["template_body"] = data["templateBody"]
    else:
        raise DeserializationError(
            "StartThingRegistrationTaskRequest.template_body required"
        )
    if "inputFileBucket" in data:
        out["input_file_bucket"] = data["inputFileBucket"]
    else:
        raise DeserializationError(
            "StartThingRegistrationTaskRequest.input_file_bucket required"
        )
    if "inputFileKey" in data:
        out["input_file_key"] = data["inputFileKey"]
    else:
        raise DeserializationError(
            "StartThingRegistrationTaskRequest.input_file_key required"
        )
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError(
            "StartThingRegistrationTaskRequest.role_arn required"
        )
    return out
