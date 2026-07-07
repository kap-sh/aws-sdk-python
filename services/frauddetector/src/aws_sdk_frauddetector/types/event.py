"""Generated from Smithy shape ``com.amazonaws.frauddetector#Event``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.event_attribute_map
    import aws_sdk_frauddetector.types.list_of_entities
    import aws_sdk_frauddetector.types.string


class Event(TypedDict, closed=True):
    event_id: NotRequired["aws_sdk_frauddetector.types.string.string"]
    """<p>The event ID.</p>"""
    event_type_name: NotRequired["aws_sdk_frauddetector.types.string.string"]
    """<p>The event type.</p>"""
    event_timestamp: NotRequired["aws_sdk_frauddetector.types.string.string"]
    """<p>The timestamp that defines when the event under evaluation occurred. The timestamp must be specified using ISO 8601 standard in UTC.</p>"""
    event_variables: NotRequired[
        "aws_sdk_frauddetector.types.event_attribute_map.EventAttributeMap"
    ]
    """<p>Names of the event type's variables you defined in Amazon Fraud Detector to represent data elements and their corresponding values for the event you are sending for evaluation.</p>"""
    current_label: NotRequired["aws_sdk_frauddetector.types.string.string"]
    """<p>The label associated with the event.</p>"""
    label_timestamp: NotRequired["aws_sdk_frauddetector.types.string.string"]
    """<p>The timestamp associated with the label to update. The timestamp must be specified using ISO 8601 standard in UTC.</p>"""
    entities: NotRequired["aws_sdk_frauddetector.types.list_of_entities.listOfEntities"]
    """<p>The event entities.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Event) -> dict:
    out: dict = {}
    if "event_id" in value:
        out["eventId"] = value["event_id"]
    if "event_type_name" in value:
        out["eventTypeName"] = value["event_type_name"]
    if "event_timestamp" in value:
        out["eventTimestamp"] = value["event_timestamp"]
    if "event_variables" in value:
        import aws_sdk_frauddetector.types.event_attribute_map

        out["eventVariables"] = (
            aws_sdk_frauddetector.types.event_attribute_map.serialize_aws_json_1_1(
                value["event_variables"]
            )
        )
    if "current_label" in value:
        out["currentLabel"] = value["current_label"]
    if "label_timestamp" in value:
        out["labelTimestamp"] = value["label_timestamp"]
    if "entities" in value:
        import aws_sdk_frauddetector.types.list_of_entities

        out["entities"] = (
            aws_sdk_frauddetector.types.list_of_entities.serialize_aws_json_1_1(
                value["entities"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Event:
    out: Event = {}  # type: ignore[typeddict-item]
    if "eventId" in data:
        out["event_id"] = data["eventId"]
    if "eventTypeName" in data:
        out["event_type_name"] = data["eventTypeName"]
    if "eventTimestamp" in data:
        out["event_timestamp"] = data["eventTimestamp"]
    if "eventVariables" in data:
        import aws_sdk_frauddetector.types.event_attribute_map

        out["event_variables"] = (
            aws_sdk_frauddetector.types.event_attribute_map.deserialize_aws_json_1_1(
                data["eventVariables"]
            )
        )
    if "currentLabel" in data:
        out["current_label"] = data["currentLabel"]
    if "labelTimestamp" in data:
        out["label_timestamp"] = data["labelTimestamp"]
    if "entities" in data:
        import aws_sdk_frauddetector.types.list_of_entities

        out["entities"] = (
            aws_sdk_frauddetector.types.list_of_entities.deserialize_aws_json_1_1(
                data["entities"]
            )
        )
    return out
