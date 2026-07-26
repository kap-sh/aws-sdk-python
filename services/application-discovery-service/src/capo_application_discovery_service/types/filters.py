"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#Filters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_application_discovery_service.types.filter

Filters: TypeAlias = list["capo_application_discovery_service.types.filter.Filter"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Filters) -> list:
    import capo_application_discovery_service.types.filter

    out: list = []
    for item in value:
        out.append(
            capo_application_discovery_service.types.filter.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> Filters:
    import capo_application_discovery_service.types.filter

    out: Filters = []
    for item in data:
        out.append(
            capo_application_discovery_service.types.filter.deserialize_aws_json_1_1(
                item
            )
        )
    return out
