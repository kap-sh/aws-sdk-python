"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#ModelDiagnosticsOutputConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_lookoutequipment.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lookoutequipment.types.model_diagnostics_s3_output_configuration
    import aws_sdk_lookoutequipment.types.name_or_arn


class ModelDiagnosticsOutputConfiguration(TypedDict):
    s3_output_configuration: "aws_sdk_lookoutequipment.types.model_diagnostics_s3_output_configuration.ModelDiagnosticsS3OutputConfiguration"
    """<p>The Amazon S3 location for the pointwise model diagnostics. </p>"""
    kms_key_id: NotRequired["aws_sdk_lookoutequipment.types.name_or_arn.NameOrArn"]
    """<p>The Amazon Web Services Key Management Service (KMS) key identifier to encrypt the pointwise model diagnostics files.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ModelDiagnosticsOutputConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_lookoutequipment.types.model_diagnostics_s3_output_configuration

    out["S3OutputConfiguration"] = (
        aws_sdk_lookoutequipment.types.model_diagnostics_s3_output_configuration.serialize_aws_json_1_0(
            value["s3_output_configuration"]
        )
    )
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ModelDiagnosticsOutputConfiguration:
    out: ModelDiagnosticsOutputConfiguration = {}  # type: ignore[typeddict-item]
    if "S3OutputConfiguration" in data:
        import aws_sdk_lookoutequipment.types.model_diagnostics_s3_output_configuration

        out["s3_output_configuration"] = (
            aws_sdk_lookoutequipment.types.model_diagnostics_s3_output_configuration.deserialize_aws_json_1_0(
                data["S3OutputConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "ModelDiagnosticsOutputConfiguration.s3_output_configuration required"
        )
    if "KmsKeyId" in data:
        out["kms_key_id"] = data["KmsKeyId"]
    return out
