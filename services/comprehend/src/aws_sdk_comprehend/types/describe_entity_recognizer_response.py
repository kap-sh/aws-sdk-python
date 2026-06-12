"""Generated from Smithy shape ``com.amazonaws.comprehend#DescribeEntityRecognizerResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.entity_recognizer_properties


class DescribeEntityRecognizerResponse(TypedDict):
    entity_recognizer_properties: NotRequired[
        "aws_sdk_comprehend.types.entity_recognizer_properties.EntityRecognizerProperties"
    ]
    """<p>Describes information associated with an entity recognizer.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEntityRecognizerResponse) -> dict:
    out: dict = {}
    if "entity_recognizer_properties" in value:
        import aws_sdk_comprehend.types.entity_recognizer_properties

        out["EntityRecognizerProperties"] = (
            aws_sdk_comprehend.types.entity_recognizer_properties.serialize_aws_json_1_1(
                value["entity_recognizer_properties"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeEntityRecognizerResponse:
    out: DescribeEntityRecognizerResponse = {}  # type: ignore[typeddict-item]
    if "EntityRecognizerProperties" in data:
        import aws_sdk_comprehend.types.entity_recognizer_properties

        out["entity_recognizer_properties"] = (
            aws_sdk_comprehend.types.entity_recognizer_properties.deserialize_aws_json_1_1(
                data["EntityRecognizerProperties"]
            )
        )
    return out
