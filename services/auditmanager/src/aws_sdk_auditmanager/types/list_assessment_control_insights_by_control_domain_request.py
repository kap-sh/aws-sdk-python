"""Generated from Smithy shape ``com.amazonaws.auditmanager#ListAssessmentControlInsightsByControlDomainRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.control_domain_id
    import aws_sdk_auditmanager.types.max_results
    import aws_sdk_auditmanager.types.token
    import aws_sdk_auditmanager.types.uuid


class ListAssessmentControlInsightsByControlDomainRequest(TypedDict):
    control_domain_id: "aws_sdk_auditmanager.types.control_domain_id.ControlDomainId"
    """<p>The unique identifier for the control domain. </p> <p>Audit Manager supports the control domains that are provided by Amazon Web Services Control Catalog. For information about how to find a list of available control domains, see <a href=\"https://docs.aws.amazon.com/controlcatalog/latest/APIReference/API_ListDomains.html\"> <code>ListDomains</code> </a> in the Amazon Web Services Control Catalog API Reference.</p>"""
    assessment_id: "aws_sdk_auditmanager.types.uuid.UUID"
    """<p>The unique identifier for the active assessment. </p>"""
    next_token: NotRequired["aws_sdk_auditmanager.types.token.Token"]
    """<p>The pagination token that's used to fetch the next set of results. </p>"""
    max_results: NotRequired["aws_sdk_auditmanager.types.max_results.MaxResults"]
    """<p>Represents the maximum number of results on a page or for an API request call. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAssessmentControlInsightsByControlDomainRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAssessmentControlInsightsByControlDomainRequest:
    out: ListAssessmentControlInsightsByControlDomainRequest = {}  # type: ignore[typeddict-item]
    return out
