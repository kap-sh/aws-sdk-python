"""Generated from Smithy shape ``com.amazonaws.codegurusecurity#Remediation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codeguru_security.types.recommendation
    import aws_sdk_codeguru_security.types.suggested_fixes


class Remediation(TypedDict):
    recommendation: NotRequired[
        "aws_sdk_codeguru_security.types.recommendation.Recommendation"
    ]
    """<p>An object that contains information about the recommended course of action to remediate a finding.</p>"""
    suggested_fixes: NotRequired[
        "aws_sdk_codeguru_security.types.suggested_fixes.SuggestedFixes"
    ]
    """<p>A list of <code>SuggestedFix</code> objects. Each object contains information about a suggested code fix to remediate the finding.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Remediation) -> dict:
    out: dict = {}
    if "recommendation" in value:
        import aws_sdk_codeguru_security.types.recommendation

        out["recommendation"] = (
            aws_sdk_codeguru_security.types.recommendation.serialize_json(
                value["recommendation"]
            )
        )
    if "suggested_fixes" in value:
        import aws_sdk_codeguru_security.types.suggested_fixes

        out["suggestedFixes"] = (
            aws_sdk_codeguru_security.types.suggested_fixes.serialize_json(
                value["suggested_fixes"]
            )
        )
    return out


def deserialize_json(data: dict) -> Remediation:
    out: Remediation = {}  # type: ignore[typeddict-item]
    if "recommendation" in data:
        import aws_sdk_codeguru_security.types.recommendation

        out["recommendation"] = (
            aws_sdk_codeguru_security.types.recommendation.deserialize_json(
                data["recommendation"]
            )
        )
    if "suggestedFixes" in data:
        import aws_sdk_codeguru_security.types.suggested_fixes

        out["suggested_fixes"] = (
            aws_sdk_codeguru_security.types.suggested_fixes.deserialize_json(
                data["suggestedFixes"]
            )
        )
    return out
