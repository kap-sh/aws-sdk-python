"""Generated from Smithy shape ``com.amazonaws.connect#Evaluation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.arn
    import aws_sdk_connect.types.evaluation_answers_output_map
    import aws_sdk_connect.types.evaluation_metadata
    import aws_sdk_connect.types.evaluation_notes_map
    import aws_sdk_connect.types.evaluation_scores_map
    import aws_sdk_connect.types.evaluation_status
    import aws_sdk_connect.types.evaluation_type
    import aws_sdk_connect.types.resource_id
    import aws_sdk_connect.types.tag_map
    import aws_sdk_connect.types.timestamp


class Evaluation(TypedDict):
    evaluation_id: "aws_sdk_connect.types.resource_id.ResourceId"
    """<p>A unique identifier for the contact evaluation.</p>"""
    evaluation_arn: "aws_sdk_connect.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) for the contact evaluation resource.</p>"""
    metadata: "aws_sdk_connect.types.evaluation_metadata.EvaluationMetadata"
    """<p>Metadata about the contact evaluation.</p>"""
    answers: (
        "aws_sdk_connect.types.evaluation_answers_output_map.EvaluationAnswersOutputMap"
    )
    """<p>A map of question identifiers to answer value.</p>"""
    notes: "aws_sdk_connect.types.evaluation_notes_map.EvaluationNotesMap"
    """<p>A map of question identifiers to note value.</p>"""
    status: "aws_sdk_connect.types.evaluation_status.EvaluationStatus"
    """<p>The status of the contact evaluation.</p>"""
    scores: NotRequired[
        "aws_sdk_connect.types.evaluation_scores_map.EvaluationScoresMap"
    ]
    """<p>A map of item (section or question) identifiers to score value.</p>"""
    created_time: "aws_sdk_connect.types.timestamp.Timestamp"
    """<p>The timestamp for when the evaluation was created.</p>"""
    last_modified_time: "aws_sdk_connect.types.timestamp.Timestamp"
    """<p>The timestamp for when the evaluation was last updated.</p>"""
    evaluation_type: NotRequired["aws_sdk_connect.types.evaluation_type.EvaluationType"]
    """<p>Type of the evaluation. </p>"""
    tags: NotRequired["aws_sdk_connect.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource. For example, { \"Tags\": {\"key1\":\"value1\", \"key2\":\"value2\"} }.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Evaluation) -> dict:
    out: dict = {}
    out["EvaluationId"] = value["evaluation_id"]
    out["EvaluationArn"] = value["evaluation_arn"]
    import aws_sdk_connect.types.evaluation_metadata

    out["Metadata"] = aws_sdk_connect.types.evaluation_metadata.serialize_json(
        value["metadata"]
    )
    import aws_sdk_connect.types.evaluation_answers_output_map

    out["Answers"] = aws_sdk_connect.types.evaluation_answers_output_map.serialize_json(
        value["answers"]
    )
    import aws_sdk_connect.types.evaluation_notes_map

    out["Notes"] = aws_sdk_connect.types.evaluation_notes_map.serialize_json(
        value["notes"]
    )
    import aws_sdk_connect.types.evaluation_status

    out["Status"] = aws_sdk_connect.types.evaluation_status.serialize_json(
        value["status"]
    )
    if "scores" in value:
        import aws_sdk_connect.types.evaluation_scores_map

        out["Scores"] = aws_sdk_connect.types.evaluation_scores_map.serialize_json(
            value["scores"]
        )
    import aws_sdk_connect.types.timestamp

    out["CreatedTime"] = aws_sdk_connect.types.timestamp.serialize_json(
        value["created_time"]
    )
    import aws_sdk_connect.types.timestamp

    out["LastModifiedTime"] = aws_sdk_connect.types.timestamp.serialize_json(
        value["last_modified_time"]
    )
    if "evaluation_type" in value:
        import aws_sdk_connect.types.evaluation_type

        out["EvaluationType"] = aws_sdk_connect.types.evaluation_type.serialize_json(
            value["evaluation_type"]
        )
    if "tags" in value:
        import aws_sdk_connect.types.tag_map

        out["Tags"] = aws_sdk_connect.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> Evaluation:
    out: Evaluation = {}  # type: ignore[typeddict-item]
    if "EvaluationId" in data:
        out["evaluation_id"] = data["EvaluationId"]
    else:
        raise DeserializationError("Evaluation.evaluation_id required")
    if "EvaluationArn" in data:
        out["evaluation_arn"] = data["EvaluationArn"]
    else:
        raise DeserializationError("Evaluation.evaluation_arn required")
    if "Metadata" in data:
        import aws_sdk_connect.types.evaluation_metadata

        out["metadata"] = aws_sdk_connect.types.evaluation_metadata.deserialize_json(
            data["Metadata"]
        )
    else:
        raise DeserializationError("Evaluation.metadata required")
    if "Answers" in data:
        import aws_sdk_connect.types.evaluation_answers_output_map

        out["answers"] = (
            aws_sdk_connect.types.evaluation_answers_output_map.deserialize_json(
                data["Answers"]
            )
        )
    else:
        raise DeserializationError("Evaluation.answers required")
    if "Notes" in data:
        import aws_sdk_connect.types.evaluation_notes_map

        out["notes"] = aws_sdk_connect.types.evaluation_notes_map.deserialize_json(
            data["Notes"]
        )
    else:
        raise DeserializationError("Evaluation.notes required")
    if "Status" in data:
        import aws_sdk_connect.types.evaluation_status

        out["status"] = aws_sdk_connect.types.evaluation_status.deserialize_json(
            data["Status"]
        )
    else:
        raise DeserializationError("Evaluation.status required")
    if "Scores" in data:
        import aws_sdk_connect.types.evaluation_scores_map

        out["scores"] = aws_sdk_connect.types.evaluation_scores_map.deserialize_json(
            data["Scores"]
        )
    if "CreatedTime" in data:
        import aws_sdk_connect.types.timestamp

        out["created_time"] = aws_sdk_connect.types.timestamp.deserialize_json(
            data["CreatedTime"]
        )
    else:
        raise DeserializationError("Evaluation.created_time required")
    if "LastModifiedTime" in data:
        import aws_sdk_connect.types.timestamp

        out["last_modified_time"] = aws_sdk_connect.types.timestamp.deserialize_json(
            data["LastModifiedTime"]
        )
    else:
        raise DeserializationError("Evaluation.last_modified_time required")
    if "EvaluationType" in data:
        import aws_sdk_connect.types.evaluation_type

        out["evaluation_type"] = aws_sdk_connect.types.evaluation_type.deserialize_json(
            data["EvaluationType"]
        )
    if "Tags" in data:
        import aws_sdk_connect.types.tag_map

        out["tags"] = aws_sdk_connect.types.tag_map.deserialize_json(data["Tags"])
    return out
