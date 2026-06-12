"""Generated from Smithy shape ``com.amazonaws.auditmanager#ListAssessmentFrameworksRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.framework_type
    import aws_sdk_auditmanager.types.max_results
    import aws_sdk_auditmanager.types.token


class ListAssessmentFrameworksRequest(TypedDict):
    framework_type: "aws_sdk_auditmanager.types.framework_type.FrameworkType"
    """<p> The type of framework, such as a standard framework or a custom framework. </p>"""
    next_token: NotRequired["aws_sdk_auditmanager.types.token.Token"]
    """<p> The pagination token that's used to fetch the next set of results. </p>"""
    max_results: NotRequired["aws_sdk_auditmanager.types.max_results.MaxResults"]
    """<p> Represents the maximum number of results on a page or for an API request call. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAssessmentFrameworksRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAssessmentFrameworksRequest:
    out: ListAssessmentFrameworksRequest = {}  # type: ignore[typeddict-item]
    return out
