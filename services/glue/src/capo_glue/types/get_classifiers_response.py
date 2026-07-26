"""Generated from Smithy shape ``com.amazonaws.glue#GetClassifiersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.classifier_list
    import capo_glue.types.token


class GetClassifiersResponse(TypedDict, closed=True):
    classifiers: NotRequired["capo_glue.types.classifier_list.ClassifierList"]
    """<p>The requested list of classifier objects.</p>"""
    next_token: NotRequired["capo_glue.types.token.Token"]
    """<p>A continuation token.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetClassifiersResponse) -> dict:
    out: dict = {}
    if "classifiers" in value:
        import capo_glue.types.classifier_list

        out["Classifiers"] = capo_glue.types.classifier_list.serialize_aws_json_1_1(
            value["classifiers"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetClassifiersResponse:
    out: GetClassifiersResponse = {}  # type: ignore[typeddict-item]
    if "Classifiers" in data:
        import capo_glue.types.classifier_list

        out["classifiers"] = capo_glue.types.classifier_list.deserialize_aws_json_1_1(
            data["Classifiers"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
