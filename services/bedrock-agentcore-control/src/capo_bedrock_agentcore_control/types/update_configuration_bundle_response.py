"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#UpdateConfigurationBundleResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_bedrock_agentcore_control.types.configuration_bundle_arn
    import capo_bedrock_agentcore_control.types.configuration_bundle_id
    import capo_bedrock_agentcore_control.types.configuration_bundle_version


class UpdateConfigurationBundleResponse(TypedDict, closed=True):
    bundle_arn: "capo_bedrock_agentcore_control.types.configuration_bundle_arn.ConfigurationBundleArn"
    """<p>The Amazon Resource Name (ARN) of the updated configuration bundle.</p>"""
    bundle_id: "capo_bedrock_agentcore_control.types.configuration_bundle_id.ConfigurationBundleId"
    """<p>The unique identifier of the updated configuration bundle.</p>"""
    version_id: "capo_bedrock_agentcore_control.types.configuration_bundle_version.ConfigurationBundleVersion"
    """<p>The new version identifier created by this update.</p>"""
    updated_at: "datetime.datetime"
    """<p>The timestamp when the configuration bundle was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateConfigurationBundleResponse) -> dict:
    out: dict = {}
    out["bundleArn"] = value["bundle_arn"]
    out["bundleId"] = value["bundle_id"]
    out["versionId"] = value["version_id"]
    import capo_bedrock_agentcore_control.types._prelude.timestamp

    out["updatedAt"] = (
        capo_bedrock_agentcore_control.types._prelude.timestamp.serialize_json(
            value["updated_at"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateConfigurationBundleResponse:
    out: UpdateConfigurationBundleResponse = {}  # type: ignore[typeddict-item]
    if "bundleArn" in data:
        out["bundle_arn"] = data["bundleArn"]
    else:
        raise DeserializationError(
            "UpdateConfigurationBundleResponse.bundle_arn required"
        )
    if "bundleId" in data:
        out["bundle_id"] = data["bundleId"]
    else:
        raise DeserializationError(
            "UpdateConfigurationBundleResponse.bundle_id required"
        )
    if "versionId" in data:
        out["version_id"] = data["versionId"]
    else:
        raise DeserializationError(
            "UpdateConfigurationBundleResponse.version_id required"
        )
    if "updatedAt" in data:
        import capo_bedrock_agentcore_control.types._prelude.timestamp

        out["updated_at"] = (
            capo_bedrock_agentcore_control.types._prelude.timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateConfigurationBundleResponse.updated_at required"
        )
    return out
