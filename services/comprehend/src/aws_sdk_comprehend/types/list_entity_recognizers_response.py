"""Generated from Smithy shape ``com.amazonaws.comprehend#ListEntityRecognizersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.entity_recognizer_properties_list
    import aws_sdk_comprehend.types.string


class ListEntityRecognizersResponse(TypedDict, closed=True):
    entity_recognizer_properties_list: NotRequired[
        "aws_sdk_comprehend.types.entity_recognizer_properties_list.EntityRecognizerPropertiesList"
    ]
    """<p>The list of properties of an entity recognizer.</p>"""
    next_token: NotRequired["aws_sdk_comprehend.types.string.String"]
    """<p>Identifies the next page of results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListEntityRecognizersResponse) -> dict:
    out: dict = {}
    if "entity_recognizer_properties_list" in value:
        import aws_sdk_comprehend.types.entity_recognizer_properties_list

        out["EntityRecognizerPropertiesList"] = (
            aws_sdk_comprehend.types.entity_recognizer_properties_list.serialize_aws_json_1_1(
                value["entity_recognizer_properties_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListEntityRecognizersResponse:
    out: ListEntityRecognizersResponse = {}  # type: ignore[typeddict-item]
    if "EntityRecognizerPropertiesList" in data:
        import aws_sdk_comprehend.types.entity_recognizer_properties_list

        out["entity_recognizer_properties_list"] = (
            aws_sdk_comprehend.types.entity_recognizer_properties_list.deserialize_aws_json_1_1(
                data["EntityRecognizerPropertiesList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
