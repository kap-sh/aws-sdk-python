"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#UnusedAccessConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.analysis_rule


class UnusedAccessConfiguration(TypedDict, closed=True):
    unused_access_age: NotRequired["int"]
    """<p>The specified access age in days for which to generate findings for unused access. For example, if you specify 90 days, the analyzer will generate findings for IAM entities within the accounts of the selected organization for any access that hasn't been used in 90 or more days since the analyzer's last scan. You can choose a value between 1 and 365 days.</p>"""
    analysis_rule: NotRequired[
        "aws_sdk_accessanalyzer.types.analysis_rule.AnalysisRule"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: UnusedAccessConfiguration) -> dict:
    out: dict = {}
    if "unused_access_age" in value:
        out["unusedAccessAge"] = value["unused_access_age"]
    if "analysis_rule" in value:
        import aws_sdk_accessanalyzer.types.analysis_rule

        out["analysisRule"] = aws_sdk_accessanalyzer.types.analysis_rule.serialize_json(
            value["analysis_rule"]
        )
    return out


def deserialize_json(data: dict) -> UnusedAccessConfiguration:
    out: UnusedAccessConfiguration = {}  # type: ignore[typeddict-item]
    if "unusedAccessAge" in data:
        out["unused_access_age"] = data["unusedAccessAge"]
    if "analysisRule" in data:
        import aws_sdk_accessanalyzer.types.analysis_rule

        out["analysis_rule"] = (
            aws_sdk_accessanalyzer.types.analysis_rule.deserialize_json(
                data["analysisRule"]
            )
        )
    return out
