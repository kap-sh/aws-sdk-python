"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#InternalAccessConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_accessanalyzer.types.internal_access_analysis_rule


class InternalAccessConfiguration(TypedDict, closed=True):
    analysis_rule: NotRequired[
        "capo_accessanalyzer.types.internal_access_analysis_rule.InternalAccessAnalysisRule"
    ]
    """<p>Contains information about analysis rules for the internal access analyzer. These rules determine which resources and access patterns will be analyzed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InternalAccessConfiguration) -> dict:
    out: dict = {}
    if "analysis_rule" in value:
        import capo_accessanalyzer.types.internal_access_analysis_rule

        out["analysisRule"] = (
            capo_accessanalyzer.types.internal_access_analysis_rule.serialize_json(
                value["analysis_rule"]
            )
        )
    return out


def deserialize_json(data: dict) -> InternalAccessConfiguration:
    out: InternalAccessConfiguration = {}  # type: ignore[typeddict-item]
    if "analysisRule" in data:
        import capo_accessanalyzer.types.internal_access_analysis_rule

        out["analysis_rule"] = (
            capo_accessanalyzer.types.internal_access_analysis_rule.deserialize_json(
                data["analysisRule"]
            )
        )
    return out
