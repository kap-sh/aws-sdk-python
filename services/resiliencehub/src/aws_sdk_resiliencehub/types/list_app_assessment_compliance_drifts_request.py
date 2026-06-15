"""Generated from Smithy shape ``com.amazonaws.resiliencehub#ListAppAssessmentComplianceDriftsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.arn
    import aws_sdk_resiliencehub.types.max_results
    import aws_sdk_resiliencehub.types.next_token


class ListAppAssessmentComplianceDriftsRequest(TypedDict):
    assessment_arn: "aws_sdk_resiliencehub.types.arn.Arn"
    r"""<p>Amazon Resource Name (ARN) of the assessment. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app-assessment/<code>app-id</code>. For more information about ARNs, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>"""
    next_token: NotRequired["aws_sdk_resiliencehub.types.next_token.NextToken"]
    """<p>Null, or the token from a previous call to get the next set of results.</p>"""
    max_results: NotRequired["aws_sdk_resiliencehub.types.max_results.MaxResults"]
    """<p>Maximum number of compliance drifts requested.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAppAssessmentComplianceDriftsRequest) -> dict:
    out: dict = {}
    out["assessmentArn"] = value["assessment_arn"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> ListAppAssessmentComplianceDriftsRequest:
    out: ListAppAssessmentComplianceDriftsRequest = {}  # type: ignore[typeddict-item]
    if "assessmentArn" in data:
        out["assessment_arn"] = data["assessmentArn"]
    else:
        raise DeserializationError(
            "ListAppAssessmentComplianceDriftsRequest.assessment_arn required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
