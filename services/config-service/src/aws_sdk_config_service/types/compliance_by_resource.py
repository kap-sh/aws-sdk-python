"""Generated from Smithy shape ``com.amazonaws.configservice#ComplianceByResource``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_config_service.types.base_resource_id
    import aws_sdk_config_service.types.compliance
    import aws_sdk_config_service.types.string_with_char_limit256


class ComplianceByResource(TypedDict):
    resource_type: NotRequired[
        "aws_sdk_config_service.types.string_with_char_limit256.StringWithCharLimit256"
    ]
    """<p>The type of the Amazon Web Services resource that was evaluated.</p>"""
    resource_id: NotRequired[
        "aws_sdk_config_service.types.base_resource_id.BaseResourceId"
    ]
    """<p>The ID of the Amazon Web Services resource that was evaluated.</p>"""
    compliance: NotRequired["aws_sdk_config_service.types.compliance.Compliance"]
    """<p>Indicates whether the Amazon Web Services resource complies with all of the Config rules that evaluated it.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ComplianceByResource) -> dict:
    out: dict = {}
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    if "resource_id" in value:
        out["ResourceId"] = value["resource_id"]
    if "compliance" in value:
        import aws_sdk_config_service.types.compliance

        out["Compliance"] = (
            aws_sdk_config_service.types.compliance.serialize_aws_json_1_1(
                value["compliance"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ComplianceByResource:
    out: ComplianceByResource = {}  # type: ignore[typeddict-item]
    if "ResourceType" in data:
        out["resource_type"] = data["ResourceType"]
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    if "Compliance" in data:
        import aws_sdk_config_service.types.compliance

        out["compliance"] = (
            aws_sdk_config_service.types.compliance.deserialize_aws_json_1_1(
                data["Compliance"]
            )
        )
    return out
