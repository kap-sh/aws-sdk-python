"""Generated from Smithy shape ``com.amazonaws.cleanrooms#GetSchemaAnalysisRuleOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.analysis_rule


class GetSchemaAnalysisRuleOutput(TypedDict):
    analysis_rule: "aws_sdk_cleanrooms.types.analysis_rule.AnalysisRule"
    """<p>A specification about how data from the configured table can be used.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSchemaAnalysisRuleOutput) -> dict:
    out: dict = {}
    import aws_sdk_cleanrooms.types.analysis_rule

    out["analysisRule"] = aws_sdk_cleanrooms.types.analysis_rule.serialize_json(
        value["analysis_rule"]
    )
    return out


def deserialize_json(data: dict) -> GetSchemaAnalysisRuleOutput:
    out: GetSchemaAnalysisRuleOutput = {}  # type: ignore[typeddict-item]
    if "analysisRule" in data:
        import aws_sdk_cleanrooms.types.analysis_rule

        out["analysis_rule"] = aws_sdk_cleanrooms.types.analysis_rule.deserialize_json(
            data["analysisRule"]
        )
    else:
        raise DeserializationError("GetSchemaAnalysisRuleOutput.analysis_rule required")
    return out
