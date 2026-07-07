"""Generated from Smithy shape ``com.amazonaws.connect#DeleteVocabularyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.arn
    import aws_sdk_connect.types.vocabulary_id
    import aws_sdk_connect.types.vocabulary_state


class DeleteVocabularyResponse(TypedDict, closed=True):
    vocabulary_arn: "aws_sdk_connect.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) of the custom vocabulary.</p>"""
    vocabulary_id: "aws_sdk_connect.types.vocabulary_id.VocabularyId"
    """<p>The identifier of the custom vocabulary.</p>"""
    state: "aws_sdk_connect.types.vocabulary_state.VocabularyState"
    """<p>The current state of the custom vocabulary.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteVocabularyResponse) -> dict:
    out: dict = {}
    out["VocabularyArn"] = value["vocabulary_arn"]
    out["VocabularyId"] = value["vocabulary_id"]
    import aws_sdk_connect.types.vocabulary_state

    out["State"] = aws_sdk_connect.types.vocabulary_state.serialize_json(value["state"])
    return out


def deserialize_json(data: dict) -> DeleteVocabularyResponse:
    out: DeleteVocabularyResponse = {}  # type: ignore[typeddict-item]
    if "VocabularyArn" in data:
        out["vocabulary_arn"] = data["VocabularyArn"]
    else:
        raise DeserializationError("DeleteVocabularyResponse.vocabulary_arn required")
    if "VocabularyId" in data:
        out["vocabulary_id"] = data["VocabularyId"]
    else:
        raise DeserializationError("DeleteVocabularyResponse.vocabulary_id required")
    if "State" in data:
        import aws_sdk_connect.types.vocabulary_state

        out["state"] = aws_sdk_connect.types.vocabulary_state.deserialize_json(
            data["State"]
        )
    else:
        raise DeserializationError("DeleteVocabularyResponse.state required")
    return out
