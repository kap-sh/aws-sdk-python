"""Generated from Smithy shape ``com.amazonaws.applicationsignals#ServiceState``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_application_signals.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_application_signals.types.attribute_filters
    import aws_sdk_application_signals.types.attributes
    import aws_sdk_application_signals.types.latest_change_events


class ServiceState(TypedDict):
    attribute_filters: NotRequired[
        "aws_sdk_application_signals.types.attribute_filters.AttributeFilters"
    ]
    """<p>The attribute filters that were applied when retrieving this service state information.</p>"""
    service: "aws_sdk_application_signals.types.attributes.Attributes"
    """<p>The key attributes that identify this service, including Type, Name, and Environment information.</p>"""
    latest_change_events: (
        "aws_sdk_application_signals.types.latest_change_events.LatestChangeEvents"
    )
    """<p>An array containing the most recent change events for this service, such as deployments, with information about when they occurred and who initiated them.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceState) -> dict:
    out: dict = {}
    if "attribute_filters" in value:
        import aws_sdk_application_signals.types.attribute_filters

        out["AttributeFilters"] = (
            aws_sdk_application_signals.types.attribute_filters.serialize_json(
                value["attribute_filters"]
            )
        )
    import aws_sdk_application_signals.types.attributes

    out["Service"] = aws_sdk_application_signals.types.attributes.serialize_json(
        value["service"]
    )
    import aws_sdk_application_signals.types.latest_change_events

    out["LatestChangeEvents"] = (
        aws_sdk_application_signals.types.latest_change_events.serialize_json(
            value["latest_change_events"]
        )
    )
    return out


def deserialize_json(data: dict) -> ServiceState:
    out: ServiceState = {}  # type: ignore[typeddict-item]
    if "AttributeFilters" in data:
        import aws_sdk_application_signals.types.attribute_filters

        out["attribute_filters"] = (
            aws_sdk_application_signals.types.attribute_filters.deserialize_json(
                data["AttributeFilters"]
            )
        )
    if "Service" in data:
        import aws_sdk_application_signals.types.attributes

        out["service"] = aws_sdk_application_signals.types.attributes.deserialize_json(
            data["Service"]
        )
    else:
        raise DeserializationError("ServiceState.service required")
    if "LatestChangeEvents" in data:
        import aws_sdk_application_signals.types.latest_change_events

        out["latest_change_events"] = (
            aws_sdk_application_signals.types.latest_change_events.deserialize_json(
                data["LatestChangeEvents"]
            )
        )
    else:
        raise DeserializationError("ServiceState.latest_change_events required")
    return out
