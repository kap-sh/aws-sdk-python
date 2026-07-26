"""Generated from Smithy shape ``com.amazonaws.healthlake#ImportJobPropertiesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_healthlake.types.import_job_properties

ImportJobPropertiesList: TypeAlias = list[
    "capo_healthlake.types.import_job_properties.ImportJobProperties"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ImportJobPropertiesList) -> list:
    import capo_healthlake.types.import_job_properties

    out: list = []
    for item in value:
        out.append(
            capo_healthlake.types.import_job_properties.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ImportJobPropertiesList:
    import capo_healthlake.types.import_job_properties

    out: ImportJobPropertiesList = []
    for item in data:
        out.append(
            capo_healthlake.types.import_job_properties.deserialize_aws_json_1_0(item)
        )
    return out
