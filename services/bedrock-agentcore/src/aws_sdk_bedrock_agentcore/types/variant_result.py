"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#VariantResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.confidence_interval


class VariantResult(TypedDict):
    variant_name: "str"
    """<p>The name of the treatment variant.</p>"""
    sample_size: "int"
    """<p>The number of sessions evaluated for this variant.</p>"""
    mean: "float"
    """<p>The mean evaluation score for this variant.</p>"""
    absolute_change: NotRequired["float"]
    """<p>The absolute change in mean score compared to the control variant.</p>"""
    percent_change: NotRequired["float"]
    """<p>The percentage change in mean score compared to the control variant.</p>"""
    p_value: NotRequired["float"]
    """<p>The p-value indicating the statistical significance of the observed difference.</p>"""
    confidence_interval: NotRequired[
        "aws_sdk_bedrock_agentcore.types.confidence_interval.ConfidenceInterval"
    ]
    """<p>The confidence interval for the observed difference.</p>"""
    is_significant: "bool"
    """<p>Whether the observed difference is statistically significant.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VariantResult) -> dict:
    out: dict = {}
    out["variantName"] = value["variant_name"]
    out["sampleSize"] = value["sample_size"]
    out["mean"] = value["mean"]
    if "absolute_change" in value:
        out["absoluteChange"] = value["absolute_change"]
    if "percent_change" in value:
        out["percentChange"] = value["percent_change"]
    if "p_value" in value:
        out["pValue"] = value["p_value"]
    if "confidence_interval" in value:
        import aws_sdk_bedrock_agentcore.types.confidence_interval

        out["confidenceInterval"] = (
            aws_sdk_bedrock_agentcore.types.confidence_interval.serialize_json(
                value["confidence_interval"]
            )
        )
    out["isSignificant"] = value["is_significant"]
    return out


def deserialize_json(data: dict) -> VariantResult:
    out: VariantResult = {}  # type: ignore[typeddict-item]
    if "variantName" in data:
        out["variant_name"] = data["variantName"]
    else:
        raise DeserializationError("VariantResult.variant_name required")
    if "sampleSize" in data:
        out["sample_size"] = data["sampleSize"]
    else:
        raise DeserializationError("VariantResult.sample_size required")
    if "mean" in data:
        out["mean"] = data["mean"]
    else:
        raise DeserializationError("VariantResult.mean required")
    if "absoluteChange" in data:
        out["absolute_change"] = data["absoluteChange"]
    if "percentChange" in data:
        out["percent_change"] = data["percentChange"]
    if "pValue" in data:
        out["p_value"] = data["pValue"]
    if "confidenceInterval" in data:
        import aws_sdk_bedrock_agentcore.types.confidence_interval

        out["confidence_interval"] = (
            aws_sdk_bedrock_agentcore.types.confidence_interval.deserialize_json(
                data["confidenceInterval"]
            )
        )
    if "isSignificant" in data:
        out["is_significant"] = data["isSignificant"]
    else:
        raise DeserializationError("VariantResult.is_significant required")
    return out
