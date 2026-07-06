"""Generated from Smithy shape ``com.amazonaws.customerprofiles#AppflowIntegrationWorkflowAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.connector_profile_name
    import aws_sdk_customer_profiles.types.source_connector_type
    import aws_sdk_customer_profiles.types.string1_to255


class AppflowIntegrationWorkflowAttributes(TypedDict, closed=True):
    source_connector_type: (
        "aws_sdk_customer_profiles.types.source_connector_type.SourceConnectorType"
    )
    """<p>Specifies the source connector type, such as Salesforce, ServiceNow, and Marketo. Indicates source of ingestion.</p>"""
    connector_profile_name: (
        "aws_sdk_customer_profiles.types.connector_profile_name.ConnectorProfileName"
    )
    """<p>The name of the AppFlow connector profile used for ingestion.</p>"""
    role_arn: NotRequired["aws_sdk_customer_profiles.types.string1_to255.string1To255"]
    """<p>The Amazon Resource Name (ARN) of the IAM role. Customer Profiles assumes this role to create resources on your behalf as part of workflow execution.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AppflowIntegrationWorkflowAttributes) -> dict:
    out: dict = {}
    import aws_sdk_customer_profiles.types.source_connector_type

    out["SourceConnectorType"] = (
        aws_sdk_customer_profiles.types.source_connector_type.serialize_json(
            value["source_connector_type"]
        )
    )
    out["ConnectorProfileName"] = value["connector_profile_name"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> AppflowIntegrationWorkflowAttributes:
    out: AppflowIntegrationWorkflowAttributes = {}  # type: ignore[typeddict-item]
    if "SourceConnectorType" in data:
        import aws_sdk_customer_profiles.types.source_connector_type

        out["source_connector_type"] = (
            aws_sdk_customer_profiles.types.source_connector_type.deserialize_json(
                data["SourceConnectorType"]
            )
        )
    else:
        raise DeserializationError(
            "AppflowIntegrationWorkflowAttributes.source_connector_type required"
        )
    if "ConnectorProfileName" in data:
        out["connector_profile_name"] = data["ConnectorProfileName"]
    else:
        raise DeserializationError(
            "AppflowIntegrationWorkflowAttributes.connector_profile_name required"
        )
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    return out
