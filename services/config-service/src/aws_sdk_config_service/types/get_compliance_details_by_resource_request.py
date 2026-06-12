"""Generated from Smithy shape ``com.amazonaws.configservice#GetComplianceDetailsByResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_config_service.types.base_resource_id
    import aws_sdk_config_service.types.compliance_types
    import aws_sdk_config_service.types.resource_evaluation_id
    import aws_sdk_config_service.types.string
    import aws_sdk_config_service.types.string_with_char_limit256


class GetComplianceDetailsByResourceRequest(TypedDict):
    resource_type: NotRequired[
        "aws_sdk_config_service.types.string_with_char_limit256.StringWithCharLimit256"
    ]
    """<p>The type of the Amazon Web Services resource for which you want compliance information.</p>"""
    resource_id: NotRequired[
        "aws_sdk_config_service.types.base_resource_id.BaseResourceId"
    ]
    """<p>The ID of the Amazon Web Services resource for which you want compliance information.</p>"""
    compliance_types: NotRequired[
        "aws_sdk_config_service.types.compliance_types.ComplianceTypes"
    ]
    """<p>Filters the results by compliance.</p> <p> <code>INSUFFICIENT_DATA</code> is a valid <code>ComplianceType</code> that is returned when an Config rule cannot be evaluated. However, <code>INSUFFICIENT_DATA</code> cannot be used as a <code>ComplianceType</code> for filtering results.</p>"""
    next_token: NotRequired["aws_sdk_config_service.types.string.String"]
    """<p>The <code>nextToken</code> string returned on a previous page that you use to get the next page of results in a paginated response.</p>"""
    resource_evaluation_id: NotRequired[
        "aws_sdk_config_service.types.resource_evaluation_id.ResourceEvaluationId"
    ]
    """<p>The unique ID of Amazon Web Services resource execution for which you want to retrieve evaluation results. </p> <note> <p>You need to only provide either a <code>ResourceEvaluationID</code> or a <code>ResourceID </code>and <code>ResourceType</code>.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetComplianceDetailsByResourceRequest) -> dict:
    out: dict = {}
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    if "resource_id" in value:
        out["ResourceId"] = value["resource_id"]
    if "compliance_types" in value:
        import aws_sdk_config_service.types.compliance_types

        out["ComplianceTypes"] = (
            aws_sdk_config_service.types.compliance_types.serialize_aws_json_1_1(
                value["compliance_types"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "resource_evaluation_id" in value:
        out["ResourceEvaluationId"] = value["resource_evaluation_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetComplianceDetailsByResourceRequest:
    out: GetComplianceDetailsByResourceRequest = {}  # type: ignore[typeddict-item]
    if "ResourceType" in data:
        out["resource_type"] = data["ResourceType"]
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    if "ComplianceTypes" in data:
        import aws_sdk_config_service.types.compliance_types

        out["compliance_types"] = (
            aws_sdk_config_service.types.compliance_types.deserialize_aws_json_1_1(
                data["ComplianceTypes"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "ResourceEvaluationId" in data:
        out["resource_evaluation_id"] = data["ResourceEvaluationId"]
    return out
