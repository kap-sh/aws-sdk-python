"""Generated from Smithy shape ``com.amazonaws.frauddetector#EventType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_frauddetector.types.description
    import capo_frauddetector.types.event_ingestion
    import capo_frauddetector.types.event_orchestration
    import capo_frauddetector.types.fraud_detector_arn
    import capo_frauddetector.types.ingested_event_statistics
    import capo_frauddetector.types.list_of_strings
    import capo_frauddetector.types.non_empty_list_of_strings
    import capo_frauddetector.types.string
    import capo_frauddetector.types.time


class EventType(TypedDict, closed=True):
    name: NotRequired["capo_frauddetector.types.string.string"]
    """<p>The event type name.</p>"""
    description: NotRequired["capo_frauddetector.types.description.description"]
    """<p>The event type description.</p>"""
    event_variables: NotRequired[
        "capo_frauddetector.types.list_of_strings.ListOfStrings"
    ]
    """<p>The event type event variables.</p>"""
    labels: NotRequired["capo_frauddetector.types.list_of_strings.ListOfStrings"]
    """<p>The event type labels.</p>"""
    entity_types: NotRequired[
        "capo_frauddetector.types.non_empty_list_of_strings.NonEmptyListOfStrings"
    ]
    """<p>The event type entity types.</p>"""
    event_ingestion: NotRequired[
        "capo_frauddetector.types.event_ingestion.EventIngestion"
    ]
    """<p>If <code>Enabled</code>, Amazon Fraud Detector stores event data when you generate a prediction and uses that data to update calculated variables in near real-time. Amazon Fraud Detector uses this data, known as <code>INGESTED_EVENTS</code>, to train your model and improve fraud predictions.</p>"""
    ingested_event_statistics: NotRequired[
        "capo_frauddetector.types.ingested_event_statistics.IngestedEventStatistics"
    ]
    """<p>Data about the stored events.</p>"""
    last_updated_time: NotRequired["capo_frauddetector.types.time.time"]
    """<p>Timestamp of when the event type was last updated.</p>"""
    created_time: NotRequired["capo_frauddetector.types.time.time"]
    """<p>Timestamp of when the event type was created.</p>"""
    arn: NotRequired["capo_frauddetector.types.fraud_detector_arn.fraudDetectorArn"]
    """<p>The entity type ARN.</p>"""
    event_orchestration: NotRequired[
        "capo_frauddetector.types.event_orchestration.EventOrchestration"
    ]
    """<p>The event orchestration status. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EventType) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "event_variables" in value:
        import capo_frauddetector.types.list_of_strings

        out["eventVariables"] = (
            capo_frauddetector.types.list_of_strings.serialize_aws_json_1_1(
                value["event_variables"]
            )
        )
    if "labels" in value:
        import capo_frauddetector.types.list_of_strings

        out["labels"] = capo_frauddetector.types.list_of_strings.serialize_aws_json_1_1(
            value["labels"]
        )
    if "entity_types" in value:
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
    if "ingested_event_statistics" in value:
        import capo_frauddetector.types.ingested_event_statistics

        out["ingestedEventStatistics"] = (
            capo_frauddetector.types.ingested_event_statistics.serialize_aws_json_1_1(
                value["ingested_event_statistics"]
            )
        )
    if "last_updated_time" in value:
        out["lastUpdatedTime"] = value["last_updated_time"]
    if "created_time" in value:
        out["createdTime"] = value["created_time"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "event_orchestration" in value:
        import capo_frauddetector.types.event_orchestration

        out["eventOrchestration"] = (
            capo_frauddetector.types.event_orchestration.serialize_aws_json_1_1(
                value["event_orchestration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EventType:
    out: EventType = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "eventVariables" in data:
        import capo_frauddetector.types.list_of_strings

        out["event_variables"] = (
            capo_frauddetector.types.list_of_strings.deserialize_aws_json_1_1(
                data["eventVariables"]
            )
        )
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
    if "eventIngestion" in data:
        import capo_frauddetector.types.event_ingestion

        out["event_ingestion"] = (
            capo_frauddetector.types.event_ingestion.deserialize_aws_json_1_1(
                data["eventIngestion"]
            )
        )
    if "ingestedEventStatistics" in data:
        import capo_frauddetector.types.ingested_event_statistics

        out["ingested_event_statistics"] = (
            capo_frauddetector.types.ingested_event_statistics.deserialize_aws_json_1_1(
                data["ingestedEventStatistics"]
            )
        )
    if "lastUpdatedTime" in data:
        out["last_updated_time"] = data["lastUpdatedTime"]
    if "createdTime" in data:
        out["created_time"] = data["createdTime"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "eventOrchestration" in data:
        import capo_frauddetector.types.event_orchestration

        out["event_orchestration"] = (
            capo_frauddetector.types.event_orchestration.deserialize_aws_json_1_1(
                data["eventOrchestration"]
            )
        )
    return out
