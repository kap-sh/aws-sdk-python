"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#VariantConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.configuration_bundle_ref
    import capo_bedrock_agentcore.types.target_ref


class VariantConfiguration(TypedDict, closed=True):
    configuration_bundle: NotRequired[
        "capo_bedrock_agentcore.types.configuration_bundle_ref.ConfigurationBundleRef"
    ]
    """<p>A reference to a configuration bundle version to use for this variant.</p>"""
    target: NotRequired["capo_bedrock_agentcore.types.target_ref.TargetRef"]
    """<p>A reference to a gateway target to route traffic to for this variant.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VariantConfiguration) -> dict:
    out: dict = {}
    if "configuration_bundle" in value:
        import capo_bedrock_agentcore.types.configuration_bundle_ref

        out["configurationBundle"] = (
            capo_bedrock_agentcore.types.configuration_bundle_ref.serialize_json(
                value["configuration_bundle"]
            )
        )
    if "target" in value:
        import capo_bedrock_agentcore.types.target_ref

        out["target"] = capo_bedrock_agentcore.types.target_ref.serialize_json(
            value["target"]
        )
    return out


def deserialize_json(data: dict) -> VariantConfiguration:
    out: VariantConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("configurationBundle") is not None:
        import capo_bedrock_agentcore.types.configuration_bundle_ref

        out["configuration_bundle"] = (
            capo_bedrock_agentcore.types.configuration_bundle_ref.deserialize_json(
                data["configurationBundle"]
            )
        )
    if data.get("target") is not None:
        import capo_bedrock_agentcore.types.target_ref

        out["target"] = capo_bedrock_agentcore.types.target_ref.deserialize_json(
            data["target"]
        )
    return out
