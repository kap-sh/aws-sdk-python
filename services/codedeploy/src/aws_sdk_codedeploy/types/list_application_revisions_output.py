"""Generated from Smithy shape ``com.amazonaws.codedeploy#ListApplicationRevisionsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codedeploy.types.next_token
    import aws_sdk_codedeploy.types.revision_location_list


class ListApplicationRevisionsOutput(TypedDict):
    revisions: NotRequired[
        "aws_sdk_codedeploy.types.revision_location_list.RevisionLocationList"
    ]
    """<p>A list of locations that contain the matching revisions.</p>"""
    next_token: NotRequired["aws_sdk_codedeploy.types.next_token.NextToken"]
    """<p>If a large amount of information is returned, an identifier is also returned. It can be used in a subsequent list application revisions call to return the next set of application revisions in the list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListApplicationRevisionsOutput) -> dict:
    out: dict = {}
    if "revisions" in value:
        import aws_sdk_codedeploy.types.revision_location_list

        out["revisions"] = (
            aws_sdk_codedeploy.types.revision_location_list.serialize_aws_json_1_1(
                value["revisions"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListApplicationRevisionsOutput:
    out: ListApplicationRevisionsOutput = {}  # type: ignore[typeddict-item]
    if "revisions" in data:
        import aws_sdk_codedeploy.types.revision_location_list

        out["revisions"] = (
            aws_sdk_codedeploy.types.revision_location_list.deserialize_aws_json_1_1(
                data["revisions"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
