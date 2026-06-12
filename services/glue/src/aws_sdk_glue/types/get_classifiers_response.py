"""Generated from Smithy shape ``com.amazonaws.glue#GetClassifiersResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.classifier_list
    import aws_sdk_glue.types.token


class GetClassifiersResponse(TypedDict):
    classifiers: NotRequired["aws_sdk_glue.types.classifier_list.ClassifierList"]
    """<p>The requested list of classifier objects.</p>"""
    next_token: NotRequired["aws_sdk_glue.types.token.Token"]
    """<p>A continuation token.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetClassifiersResponse) -> dict:
    out: dict = {}
    if "classifiers" in value:
        import aws_sdk_glue.types.classifier_list

        out["Classifiers"] = aws_sdk_glue.types.classifier_list.serialize_aws_json_1_1(
            value["classifiers"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetClassifiersResponse:
    out: GetClassifiersResponse = {}  # type: ignore[typeddict-item]
    if "Classifiers" in data:
        import aws_sdk_glue.types.classifier_list

        out["classifiers"] = (
            aws_sdk_glue.types.classifier_list.deserialize_aws_json_1_1(
                data["Classifiers"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
