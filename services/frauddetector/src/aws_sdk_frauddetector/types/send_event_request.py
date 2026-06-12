"""Generated from Smithy shape ``com.amazonaws.frauddetector#SendEventRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_frauddetector.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.event_variable_map
    import aws_sdk_frauddetector.types.identifier
    import aws_sdk_frauddetector.types.list_of_entities
    import aws_sdk_frauddetector.types.utc_timestamp_iso8601


class SendEventRequest(TypedDict):
    event_id: "aws_sdk_frauddetector.types.identifier.identifier"
    """<p>The event ID to upload.</p>"""
    event_type_name: "aws_sdk_frauddetector.types.identifier.identifier"
    """<p>The event type name of the event.</p>"""
    event_timestamp: (
        "aws_sdk_frauddetector.types.utc_timestamp_iso8601.utcTimestampISO8601"
    )
    """<p>The timestamp that defines when the event under evaluation occurred. The timestamp must be specified using ISO 8601 standard in UTC.</p>"""
    event_variables: "aws_sdk_frauddetector.types.event_variable_map.EventVariableMap"
    """<p>Names of the event type's variables you defined in Amazon Fraud Detector to represent data elements and their corresponding values for the event you are sending for evaluation.</p>"""
    assigned_label: NotRequired["aws_sdk_frauddetector.types.identifier.identifier"]
    """<p>The label to associate with the event. Required if specifying <code>labelTimestamp</code>.</p>"""
    label_timestamp: NotRequired[
        "aws_sdk_frauddetector.types.utc_timestamp_iso8601.utcTimestampISO8601"
    ]
    """<p>The timestamp associated with the label. Required if specifying <code>assignedLabel</code>.</p>"""
    entities: "aws_sdk_frauddetector.types.list_of_entities.listOfEntities"
    """<p>An array of entities.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SendEventRequest) -> dict:
    out: dict = {}
    out["eventId"] = value["event_id"]
    out["eventTypeName"] = value["event_type_name"]
    out["eventTimestamp"] = value["event_timestamp"]
    import aws_sdk_frauddetector.types.event_variable_map

    out["eventVariables"] = (
        aws_sdk_frauddetector.types.event_variable_map.serialize_aws_json_1_1(
            value["event_variables"]
        )
    )
    if "assigned_label" in value:
        out["assignedLabel"] = value["assigned_label"]
    if "label_timestamp" in value:
        out["labelTimestamp"] = value["label_timestamp"]
    import aws_sdk_frauddetector.types.list_of_entities

    out["entities"] = (
        aws_sdk_frauddetector.types.list_of_entities.serialize_aws_json_1_1(
            value["entities"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> SendEventRequest:
    out: SendEventRequest = {}  # type: ignore[typeddict-item]
    if "eventId" in data:
        out["event_id"] = data["eventId"]
    else:
        raise DeserializationError("SendEventRequest.event_id required")
    if "eventTypeName" in data:
        out["event_type_name"] = data["eventTypeName"]
    else:
        raise DeserializationError("SendEventRequest.event_type_name required")
    if "eventTimestamp" in data:
        out["event_timestamp"] = data["eventTimestamp"]
    else:
        raise DeserializationError("SendEventRequest.event_timestamp required")
    if "eventVariables" in data:
        import aws_sdk_frauddetector.types.event_variable_map

        out["event_variables"] = (
            aws_sdk_frauddetector.types.event_variable_map.deserialize_aws_json_1_1(
                data["eventVariables"]
            )
        )
    else:
        raise DeserializationError("SendEventRequest.event_variables required")
    if "assignedLabel" in data:
        out["assigned_label"] = data["assignedLabel"]
    if "labelTimestamp" in data:
        out["label_timestamp"] = data["labelTimestamp"]
    if "entities" in data:
        import aws_sdk_frauddetector.types.list_of_entities

        out["entities"] = (
            aws_sdk_frauddetector.types.list_of_entities.deserialize_aws_json_1_1(
                data["entities"]
            )
        )
    else:
        raise DeserializationError("SendEventRequest.entities required")
    return out
