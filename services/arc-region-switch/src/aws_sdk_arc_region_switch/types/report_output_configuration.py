"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#ReportOutputConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_arc_region_switch.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_arc_region_switch.types.s3_report_output_configuration


class _ReportOutputConfiguration_s3Configuration(TypedDict):
    s3Configuration: "aws_sdk_arc_region_switch.types.s3_report_output_configuration.S3ReportOutputConfiguration"


ReportOutputConfiguration: TypeAlias = _ReportOutputConfiguration_s3Configuration


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ReportOutputConfiguration) -> dict:
    if "s3Configuration" in value:
        import aws_sdk_arc_region_switch.types.s3_report_output_configuration

        return {
            "s3Configuration": aws_sdk_arc_region_switch.types.s3_report_output_configuration.serialize_aws_json_1_0(
                value["s3Configuration"]
            )
        }
    else:
        raise SerializationError("ReportOutputConfiguration: no variant present")


def deserialize_aws_json_1_0(data: dict) -> ReportOutputConfiguration:
    if "s3Configuration" in data:
        import aws_sdk_arc_region_switch.types.s3_report_output_configuration

        return {
            "s3Configuration": aws_sdk_arc_region_switch.types.s3_report_output_configuration.deserialize_aws_json_1_0(
                data["s3Configuration"]
            )
        }
    else:
        raise DeserializationError(
            "ReportOutputConfiguration: no recognized variant key"
        )
