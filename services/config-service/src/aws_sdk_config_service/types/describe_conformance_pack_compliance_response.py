"""Generated from Smithy shape ``com.amazonaws.configservice#DescribeConformancePackComplianceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_config_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_config_service.types.conformance_pack_name
    import aws_sdk_config_service.types.conformance_pack_rule_compliance_list
    import aws_sdk_config_service.types.next_token


class DescribeConformancePackComplianceResponse(TypedDict):
    conformance_pack_name: (
        "aws_sdk_config_service.types.conformance_pack_name.ConformancePackName"
    )
    """<p>Name of the conformance pack.</p>"""
    conformance_pack_rule_compliance_list: "aws_sdk_config_service.types.conformance_pack_rule_compliance_list.ConformancePackRuleComplianceList"
    """<p>Returns a list of <code>ConformancePackRuleCompliance</code> objects.</p>"""
    next_token: NotRequired["aws_sdk_config_service.types.next_token.NextToken"]
    """<p>The <code>nextToken</code> string returned in a previous request that you use to request the next page of results in a paginated response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeConformancePackComplianceResponse) -> dict:
    out: dict = {}
    out["ConformancePackName"] = value["conformance_pack_name"]
    import aws_sdk_config_service.types.conformance_pack_rule_compliance_list

    out["ConformancePackRuleComplianceList"] = (
        aws_sdk_config_service.types.conformance_pack_rule_compliance_list.serialize_aws_json_1_1(
            value["conformance_pack_rule_compliance_list"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeConformancePackComplianceResponse:
    out: DescribeConformancePackComplianceResponse = {}  # type: ignore[typeddict-item]
    if "ConformancePackName" in data:
        out["conformance_pack_name"] = data["ConformancePackName"]
    else:
        raise DeserializationError(
            "DescribeConformancePackComplianceResponse.conformance_pack_name required"
        )
    if "ConformancePackRuleComplianceList" in data:
        import aws_sdk_config_service.types.conformance_pack_rule_compliance_list

        out["conformance_pack_rule_compliance_list"] = (
            aws_sdk_config_service.types.conformance_pack_rule_compliance_list.deserialize_aws_json_1_1(
                data["ConformancePackRuleComplianceList"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeConformancePackComplianceResponse.conformance_pack_rule_compliance_list required"
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
