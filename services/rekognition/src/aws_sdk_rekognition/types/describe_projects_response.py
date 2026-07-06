"""Generated from Smithy shape ``com.amazonaws.rekognition#DescribeProjectsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.extended_pagination_token
    import aws_sdk_rekognition.types.project_descriptions


class DescribeProjectsResponse(TypedDict, closed=True):
    project_descriptions: NotRequired[
        "aws_sdk_rekognition.types.project_descriptions.ProjectDescriptions"
    ]
    """<p>A list of project descriptions. The list is sorted by the date and time the projects are created.</p>"""
    next_token: NotRequired[
        "aws_sdk_rekognition.types.extended_pagination_token.ExtendedPaginationToken"
    ]
    """<p>If the previous response was incomplete (because there is more results to retrieve), Amazon Rekognition returns a pagination token in the response. You can use this pagination token to retrieve the next set of results. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeProjectsResponse) -> dict:
    out: dict = {}
    if "project_descriptions" in value:
        import aws_sdk_rekognition.types.project_descriptions

        out["ProjectDescriptions"] = (
            aws_sdk_rekognition.types.project_descriptions.serialize_aws_json_1_1(
                value["project_descriptions"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeProjectsResponse:
    out: DescribeProjectsResponse = {}  # type: ignore[typeddict-item]
    if "ProjectDescriptions" in data:
        import aws_sdk_rekognition.types.project_descriptions

        out["project_descriptions"] = (
            aws_sdk_rekognition.types.project_descriptions.deserialize_aws_json_1_1(
                data["ProjectDescriptions"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
