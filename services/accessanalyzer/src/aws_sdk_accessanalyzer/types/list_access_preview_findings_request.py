"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#ListAccessPreviewFindingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_accessanalyzer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.access_preview_id
    import aws_sdk_accessanalyzer.types.analyzer_arn
    import aws_sdk_accessanalyzer.types.filter_criteria_map
    import aws_sdk_accessanalyzer.types.token


class ListAccessPreviewFindingsRequest(TypedDict, closed=True):
    access_preview_id: "aws_sdk_accessanalyzer.types.access_preview_id.AccessPreviewId"
    """<p>The unique ID for the access preview.</p>"""
    analyzer_arn: "aws_sdk_accessanalyzer.types.analyzer_arn.AnalyzerArn"
    r"""<p>The <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-getting-started.html#permission-resources\">ARN of the analyzer</a> used to generate the access.</p>"""
    filter: NotRequired[
        "aws_sdk_accessanalyzer.types.filter_criteria_map.FilterCriteriaMap"
    ]
    """<p>Criteria to filter the returned findings.</p>"""
    next_token: NotRequired["aws_sdk_accessanalyzer.types.token.Token"]
    """<p>A token used for pagination of results returned.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of results to return in the response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAccessPreviewFindingsRequest) -> dict:
    out: dict = {}
    out["analyzerArn"] = value["analyzer_arn"]
    if "filter" in value:
        import aws_sdk_accessanalyzer.types.filter_criteria_map

        out["filter"] = aws_sdk_accessanalyzer.types.filter_criteria_map.serialize_json(
            value["filter"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> ListAccessPreviewFindingsRequest:
    out: ListAccessPreviewFindingsRequest = {}  # type: ignore[typeddict-item]
    if "analyzerArn" in data:
        out["analyzer_arn"] = data["analyzerArn"]
    else:
        raise DeserializationError(
            "ListAccessPreviewFindingsRequest.analyzer_arn required"
        )
    if "filter" in data:
        import aws_sdk_accessanalyzer.types.filter_criteria_map

        out["filter"] = (
            aws_sdk_accessanalyzer.types.filter_criteria_map.deserialize_json(
                data["filter"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
