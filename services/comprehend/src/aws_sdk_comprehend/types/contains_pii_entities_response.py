"""Generated from Smithy shape ``com.amazonaws.comprehend#ContainsPiiEntitiesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.list_of_entity_labels


class ContainsPiiEntitiesResponse(TypedDict, closed=True):
    labels: NotRequired[
        "aws_sdk_comprehend.types.list_of_entity_labels.ListOfEntityLabels"
    ]
    """<p>The labels used in the document being analyzed. Individual labels represent personally identifiable information (PII) entity types.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainsPiiEntitiesResponse) -> dict:
    out: dict = {}
    if "labels" in value:
        import aws_sdk_comprehend.types.list_of_entity_labels

        out["Labels"] = (
            aws_sdk_comprehend.types.list_of_entity_labels.serialize_aws_json_1_1(
                value["labels"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ContainsPiiEntitiesResponse:
    out: ContainsPiiEntitiesResponse = {}  # type: ignore[typeddict-item]
    if "Labels" in data:
        import aws_sdk_comprehend.types.list_of_entity_labels

        out["labels"] = (
            aws_sdk_comprehend.types.list_of_entity_labels.deserialize_aws_json_1_1(
                data["Labels"]
            )
        )
    return out
