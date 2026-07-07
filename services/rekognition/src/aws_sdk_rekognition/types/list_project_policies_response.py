"""Generated from Smithy shape ``com.amazonaws.rekognition#ListProjectPoliciesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.extended_pagination_token
    import aws_sdk_rekognition.types.project_policies


class ListProjectPoliciesResponse(TypedDict, closed=True):
    project_policies: NotRequired[
        "aws_sdk_rekognition.types.project_policies.ProjectPolicies"
    ]
    """<p>A list of project policies attached to the project.</p>"""
    next_token: NotRequired[
        "aws_sdk_rekognition.types.extended_pagination_token.ExtendedPaginationToken"
    ]
    """<p>If the response is truncated, Amazon Rekognition returns this token that you can use in the subsequent request to retrieve the next set of project policies.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListProjectPoliciesResponse) -> dict:
    out: dict = {}
    if "project_policies" in value:
        import aws_sdk_rekognition.types.project_policies

        out["ProjectPolicies"] = (
            aws_sdk_rekognition.types.project_policies.serialize_aws_json_1_1(
                value["project_policies"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListProjectPoliciesResponse:
    out: ListProjectPoliciesResponse = {}  # type: ignore[typeddict-item]
    if "ProjectPolicies" in data:
        import aws_sdk_rekognition.types.project_policies

        out["project_policies"] = (
            aws_sdk_rekognition.types.project_policies.deserialize_aws_json_1_1(
                data["ProjectPolicies"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
