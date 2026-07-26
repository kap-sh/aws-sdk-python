"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#InferenceOutputConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lookoutequipment.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lookoutequipment.types.inference_s3_output_configuration
    import capo_lookoutequipment.types.name_or_arn


class InferenceOutputConfiguration(TypedDict, closed=True):
    s3_output_configuration: "capo_lookoutequipment.types.inference_s3_output_configuration.InferenceS3OutputConfiguration"
    """<p> Specifies configuration information for the output results from for the inference, output S3 location. </p>"""
    kms_key_id: NotRequired["capo_lookoutequipment.types.name_or_arn.NameOrArn"]
    """<p>The ID number for the KMS key key used to encrypt the inference output. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InferenceOutputConfiguration) -> dict:
    out: dict = {}
    import capo_lookoutequipment.types.inference_s3_output_configuration

    out["S3OutputConfiguration"] = (
        capo_lookoutequipment.types.inference_s3_output_configuration.serialize_aws_json_1_0(
            value["s3_output_configuration"]
        )
    )
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> InferenceOutputConfiguration:
    out: InferenceOutputConfiguration = {}  # type: ignore[typeddict-item]
    if "S3OutputConfiguration" in data:
        import capo_lookoutequipment.types.inference_s3_output_configuration

        out["s3_output_configuration"] = (
            capo_lookoutequipment.types.inference_s3_output_configuration.deserialize_aws_json_1_0(
                data["S3OutputConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "InferenceOutputConfiguration.s3_output_configuration required"
        )
    if "KmsKeyId" in data:
        out["kms_key_id"] = data["KmsKeyId"]
    return out
