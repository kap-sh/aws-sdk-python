"""Generated from Smithy shape ``com.amazonaws.configservice#DescribeAggregateComplianceByConformancePacksResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_config_service.types.aggregate_compliance_by_conformance_pack_list
    import aws_sdk_config_service.types.next_token


class DescribeAggregateComplianceByConformancePacksResponse(TypedDict, closed=True):
    aggregate_compliance_by_conformance_packs: NotRequired[
        "aws_sdk_config_service.types.aggregate_compliance_by_conformance_pack_list.AggregateComplianceByConformancePackList"
    ]
    """<p>Returns the <code>AggregateComplianceByConformancePack</code> object.</p>"""
    next_token: NotRequired["aws_sdk_config_service.types.next_token.NextToken"]
    """<p>The <code>nextToken</code> string returned on a previous page that you use to get the next page of results in a paginated response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DescribeAggregateComplianceByConformancePacksResponse,
) -> dict:
    out: dict = {}
    if "aggregate_compliance_by_conformance_packs" in value:
        import aws_sdk_config_service.types.aggregate_compliance_by_conformance_pack_list

        out["AggregateComplianceByConformancePacks"] = (
            aws_sdk_config_service.types.aggregate_compliance_by_conformance_pack_list.serialize_aws_json_1_1(
                value["aggregate_compliance_by_conformance_packs"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DescribeAggregateComplianceByConformancePacksResponse:
    out: DescribeAggregateComplianceByConformancePacksResponse = {}  # type: ignore[typeddict-item]
    if "AggregateComplianceByConformancePacks" in data:
        import aws_sdk_config_service.types.aggregate_compliance_by_conformance_pack_list

        out["aggregate_compliance_by_conformance_packs"] = (
            aws_sdk_config_service.types.aggregate_compliance_by_conformance_pack_list.deserialize_aws_json_1_1(
                data["AggregateComplianceByConformancePacks"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
