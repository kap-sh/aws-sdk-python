"""Generated from Smithy shape ``com.amazonaws.comprehend#BatchDetectEntitiesItemResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.integer
    import aws_sdk_comprehend.types.list_of_entities


class BatchDetectEntitiesItemResult(TypedDict):
    index: NotRequired["aws_sdk_comprehend.types.integer.Integer"]
    """<p>The zero-based index of the document in the input list.</p>"""
    entities: NotRequired["aws_sdk_comprehend.types.list_of_entities.ListOfEntities"]
    """<p>One or more <a>Entity</a> objects, one for each entity detected in the document.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchDetectEntitiesItemResult) -> dict:
    out: dict = {}
    if "index" in value:
        out["Index"] = value["index"]
    if "entities" in value:
        import aws_sdk_comprehend.types.list_of_entities

        out["Entities"] = (
            aws_sdk_comprehend.types.list_of_entities.serialize_aws_json_1_1(
                value["entities"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchDetectEntitiesItemResult:
    out: BatchDetectEntitiesItemResult = {}  # type: ignore[typeddict-item]
    if "Index" in data:
        out["index"] = data["Index"]
    if "Entities" in data:
        import aws_sdk_comprehend.types.list_of_entities

        out["entities"] = (
            aws_sdk_comprehend.types.list_of_entities.deserialize_aws_json_1_1(
                data["Entities"]
            )
        )
    return out
