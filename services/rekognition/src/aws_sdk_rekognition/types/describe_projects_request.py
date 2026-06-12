"""Generated from Smithy shape ``com.amazonaws.rekognition#DescribeProjectsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.customization_features
    import aws_sdk_rekognition.types.extended_pagination_token
    import aws_sdk_rekognition.types.project_names
    import aws_sdk_rekognition.types.projects_page_size


class DescribeProjectsRequest(TypedDict):
    next_token: NotRequired[
        "aws_sdk_rekognition.types.extended_pagination_token.ExtendedPaginationToken"
    ]
    """<p>If the previous response was incomplete (because there is more results to retrieve), Rekognition returns a pagination token in the response. You can use this pagination token to retrieve the next set of results. </p>"""
    max_results: NotRequired[
        "aws_sdk_rekognition.types.projects_page_size.ProjectsPageSize"
    ]
    """<p>The maximum number of results to return per paginated call. The largest value you can specify is 100. If you specify a value greater than 100, a ValidationException error occurs. The default value is 100. </p>"""
    project_names: NotRequired["aws_sdk_rekognition.types.project_names.ProjectNames"]
    """<p>A list of the projects that you want Rekognition to describe. If you don't specify a value, the response includes descriptions for all the projects in your AWS account.</p>"""
    features: NotRequired[
        "aws_sdk_rekognition.types.customization_features.CustomizationFeatures"
    ]
    """<p>Specifies the type of customization to filter projects by. If no value is specified, CUSTOM_LABELS is used as a default.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeProjectsRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "project_names" in value:
        import aws_sdk_rekognition.types.project_names

        out["ProjectNames"] = (
            aws_sdk_rekognition.types.project_names.serialize_aws_json_1_1(
                value["project_names"]
            )
        )
    if "features" in value:
        import aws_sdk_rekognition.types.customization_features

        out["Features"] = (
            aws_sdk_rekognition.types.customization_features.serialize_aws_json_1_1(
                value["features"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeProjectsRequest:
    out: DescribeProjectsRequest = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "ProjectNames" in data:
        import aws_sdk_rekognition.types.project_names

        out["project_names"] = (
            aws_sdk_rekognition.types.project_names.deserialize_aws_json_1_1(
                data["ProjectNames"]
            )
        )
    if "Features" in data:
        import aws_sdk_rekognition.types.customization_features

        out["features"] = (
            aws_sdk_rekognition.types.customization_features.deserialize_aws_json_1_1(
                data["Features"]
            )
        )
    return out
