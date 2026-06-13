"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ProtectedQueryDistributeOutputConfigurationLocations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.protected_query_distribute_output_configuration_location

ProtectedQueryDistributeOutputConfigurationLocations: TypeAlias = list[
    "aws_sdk_cleanrooms.types.protected_query_distribute_output_configuration_location.ProtectedQueryDistributeOutputConfigurationLocation"
]


# --- restJson1 ser/de ---
def serialize_json(value: ProtectedQueryDistributeOutputConfigurationLocations) -> list:
    import aws_sdk_cleanrooms.types.protected_query_distribute_output_configuration_location

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cleanrooms.types.protected_query_distribute_output_configuration_location.serialize_json(
                item
            )
        )
    return out


def deserialize_json(
    data: list,
) -> ProtectedQueryDistributeOutputConfigurationLocations:
    import aws_sdk_cleanrooms.types.protected_query_distribute_output_configuration_location

    out: ProtectedQueryDistributeOutputConfigurationLocations = []
    for item in data:
        out.append(
            aws_sdk_cleanrooms.types.protected_query_distribute_output_configuration_location.deserialize_json(
                item
            )
        )
    return out
