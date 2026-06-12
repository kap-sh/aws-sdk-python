"""Generated from Smithy shape ``com.amazonaws.codedeploy#ListDeploymentGroupsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_codedeploy.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codedeploy.types.application_name
    import aws_sdk_codedeploy.types.next_token


class ListDeploymentGroupsInput(TypedDict):
    application_name: "aws_sdk_codedeploy.types.application_name.ApplicationName"
    """<p>The name of an CodeDeploy application associated with the user or Amazon Web Services account.</p>"""
    next_token: NotRequired["aws_sdk_codedeploy.types.next_token.NextToken"]
    """<p>An identifier returned from the previous list deployment groups call. It can be used to return the next set of deployment groups in the list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDeploymentGroupsInput) -> dict:
    out: dict = {}
    out["applicationName"] = value["application_name"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDeploymentGroupsInput:
    out: ListDeploymentGroupsInput = {}  # type: ignore[typeddict-item]
    if "applicationName" in data:
        out["application_name"] = data["applicationName"]
    else:
        raise DeserializationError(
            "ListDeploymentGroupsInput.application_name required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
