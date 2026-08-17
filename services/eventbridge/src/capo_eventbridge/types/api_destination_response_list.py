"""Generated from Smithy shape ``com.amazonaws.eventbridge#ApiDestinationResponseList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_eventbridge.types.api_destination

ApiDestinationResponseList: TypeAlias = list[
    "capo_eventbridge.types.api_destination.ApiDestination"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApiDestinationResponseList) -> list:
    import capo_eventbridge.types.api_destination

    out: list = []
    for item in value:
        out.append(capo_eventbridge.types.api_destination.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ApiDestinationResponseList:
    import capo_eventbridge.types.api_destination

    out: ApiDestinationResponseList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_eventbridge.types.api_destination.deserialize_aws_json_1_1(item)
        )
    return out
