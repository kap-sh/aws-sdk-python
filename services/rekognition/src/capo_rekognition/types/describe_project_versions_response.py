"""Generated from Smithy shape ``com.amazonaws.rekognition#DescribeProjectVersionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.extended_pagination_token
    import capo_rekognition.types.project_version_descriptions


class DescribeProjectVersionsResponse(TypedDict, closed=True):
    project_version_descriptions: NotRequired[
        "capo_rekognition.types.project_version_descriptions.ProjectVersionDescriptions"
    ]
    """<p>A list of project version descriptions. The list is sorted by the creation date and time of the project versions, latest to earliest.</p>"""
    next_token: NotRequired[
        "capo_rekognition.types.extended_pagination_token.ExtendedPaginationToken"
    ]
    """<p>If the previous response was incomplete (because there is more results to retrieve), Amazon Rekognition returns a pagination token in the response. You can use this pagination token to retrieve the next set of results. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeProjectVersionsResponse) -> dict:
    out: dict = {}
    if "project_version_descriptions" in value:
        import capo_rekognition.types.project_version_descriptions

        out["ProjectVersionDescriptions"] = (
            capo_rekognition.types.project_version_descriptions.serialize_aws_json_1_1(
                value["project_version_descriptions"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeProjectVersionsResponse:
    out: DescribeProjectVersionsResponse = {}  # type: ignore[typeddict-item]
    if "ProjectVersionDescriptions" in data:
        import capo_rekognition.types.project_version_descriptions

        out["project_version_descriptions"] = (
            capo_rekognition.types.project_version_descriptions.deserialize_aws_json_1_1(
                data["ProjectVersionDescriptions"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
