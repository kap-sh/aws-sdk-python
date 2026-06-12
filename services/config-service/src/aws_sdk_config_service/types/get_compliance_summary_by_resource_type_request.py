"""Generated from Smithy shape ``com.amazonaws.configservice#GetComplianceSummaryByResourceTypeRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_config_service.types.resource_types


class GetComplianceSummaryByResourceTypeRequest(TypedDict):
    resource_types: NotRequired[
        "aws_sdk_config_service.types.resource_types.ResourceTypes"
    ]
    """<p>Specify one or more resource types to get the number of resources that are compliant and the number that are noncompliant for each resource type.</p> <p>For this request, you can specify an Amazon Web Services resource type such as <code>AWS::EC2::Instance</code>. You can specify that the resource type is an Amazon Web Services account by specifying <code>AWS::::Account</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetComplianceSummaryByResourceTypeRequest) -> dict:
    out: dict = {}
    if "resource_types" in value:
        import aws_sdk_config_service.types.resource_types

        out["ResourceTypes"] = (
            aws_sdk_config_service.types.resource_types.serialize_aws_json_1_1(
                value["resource_types"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetComplianceSummaryByResourceTypeRequest:
    out: GetComplianceSummaryByResourceTypeRequest = {}  # type: ignore[typeddict-item]
    if "ResourceTypes" in data:
        import aws_sdk_config_service.types.resource_types

        out["resource_types"] = (
            aws_sdk_config_service.types.resource_types.deserialize_aws_json_1_1(
                data["ResourceTypes"]
            )
        )
    return out
