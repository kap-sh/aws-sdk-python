"""Generated from Smithy shape ``com.amazonaws.frauddetector#GetLabelsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.identifier
    import aws_sdk_frauddetector.types.labels_max_results
    import aws_sdk_frauddetector.types.string


class GetLabelsRequest(TypedDict):
    name: NotRequired["aws_sdk_frauddetector.types.identifier.identifier"]
    """<p>The name of the label or labels to get.</p>"""
    next_token: NotRequired["aws_sdk_frauddetector.types.string.string"]
    """<p>The next token for the subsequent request.</p>"""
    max_results: NotRequired[
        "aws_sdk_frauddetector.types.labels_max_results.labelsMaxResults"
    ]
    """<p>The maximum number of objects to return for the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetLabelsRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetLabelsRequest:
    out: GetLabelsRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
