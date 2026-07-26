"""Generated from Smithy shape ``com.amazonaws.configservice#ListConformancePackComplianceScoresResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_config_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_config_service.types.conformance_pack_compliance_scores
    import capo_config_service.types.next_token


class ListConformancePackComplianceScoresResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_config_service.types.next_token.NextToken"]
    """<p>The <code>nextToken</code> string that you can use to get the next page of results in a paginated response.</p>"""
    conformance_pack_compliance_scores: "capo_config_service.types.conformance_pack_compliance_scores.ConformancePackComplianceScores"
    """<p>A list of <code>ConformancePackComplianceScore</code> objects.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListConformancePackComplianceScoresResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    import capo_config_service.types.conformance_pack_compliance_scores

    out["ConformancePackComplianceScores"] = (
        capo_config_service.types.conformance_pack_compliance_scores.serialize_aws_json_1_1(
            value["conformance_pack_compliance_scores"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListConformancePackComplianceScoresResponse:
    out: ListConformancePackComplianceScoresResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "ConformancePackComplianceScores" in data:
        import capo_config_service.types.conformance_pack_compliance_scores

        out["conformance_pack_compliance_scores"] = (
            capo_config_service.types.conformance_pack_compliance_scores.deserialize_aws_json_1_1(
                data["ConformancePackComplianceScores"]
            )
        )
    else:
        raise DeserializationError(
            "ListConformancePackComplianceScoresResponse.conformance_pack_compliance_scores required"
        )
    return out
