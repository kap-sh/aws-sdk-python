"""Generated from Smithy shape ``com.amazonaws.comprehend#DetectPiiEntitiesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.list_of_pii_entities


class DetectPiiEntitiesResponse(TypedDict):
    entities: NotRequired[
        "aws_sdk_comprehend.types.list_of_pii_entities.ListOfPiiEntities"
    ]
    """<p>A collection of PII entities identified in the input text. For each entity, the response provides the entity type, where the entity text begins and ends, and the level of confidence that Amazon Comprehend has in the detection.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DetectPiiEntitiesResponse) -> dict:
    out: dict = {}
    if "entities" in value:
        import aws_sdk_comprehend.types.list_of_pii_entities

        out["Entities"] = (
            aws_sdk_comprehend.types.list_of_pii_entities.serialize_aws_json_1_1(
                value["entities"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DetectPiiEntitiesResponse:
    out: DetectPiiEntitiesResponse = {}  # type: ignore[typeddict-item]
    if "Entities" in data:
        import aws_sdk_comprehend.types.list_of_pii_entities

        out["entities"] = (
            aws_sdk_comprehend.types.list_of_pii_entities.deserialize_aws_json_1_1(
                data["Entities"]
            )
        )
    return out
