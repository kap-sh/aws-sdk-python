"""Generated from Smithy shape ``com.amazonaws.glue#GetClassifierResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.classifier


class GetClassifierResponse(TypedDict, closed=True):
    classifier: NotRequired["capo_glue.types.classifier.Classifier"]
    """<p>The requested classifier.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetClassifierResponse) -> dict:
    out: dict = {}
    if "classifier" in value:
        import capo_glue.types.classifier

        out["Classifier"] = capo_glue.types.classifier.serialize_aws_json_1_1(
            value["classifier"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetClassifierResponse:
    out: GetClassifierResponse = {}  # type: ignore[typeddict-item]
    if "Classifier" in data:
        import capo_glue.types.classifier

        out["classifier"] = capo_glue.types.classifier.deserialize_aws_json_1_1(
            data["Classifier"]
        )
    return out
