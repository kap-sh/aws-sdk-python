"""Generated from Smithy shape ``com.amazonaws.healthlake#ExportJobPropertiesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_healthlake.types.export_job_properties

ExportJobPropertiesList: TypeAlias = list[
    "aws_sdk_healthlake.types.export_job_properties.ExportJobProperties"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExportJobPropertiesList) -> list:
    import aws_sdk_healthlake.types.export_job_properties

    out: list = []
    for item in value:
        out.append(
            aws_sdk_healthlake.types.export_job_properties.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ExportJobPropertiesList:
    import aws_sdk_healthlake.types.export_job_properties

    out: ExportJobPropertiesList = []
    for item in data:
        out.append(
            aws_sdk_healthlake.types.export_job_properties.deserialize_aws_json_1_0(
                item
            )
        )
    return out
