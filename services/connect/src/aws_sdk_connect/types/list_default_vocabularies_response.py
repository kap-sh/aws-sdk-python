"""Generated from Smithy shape ``com.amazonaws.connect#ListDefaultVocabulariesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.default_vocabulary_list
    import aws_sdk_connect.types.vocabulary_next_token


class ListDefaultVocabulariesResponse(TypedDict, closed=True):
    default_vocabulary_list: (
        "aws_sdk_connect.types.default_vocabulary_list.DefaultVocabularyList"
    )
    """<p>A list of default vocabularies.</p>"""
    next_token: NotRequired[
        "aws_sdk_connect.types.vocabulary_next_token.VocabularyNextToken"
    ]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDefaultVocabulariesResponse) -> dict:
    out: dict = {}
    import aws_sdk_connect.types.default_vocabulary_list

    out["DefaultVocabularyList"] = (
        aws_sdk_connect.types.default_vocabulary_list.serialize_json(
            value["default_vocabulary_list"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDefaultVocabulariesResponse:
    out: ListDefaultVocabulariesResponse = {}  # type: ignore[typeddict-item]
    if "DefaultVocabularyList" in data:
        import aws_sdk_connect.types.default_vocabulary_list

        out["default_vocabulary_list"] = (
            aws_sdk_connect.types.default_vocabulary_list.deserialize_json(
                data["DefaultVocabularyList"]
            )
        )
    else:
        raise DeserializationError(
            "ListDefaultVocabulariesResponse.default_vocabulary_list required"
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
