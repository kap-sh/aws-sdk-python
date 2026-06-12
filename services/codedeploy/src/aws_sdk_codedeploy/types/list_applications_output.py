"""Generated from Smithy shape ``com.amazonaws.codedeploy#ListApplicationsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codedeploy.types.applications_list
    import aws_sdk_codedeploy.types.next_token


class ListApplicationsOutput(TypedDict):
    applications: NotRequired[
        "aws_sdk_codedeploy.types.applications_list.ApplicationsList"
    ]
    """<p>A list of application names.</p>"""
    next_token: NotRequired["aws_sdk_codedeploy.types.next_token.NextToken"]
    """<p>If a large amount of information is returned, an identifier is also returned. It can be used in a subsequent list applications call to return the next set of applications in the list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListApplicationsOutput) -> dict:
    out: dict = {}
    if "applications" in value:
        import aws_sdk_codedeploy.types.applications_list

        out["applications"] = (
            aws_sdk_codedeploy.types.applications_list.serialize_aws_json_1_1(
                value["applications"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListApplicationsOutput:
    out: ListApplicationsOutput = {}  # type: ignore[typeddict-item]
    if "applications" in data:
        import aws_sdk_codedeploy.types.applications_list

        out["applications"] = (
            aws_sdk_codedeploy.types.applications_list.deserialize_aws_json_1_1(
                data["applications"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
