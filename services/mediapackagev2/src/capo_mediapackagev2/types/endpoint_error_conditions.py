"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#EndpointErrorConditions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediapackagev2.types.endpoint_error_condition

EndpointErrorConditions: TypeAlias = list[
    "capo_mediapackagev2.types.endpoint_error_condition.EndpointErrorCondition"
]


# --- restJson1 ser/de ---
def serialize_json(value: EndpointErrorConditions) -> list:
    import capo_mediapackagev2.types.endpoint_error_condition

    out: list = []
    for item in value:
        out.append(
            capo_mediapackagev2.types.endpoint_error_condition.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> EndpointErrorConditions:
    import capo_mediapackagev2.types.endpoint_error_condition

    out: EndpointErrorConditions = []
    for item in data:
        out.append(
            capo_mediapackagev2.types.endpoint_error_condition.deserialize_json(item)
        )
    return out
