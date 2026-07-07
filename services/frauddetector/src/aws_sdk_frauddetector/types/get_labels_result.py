"""Generated from Smithy shape ``com.amazonaws.frauddetector#GetLabelsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.label_list
    import aws_sdk_frauddetector.types.string


class GetLabelsResult(TypedDict, closed=True):
    labels: NotRequired["aws_sdk_frauddetector.types.label_list.labelList"]
    """<p>An array of labels.</p>"""
    next_token: NotRequired["aws_sdk_frauddetector.types.string.string"]
    """<p>The next page token.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetLabelsResult) -> dict:
    out: dict = {}
    if "labels" in value:
        import aws_sdk_frauddetector.types.label_list

        out["labels"] = aws_sdk_frauddetector.types.label_list.serialize_aws_json_1_1(
            value["labels"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetLabelsResult:
    out: GetLabelsResult = {}  # type: ignore[typeddict-item]
    if "labels" in data:
        import aws_sdk_frauddetector.types.label_list

        out["labels"] = aws_sdk_frauddetector.types.label_list.deserialize_aws_json_1_1(
            data["labels"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
