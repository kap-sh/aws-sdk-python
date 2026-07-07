"""Generated from Smithy shape ``com.amazonaws.configservice#GetConformancePackComplianceDetailsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_config_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_config_service.types.conformance_pack_evaluation_filters
    import aws_sdk_config_service.types.conformance_pack_name
    import aws_sdk_config_service.types.get_conformance_pack_compliance_details_limit
    import aws_sdk_config_service.types.next_token


class GetConformancePackComplianceDetailsRequest(TypedDict, closed=True):
    conformance_pack_name: (
        "aws_sdk_config_service.types.conformance_pack_name.ConformancePackName"
    )
    """<p>Name of the conformance pack.</p>"""
    filters: NotRequired[
        "aws_sdk_config_service.types.conformance_pack_evaluation_filters.ConformancePackEvaluationFilters"
    ]
    """<p>A <code>ConformancePackEvaluationFilters</code> object.</p>"""
    limit: "aws_sdk_config_service.types.get_conformance_pack_compliance_details_limit.GetConformancePackComplianceDetailsLimit"
    """<p>The maximum number of evaluation results returned on each page. If you do no specify a number, Config uses the default. The default is 100.</p>"""
    next_token: NotRequired["aws_sdk_config_service.types.next_token.NextToken"]
    """<p>The <code>nextToken</code> string returned in a previous request that you use to request the next page of results in a paginated response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetConformancePackComplianceDetailsRequest) -> dict:
    out: dict = {}
    out["ConformancePackName"] = value["conformance_pack_name"]
    if "filters" in value:
        import aws_sdk_config_service.types.conformance_pack_evaluation_filters

        out["Filters"] = (
            aws_sdk_config_service.types.conformance_pack_evaluation_filters.serialize_aws_json_1_1(
                value["filters"]
            )
        )
    out["Limit"] = value.get("limit", 0)
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetConformancePackComplianceDetailsRequest:
    out: GetConformancePackComplianceDetailsRequest = {}  # type: ignore[typeddict-item]
    if "ConformancePackName" in data:
        out["conformance_pack_name"] = data["ConformancePackName"]
    else:
        raise DeserializationError(
            "GetConformancePackComplianceDetailsRequest.conformance_pack_name required"
        )
    if "Filters" in data:
        import aws_sdk_config_service.types.conformance_pack_evaluation_filters

        out["filters"] = (
            aws_sdk_config_service.types.conformance_pack_evaluation_filters.deserialize_aws_json_1_1(
                data["Filters"]
            )
        )
    if "Limit" in data:
        out["limit"] = data["Limit"]
    else:
        out["limit"] = 0
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
