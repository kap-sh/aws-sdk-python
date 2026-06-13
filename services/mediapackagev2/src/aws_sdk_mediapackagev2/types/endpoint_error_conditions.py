"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#EndpointErrorConditions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediapackagev2.types.endpoint_error_condition

EndpointErrorConditions: TypeAlias = list[
    "aws_sdk_mediapackagev2.types.endpoint_error_condition.EndpointErrorCondition"
]


# --- restJson1 ser/de ---
def serialize_json(value: EndpointErrorConditions) -> list:
    import aws_sdk_mediapackagev2.types.endpoint_error_condition

    out: list = []
    for item in value:
        out.append(
            aws_sdk_mediapackagev2.types.endpoint_error_condition.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> EndpointErrorConditions:
    import aws_sdk_mediapackagev2.types.endpoint_error_condition

    out: EndpointErrorConditions = []
    for item in data:
        out.append(
            aws_sdk_mediapackagev2.types.endpoint_error_condition.deserialize_json(item)
        )
    return out
