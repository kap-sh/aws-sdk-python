"""Generated from Smithy shape ``com.amazonaws.securityhub#Remediation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.recommendation


class Remediation(TypedDict, closed=True):
    recommendation: NotRequired["capo_securityhub.types.recommendation.Recommendation"]
    """<p>A recommendation on the steps to take to remediate the issue identified by a finding.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Remediation) -> dict:
    out: dict = {}
    if "recommendation" in value:
        import capo_securityhub.types.recommendation

        out["Recommendation"] = capo_securityhub.types.recommendation.serialize_json(
            value["recommendation"]
        )
    return out


def deserialize_json(data: dict) -> Remediation:
    out: Remediation = {}  # type: ignore[typeddict-item]
    if "Recommendation" in data:
        import capo_securityhub.types.recommendation

        out["recommendation"] = capo_securityhub.types.recommendation.deserialize_json(
            data["Recommendation"]
        )
    return out
