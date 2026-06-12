"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#InferenceInputConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lookoutequipment.types.inference_input_name_configuration
    import aws_sdk_lookoutequipment.types.inference_s3_input_configuration
    import aws_sdk_lookoutequipment.types.time_zone_offset


class InferenceInputConfiguration(TypedDict):
    s3_input_configuration: NotRequired[
        "aws_sdk_lookoutequipment.types.inference_s3_input_configuration.InferenceS3InputConfiguration"
    ]
    """<p> Specifies configuration information for the input data for the inference, including Amazon S3 location of input data.</p>"""
    input_time_zone_offset: NotRequired[
        "aws_sdk_lookoutequipment.types.time_zone_offset.TimeZoneOffset"
    ]
    """<p>Indicates the difference between your time zone and Coordinated Universal Time (UTC).</p>"""
    inference_input_name_configuration: NotRequired[
        "aws_sdk_lookoutequipment.types.inference_input_name_configuration.InferenceInputNameConfiguration"
    ]
    """<p>Specifies configuration information for the input data for the inference, including timestamp format and delimiter. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InferenceInputConfiguration) -> dict:
    out: dict = {}
    if "s3_input_configuration" in value:
        import aws_sdk_lookoutequipment.types.inference_s3_input_configuration

        out["S3InputConfiguration"] = (
            aws_sdk_lookoutequipment.types.inference_s3_input_configuration.serialize_aws_json_1_0(
                value["s3_input_configuration"]
            )
        )
    if "input_time_zone_offset" in value:
        out["InputTimeZoneOffset"] = value["input_time_zone_offset"]
    if "inference_input_name_configuration" in value:
        import aws_sdk_lookoutequipment.types.inference_input_name_configuration

        out["InferenceInputNameConfiguration"] = (
            aws_sdk_lookoutequipment.types.inference_input_name_configuration.serialize_aws_json_1_0(
                value["inference_input_name_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> InferenceInputConfiguration:
    out: InferenceInputConfiguration = {}  # type: ignore[typeddict-item]
    if "S3InputConfiguration" in data:
        import aws_sdk_lookoutequipment.types.inference_s3_input_configuration

        out["s3_input_configuration"] = (
            aws_sdk_lookoutequipment.types.inference_s3_input_configuration.deserialize_aws_json_1_0(
                data["S3InputConfiguration"]
            )
        )
    if "InputTimeZoneOffset" in data:
        out["input_time_zone_offset"] = data["InputTimeZoneOffset"]
    if "InferenceInputNameConfiguration" in data:
        import aws_sdk_lookoutequipment.types.inference_input_name_configuration

        out["inference_input_name_configuration"] = (
            aws_sdk_lookoutequipment.types.inference_input_name_configuration.deserialize_aws_json_1_0(
                data["InferenceInputNameConfiguration"]
            )
        )
    return out
