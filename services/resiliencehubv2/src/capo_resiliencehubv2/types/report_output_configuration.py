"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ReportOutputConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_resiliencehubv2.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.s3_report_output_configuration


class _ReportOutputConfiguration_s3(TypedDict, closed=True):
    s3: "capo_resiliencehubv2.types.s3_report_output_configuration.S3ReportOutputConfiguration"


ReportOutputConfiguration: TypeAlias = _ReportOutputConfiguration_s3


# --- restJson1 ser/de ---
def serialize_json(value: ReportOutputConfiguration) -> dict:
    if "s3" in value:
        import capo_resiliencehubv2.types.s3_report_output_configuration

        return {
            "s3": capo_resiliencehubv2.types.s3_report_output_configuration.serialize_json(
                value["s3"]
            )
        }
    else:
        raise SerializationError("ReportOutputConfiguration: no variant present")


def deserialize_json(data: dict) -> ReportOutputConfiguration:
    if "s3" in data:
        import capo_resiliencehubv2.types.s3_report_output_configuration

        return {
            "s3": capo_resiliencehubv2.types.s3_report_output_configuration.deserialize_json(
                data["s3"]
            )
        }
    else:
        raise DeserializationError(
            "ReportOutputConfiguration: no recognized variant key"
        )
