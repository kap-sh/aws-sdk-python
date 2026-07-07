"""Generated from Smithy shape ``com.amazonaws.customerprofiles#SourceFlowConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.connector_profile_name
    import aws_sdk_customer_profiles.types.incremental_pull_config
    import aws_sdk_customer_profiles.types.source_connector_properties
    import aws_sdk_customer_profiles.types.source_connector_type


class SourceFlowConfig(TypedDict, closed=True):
    connector_profile_name: NotRequired[
        "aws_sdk_customer_profiles.types.connector_profile_name.ConnectorProfileName"
    ]
    """<p>The name of the AppFlow connector profile. This name must be unique for each connector profile in the AWS account.</p>"""
    connector_type: (
        "aws_sdk_customer_profiles.types.source_connector_type.SourceConnectorType"
    )
    """<p>The type of connector, such as Salesforce, Marketo, and so on.</p>"""
    incremental_pull_config: NotRequired[
        "aws_sdk_customer_profiles.types.incremental_pull_config.IncrementalPullConfig"
    ]
    """<p>Defines the configuration for a scheduled incremental data pull. If a valid configuration is provided, the fields specified in the configuration are used when querying for the incremental data pull.</p>"""
    source_connector_properties: "aws_sdk_customer_profiles.types.source_connector_properties.SourceConnectorProperties"
    """<p>Specifies the information that is required to query a particular source connector.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SourceFlowConfig) -> dict:
    out: dict = {}
    if "connector_profile_name" in value:
        out["ConnectorProfileName"] = value["connector_profile_name"]
    import aws_sdk_customer_profiles.types.source_connector_type

    out["ConnectorType"] = (
        aws_sdk_customer_profiles.types.source_connector_type.serialize_json(
            value["connector_type"]
        )
    )
    if "incremental_pull_config" in value:
        import aws_sdk_customer_profiles.types.incremental_pull_config

        out["IncrementalPullConfig"] = (
            aws_sdk_customer_profiles.types.incremental_pull_config.serialize_json(
                value["incremental_pull_config"]
            )
        )
    import aws_sdk_customer_profiles.types.source_connector_properties

    out["SourceConnectorProperties"] = (
        aws_sdk_customer_profiles.types.source_connector_properties.serialize_json(
            value["source_connector_properties"]
        )
    )
    return out


def deserialize_json(data: dict) -> SourceFlowConfig:
    out: SourceFlowConfig = {}  # type: ignore[typeddict-item]
    if "ConnectorProfileName" in data:
        out["connector_profile_name"] = data["ConnectorProfileName"]
    if "ConnectorType" in data:
        import aws_sdk_customer_profiles.types.source_connector_type

        out["connector_type"] = (
            aws_sdk_customer_profiles.types.source_connector_type.deserialize_json(
                data["ConnectorType"]
            )
        )
    else:
        raise DeserializationError("SourceFlowConfig.connector_type required")
    if "IncrementalPullConfig" in data:
        import aws_sdk_customer_profiles.types.incremental_pull_config

        out["incremental_pull_config"] = (
            aws_sdk_customer_profiles.types.incremental_pull_config.deserialize_json(
                data["IncrementalPullConfig"]
            )
        )
    if "SourceConnectorProperties" in data:
        import aws_sdk_customer_profiles.types.source_connector_properties

        out["source_connector_properties"] = (
            aws_sdk_customer_profiles.types.source_connector_properties.deserialize_json(
                data["SourceConnectorProperties"]
            )
        )
    else:
        raise DeserializationError(
            "SourceFlowConfig.source_connector_properties required"
        )
    return out
