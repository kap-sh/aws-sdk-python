"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#VariantConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.configuration_bundle_ref
    import aws_sdk_bedrock_agentcore.types.target_ref


class VariantConfiguration(TypedDict, closed=True):
    configuration_bundle: NotRequired[
        "aws_sdk_bedrock_agentcore.types.configuration_bundle_ref.ConfigurationBundleRef"
    ]
    """<p>A reference to a configuration bundle version to use for this variant.</p>"""
    target: NotRequired["aws_sdk_bedrock_agentcore.types.target_ref.TargetRef"]
    """<p>A reference to a gateway target to route traffic to for this variant.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VariantConfiguration) -> dict:
    out: dict = {}
    if "configuration_bundle" in value:
        import aws_sdk_bedrock_agentcore.types.configuration_bundle_ref

        out["configurationBundle"] = (
            aws_sdk_bedrock_agentcore.types.configuration_bundle_ref.serialize_json(
                value["configuration_bundle"]
            )
        )
    if "target" in value:
        import aws_sdk_bedrock_agentcore.types.target_ref

        out["target"] = aws_sdk_bedrock_agentcore.types.target_ref.serialize_json(
            value["target"]
        )
    return out


def deserialize_json(data: dict) -> VariantConfiguration:
    out: VariantConfiguration = {}  # type: ignore[typeddict-item]
    if "configurationBundle" in data:
        import aws_sdk_bedrock_agentcore.types.configuration_bundle_ref

        out["configuration_bundle"] = (
            aws_sdk_bedrock_agentcore.types.configuration_bundle_ref.deserialize_json(
                data["configurationBundle"]
            )
        )
    if "target" in data:
        import aws_sdk_bedrock_agentcore.types.target_ref

        out["target"] = aws_sdk_bedrock_agentcore.types.target_ref.deserialize_json(
            data["target"]
        )
    return out
