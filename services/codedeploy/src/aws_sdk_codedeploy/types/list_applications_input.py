"""Generated from Smithy shape ``com.amazonaws.codedeploy#ListApplicationsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codedeploy.types.next_token


class ListApplicationsInput(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_codedeploy.types.next_token.NextToken"]
    """<p>An identifier returned from the previous list applications call. It can be used to return the next set of applications in the list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListApplicationsInput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListApplicationsInput:
    out: ListApplicationsInput = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
