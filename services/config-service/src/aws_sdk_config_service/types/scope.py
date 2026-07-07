"""Generated from Smithy shape ``com.amazonaws.configservice#Scope``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_config_service.types.base_resource_id
    import aws_sdk_config_service.types.compliance_resource_types
    import aws_sdk_config_service.types.service_principals
    import aws_sdk_config_service.types.string_with_char_limit128
    import aws_sdk_config_service.types.string_with_char_limit256


class Scope(TypedDict, closed=True):
    compliance_resource_types: NotRequired[
        "aws_sdk_config_service.types.compliance_resource_types.ComplianceResourceTypes"
    ]
    """<p>The resource types of only those Amazon Web Services resources that you want to trigger an evaluation for the rule. You can only specify one type if you also specify a resource ID for <code>ComplianceResourceId</code>.</p>"""
    tag_key: NotRequired[
        "aws_sdk_config_service.types.string_with_char_limit128.StringWithCharLimit128"
    ]
    """<p>The tag key that is applied to only those Amazon Web Services resources that you want to trigger an evaluation for the rule.</p>"""
    tag_value: NotRequired[
        "aws_sdk_config_service.types.string_with_char_limit256.StringWithCharLimit256"
    ]
    """<p>The tag value applied to only those Amazon Web Services resources that you want to trigger an evaluation for the rule. If you specify a value for <code>TagValue</code>, you must also specify a value for <code>TagKey</code>.</p>"""
    compliance_resource_id: NotRequired[
        "aws_sdk_config_service.types.base_resource_id.BaseResourceId"
    ]
    """<p>The ID of the only Amazon Web Services resource that you want to trigger an evaluation for the rule. If you specify a resource ID, you must specify one resource type for <code>ComplianceResourceTypes</code>.</p>"""
    service_principals: NotRequired[
        "aws_sdk_config_service.types.service_principals.ServicePrincipals"
    ]
    """<p>The service principals of the Amazon Web Services services for the rule.</p> <note> <p>The field is populated only if the service-linked rule is created by a service. The field is empty if you create your own rule.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Scope) -> dict:
    out: dict = {}
    if "compliance_resource_types" in value:
        import aws_sdk_config_service.types.compliance_resource_types

        out["ComplianceResourceTypes"] = (
            aws_sdk_config_service.types.compliance_resource_types.serialize_aws_json_1_1(
                value["compliance_resource_types"]
            )
        )
    if "tag_key" in value:
        out["TagKey"] = value["tag_key"]
    if "tag_value" in value:
        out["TagValue"] = value["tag_value"]
    if "compliance_resource_id" in value:
        out["ComplianceResourceId"] = value["compliance_resource_id"]
    if "service_principals" in value:
        import aws_sdk_config_service.types.service_principals

        out["ServicePrincipals"] = (
            aws_sdk_config_service.types.service_principals.serialize_aws_json_1_1(
                value["service_principals"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Scope:
    out: Scope = {}  # type: ignore[typeddict-item]
    if "ComplianceResourceTypes" in data:
        import aws_sdk_config_service.types.compliance_resource_types

        out["compliance_resource_types"] = (
            aws_sdk_config_service.types.compliance_resource_types.deserialize_aws_json_1_1(
                data["ComplianceResourceTypes"]
            )
        )
    if "TagKey" in data:
        out["tag_key"] = data["TagKey"]
    if "TagValue" in data:
        out["tag_value"] = data["TagValue"]
    if "ComplianceResourceId" in data:
        out["compliance_resource_id"] = data["ComplianceResourceId"]
    if "ServicePrincipals" in data:
        import aws_sdk_config_service.types.service_principals

        out["service_principals"] = (
            aws_sdk_config_service.types.service_principals.deserialize_aws_json_1_1(
                data["ServicePrincipals"]
            )
        )
    return out
