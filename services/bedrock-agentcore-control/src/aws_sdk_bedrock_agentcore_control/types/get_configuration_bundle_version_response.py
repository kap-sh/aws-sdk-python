"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GetConfigurationBundleVersionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_bedrock_agentcore_control.types.component_configuration_map
    import aws_sdk_bedrock_agentcore_control.types.configuration_bundle_arn
    import aws_sdk_bedrock_agentcore_control.types.configuration_bundle_description
    import aws_sdk_bedrock_agentcore_control.types.configuration_bundle_id
    import aws_sdk_bedrock_agentcore_control.types.configuration_bundle_name
    import aws_sdk_bedrock_agentcore_control.types.configuration_bundle_version
    import aws_sdk_bedrock_agentcore_control.types.version_lineage_metadata


class GetConfigurationBundleVersionResponse(TypedDict):
    bundle_arn: "aws_sdk_bedrock_agentcore_control.types.configuration_bundle_arn.ConfigurationBundleArn"
    """<p>The Amazon Resource Name (ARN) of the configuration bundle.</p>"""
    bundle_id: "aws_sdk_bedrock_agentcore_control.types.configuration_bundle_id.ConfigurationBundleId"
    """<p>The unique identifier of the configuration bundle.</p>"""
    bundle_name: "aws_sdk_bedrock_agentcore_control.types.configuration_bundle_name.ConfigurationBundleName"
    """<p>The name of the configuration bundle.</p>"""
    description: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.configuration_bundle_description.ConfigurationBundleDescription"
    ]
    """<p>The description of the configuration bundle.</p>"""
    version_id: "aws_sdk_bedrock_agentcore_control.types.configuration_bundle_version.ConfigurationBundleVersion"
    """<p>The version identifier of this configuration bundle version.</p>"""
    components: "aws_sdk_bedrock_agentcore_control.types.component_configuration_map.ComponentConfigurationMap"
    """<p>A map of component identifiers to their configurations for this version.</p>"""
    lineage_metadata: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.version_lineage_metadata.VersionLineageMetadata"
    ]
    """<p>The version lineage metadata, including parent versions, branch name, and creation source.</p>"""
    created_at: "datetime.datetime"
    """<p>The timestamp when the configuration bundle was created.</p>"""
    version_created_at: "datetime.datetime"
    """<p>The timestamp when this specific version was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetConfigurationBundleVersionResponse) -> dict:
    out: dict = {}
    out["bundleArn"] = value["bundle_arn"]
    out["bundleId"] = value["bundle_id"]
    out["bundleName"] = value["bundle_name"]
    if "description" in value:
        out["description"] = value["description"]
    out["versionId"] = value["version_id"]
    import aws_sdk_bedrock_agentcore_control.types.component_configuration_map

    out["components"] = (
        aws_sdk_bedrock_agentcore_control.types.component_configuration_map.serialize_json(
            value["components"]
        )
    )
    if "lineage_metadata" in value:
        import aws_sdk_bedrock_agentcore_control.types.version_lineage_metadata

        out["lineageMetadata"] = (
            aws_sdk_bedrock_agentcore_control.types.version_lineage_metadata.serialize_json(
                value["lineage_metadata"]
            )
        )
    import aws_sdk_bedrock_agentcore_control.types._prelude.timestamp

    out["createdAt"] = (
        aws_sdk_bedrock_agentcore_control.types._prelude.timestamp.serialize_json(
            value["created_at"]
        )
    )
    import aws_sdk_bedrock_agentcore_control.types._prelude.timestamp

    out["versionCreatedAt"] = (
        aws_sdk_bedrock_agentcore_control.types._prelude.timestamp.serialize_json(
            value["version_created_at"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetConfigurationBundleVersionResponse:
    out: GetConfigurationBundleVersionResponse = {}  # type: ignore[typeddict-item]
    if "bundleArn" in data:
        out["bundle_arn"] = data["bundleArn"]
    else:
        raise DeserializationError(
            "GetConfigurationBundleVersionResponse.bundle_arn required"
        )
    if "bundleId" in data:
        out["bundle_id"] = data["bundleId"]
    else:
        raise DeserializationError(
            "GetConfigurationBundleVersionResponse.bundle_id required"
        )
    if "bundleName" in data:
        out["bundle_name"] = data["bundleName"]
    else:
        raise DeserializationError(
            "GetConfigurationBundleVersionResponse.bundle_name required"
        )
    if "description" in data:
        out["description"] = data["description"]
    if "versionId" in data:
        out["version_id"] = data["versionId"]
    else:
        raise DeserializationError(
            "GetConfigurationBundleVersionResponse.version_id required"
        )
    if "components" in data:
        import aws_sdk_bedrock_agentcore_control.types.component_configuration_map

        out["components"] = (
            aws_sdk_bedrock_agentcore_control.types.component_configuration_map.deserialize_json(
                data["components"]
            )
        )
    else:
        raise DeserializationError(
            "GetConfigurationBundleVersionResponse.components required"
        )
    if "lineageMetadata" in data:
        import aws_sdk_bedrock_agentcore_control.types.version_lineage_metadata

        out["lineage_metadata"] = (
            aws_sdk_bedrock_agentcore_control.types.version_lineage_metadata.deserialize_json(
                data["lineageMetadata"]
            )
        )
    if "createdAt" in data:
        import aws_sdk_bedrock_agentcore_control.types._prelude.timestamp

        out["created_at"] = (
            aws_sdk_bedrock_agentcore_control.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError(
            "GetConfigurationBundleVersionResponse.created_at required"
        )
    if "versionCreatedAt" in data:
        import aws_sdk_bedrock_agentcore_control.types._prelude.timestamp

        out["version_created_at"] = (
            aws_sdk_bedrock_agentcore_control.types._prelude.timestamp.deserialize_json(
                data["versionCreatedAt"]
            )
        )
    else:
        raise DeserializationError(
            "GetConfigurationBundleVersionResponse.version_created_at required"
        )
    return out
