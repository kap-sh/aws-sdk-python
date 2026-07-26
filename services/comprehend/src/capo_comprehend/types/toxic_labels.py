"""Generated from Smithy shape ``com.amazonaws.comprehend#ToxicLabels``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.float
    import capo_comprehend.types.list_of_toxic_content


class ToxicLabels(TypedDict, closed=True):
    labels: NotRequired[
        "capo_comprehend.types.list_of_toxic_content.ListOfToxicContent"
    ]
    """<p>Array of toxic content types identified in the string.</p>"""
    toxicity: NotRequired["capo_comprehend.types.float.Float"]
    """<p>Overall toxicity score for the string. Value range is zero to one, where one is the highest confidence.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ToxicLabels) -> dict:
    out: dict = {}
    if "labels" in value:
        import capo_comprehend.types.list_of_toxic_content

        out["Labels"] = (
            capo_comprehend.types.list_of_toxic_content.serialize_aws_json_1_1(
                value["labels"]
            )
        )
    if "toxicity" in value:
        out["Toxicity"] = value["toxicity"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ToxicLabels:
    out: ToxicLabels = {}  # type: ignore[typeddict-item]
    if "Labels" in data:
        import capo_comprehend.types.list_of_toxic_content

        out["labels"] = (
            capo_comprehend.types.list_of_toxic_content.deserialize_aws_json_1_1(
                data["Labels"]
            )
        )
    if "Toxicity" in data:
        out["toxicity"] = data["Toxicity"]
    return out
