"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ConfigurationBundleSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_bedrock_agentcore_control.types.configuration_bundle_arn
    import aws_sdk_bedrock_agentcore_control.types.configuration_bundle_description
    import aws_sdk_bedrock_agentcore_control.types.configuration_bundle_id
    import aws_sdk_bedrock_agentcore_control.types.configuration_bundle_name


class ConfigurationBundleSummary(TypedDict, closed=True):
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
    created_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the configuration bundle was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConfigurationBundleSummary) -> dict:
    out: dict = {}
    out["bundleArn"] = value["bundle_arn"]
    out["bundleId"] = value["bundle_id"]
    out["bundleName"] = value["bundle_name"]
    if "description" in value:
        out["description"] = value["description"]
    if "created_at" in value:
        import aws_sdk_bedrock_agentcore_control.types._prelude.timestamp

        out["createdAt"] = (
            aws_sdk_bedrock_agentcore_control.types._prelude.timestamp.serialize_json(
                value["created_at"]
            )
        )
    return out


def deserialize_json(data: dict) -> ConfigurationBundleSummary:
    out: ConfigurationBundleSummary = {}  # type: ignore[typeddict-item]
    if "bundleArn" in data:
        out["bundle_arn"] = data["bundleArn"]
    else:
        raise DeserializationError("ConfigurationBundleSummary.bundle_arn required")
    if "bundleId" in data:
        out["bundle_id"] = data["bundleId"]
    else:
        raise DeserializationError("ConfigurationBundleSummary.bundle_id required")
    if "bundleName" in data:
        out["bundle_name"] = data["bundleName"]
    else:
        raise DeserializationError("ConfigurationBundleSummary.bundle_name required")
    if "description" in data:
        out["description"] = data["description"]
    if "createdAt" in data:
        import aws_sdk_bedrock_agentcore_control.types._prelude.timestamp

        out["created_at"] = (
            aws_sdk_bedrock_agentcore_control.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    return out
