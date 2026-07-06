"""Generated from Smithy shape ``com.amazonaws.athena#S3LoggingConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_athena.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_athena.types.boxed_boolean
    import aws_sdk_athena.types.kms_key
    import aws_sdk_athena.types.s3_output_location


class S3LoggingConfiguration(TypedDict, closed=True):
    enabled: "aws_sdk_athena.types.boxed_boolean.BoxedBoolean"
    """<p>Enables S3 log delivery.</p>"""
    kms_key: NotRequired["aws_sdk_athena.types.kms_key.KmsKey"]
    """<p>The KMS key ARN to encrypt the logs published to the given Amazon S3 destination.</p>"""
    log_location: NotRequired[
        "aws_sdk_athena.types.s3_output_location.S3OutputLocation"
    ]
    """<p>The Amazon S3 destination URI for log publishing.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3LoggingConfiguration) -> dict:
    out: dict = {}
    out["Enabled"] = value["enabled"]
    if "kms_key" in value:
        out["KmsKey"] = value["kms_key"]
    if "log_location" in value:
        out["LogLocation"] = value["log_location"]
    return out


def deserialize_aws_json_1_1(data: dict) -> S3LoggingConfiguration:
    out: S3LoggingConfiguration = {}  # type: ignore[typeddict-item]
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    else:
        raise DeserializationError("S3LoggingConfiguration.enabled required")
    if "KmsKey" in data:
        out["kms_key"] = data["KmsKey"]
    if "LogLocation" in data:
        out["log_location"] = data["LogLocation"]
    return out
