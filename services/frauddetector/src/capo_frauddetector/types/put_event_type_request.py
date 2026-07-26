"""Generated from Smithy shape ``com.amazonaws.frauddetector#PutEventTypeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_frauddetector.errors import DeserializationError

if TYPE_CHECKING:
    import capo_frauddetector.types.description
    import capo_frauddetector.types.event_ingestion
    import capo_frauddetector.types.event_orchestration
    import capo_frauddetector.types.identifier
    import capo_frauddetector.types.list_of_strings
    import capo_frauddetector.types.non_empty_list_of_strings
    import capo_frauddetector.types.tag_list


class PutEventTypeRequest(TypedDict, closed=True):
    name: "capo_frauddetector.types.identifier.identifier"
    """<p>The name.</p>"""
    description: NotRequired["capo_frauddetector.types.description.description"]
    """<p>The description of the event type.</p>"""
    event_variables: (
        "capo_frauddetector.types.non_empty_list_of_strings.NonEmptyListOfStrings"
    )
    """<p>The event type variables.</p>"""
    labels: NotRequired["capo_frauddetector.types.list_of_strings.ListOfStrings"]
    """<p>The event type labels.</p>"""
    entity_types: (
        "capo_frauddetector.types.non_empty_list_of_strings.NonEmptyListOfStrings"
    )
    """<p>The entity type for the event type. Example entity types: customer, merchant, account.</p>"""
    event_ingestion: NotRequired[
        "capo_frauddetector.types.event_ingestion.EventIngestion"
    ]
    """<p>Specifies if ingestion is enabled or disabled.</p>"""
    tags: NotRequired["capo_frauddetector.types.tag_list.tagList"]
    """<p>A collection of key and value pairs.</p>"""
    event_orchestration: NotRequired[
        "capo_frauddetector.types.event_orchestration.EventOrchestration"
    ]
    """<p>Enables or disables event orchestration. If enabled, you can send event predictions to select AWS services for downstream processing of the events.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutEventTypeRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_frauddetector.types.non_empty_list_of_strings

    out["eventVariables"] = (
        capo_frauddetector.types.non_empty_list_of_strings.serialize_aws_json_1_1(
            value["event_variables"]
        )
    )
    if "labels" in value:
        import capo_frauddetector.types.list_of_strings

        out["labels"] = capo_frauddetector.types.list_of_strings.serialize_aws_json_1_1(
            value["labels"]
        )
    import capo_frauddetector.types.non_empty_list_of_strings

    out["entityTypes"] = (
        capo_frauddetector.types.non_empty_list_of_strings.serialize_aws_json_1_1(
            value["entity_types"]
        )
    )
    if "event_ingestion" in value:
        import capo_frauddetector.types.event_ingestion

        out["eventIngestion"] = (
            capo_frauddetector.types.event_ingestion.serialize_aws_json_1_1(
                value["event_ingestion"]
            )
        )
    if "tags" in value:
        import capo_frauddetector.types.tag_list

        out["tags"] = capo_frauddetector.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "event_orchestration" in value:
        import capo_frauddetector.types.event_orchestration

        out["eventOrchestration"] = (
            capo_frauddetector.types.event_orchestration.serialize_aws_json_1_1(
                value["event_orchestration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutEventTypeRequest:
    out: PutEventTypeRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("PutEventTypeRequest.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "eventVariables" in data:
        import capo_frauddetector.types.non_empty_list_of_strings

        out["event_variables"] = (
            capo_frauddetector.types.non_empty_list_of_strings.deserialize_aws_json_1_1(
                data["eventVariables"]
            )
        )
    else:
        raise DeserializationError("PutEventTypeRequest.event_variables required")
    if "labels" in data:
        import capo_frauddetector.types.list_of_strings

        out["labels"] = (
            capo_frauddetector.types.list_of_strings.deserialize_aws_json_1_1(
                data["labels"]
            )
        )
    if "entityTypes" in data:
        import capo_frauddetector.types.non_empty_list_of_strings

        out["entity_types"] = (
            capo_frauddetector.types.non_empty_list_of_strings.deserialize_aws_json_1_1(
                data["entityTypes"]
            )
        )
    else:
        raise DeserializationError("PutEventTypeRequest.entity_types required")
    if "eventIngestion" in data:
        import capo_frauddetector.types.event_ingestion

        out["event_ingestion"] = (
            capo_frauddetector.types.event_ingestion.deserialize_aws_json_1_1(
                data["eventIngestion"]
            )
        )
    if "tags" in data:
        import capo_frauddetector.types.tag_list

        out["tags"] = capo_frauddetector.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    if "eventOrchestration" in data:
        import capo_frauddetector.types.event_orchestration

        out["event_orchestration"] = (
            capo_frauddetector.types.event_orchestration.deserialize_aws_json_1_1(
                data["eventOrchestration"]
            )
        )
    return out
