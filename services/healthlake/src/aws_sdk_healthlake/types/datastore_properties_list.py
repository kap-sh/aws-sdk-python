"""Generated from Smithy shape ``com.amazonaws.healthlake#DatastorePropertiesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_healthlake.types.datastore_properties

DatastorePropertiesList: TypeAlias = list[
    "aws_sdk_healthlake.types.datastore_properties.DatastoreProperties"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DatastorePropertiesList) -> list:
    import aws_sdk_healthlake.types.datastore_properties

    out: list = []
    for item in value:
        out.append(
            aws_sdk_healthlake.types.datastore_properties.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> DatastorePropertiesList:
    import aws_sdk_healthlake.types.datastore_properties

    out: DatastorePropertiesList = []
    for item in data:
        out.append(
            aws_sdk_healthlake.types.datastore_properties.deserialize_aws_json_1_0(item)
        )
    return out
