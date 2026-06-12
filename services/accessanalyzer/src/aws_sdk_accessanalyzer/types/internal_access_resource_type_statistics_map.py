"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#InternalAccessResourceTypeStatisticsMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.internal_access_resource_type_details
    import aws_sdk_accessanalyzer.types.resource_type

InternalAccessResourceTypeStatisticsMap: TypeAlias = dict[
    "aws_sdk_accessanalyzer.types.resource_type.ResourceType",
    "aws_sdk_accessanalyzer.types.internal_access_resource_type_details.InternalAccessResourceTypeDetails",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: InternalAccessResourceTypeStatisticsMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_accessanalyzer.types.internal_access_resource_type_details

        out[key] = (
            aws_sdk_accessanalyzer.types.internal_access_resource_type_details.serialize_json(
                value
            )
        )
    return out


def deserialize_json(data: dict) -> InternalAccessResourceTypeStatisticsMap:
    out: InternalAccessResourceTypeStatisticsMap = {}
    for key, value in data.items():
        import aws_sdk_accessanalyzer.types.internal_access_resource_type_details

        out[key] = (
            aws_sdk_accessanalyzer.types.internal_access_resource_type_details.deserialize_json(
                value
            )
        )
    return out
