"""Generated from Smithy shape ``com.amazonaws.support#TrustedAdvisorResourcesSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_support.types.long


class TrustedAdvisorResourcesSummary(TypedDict, closed=True):
    resources_processed: "capo_support.types.long.Long"
    """<p>The number of Amazon Web Services resources that were analyzed by the Trusted Advisor check.</p>"""
    resources_flagged: "capo_support.types.long.Long"
    """<p>The number of Amazon Web Services resources that were flagged (listed) by the Trusted Advisor check.</p>"""
    resources_ignored: "capo_support.types.long.Long"
    """<p>The number of Amazon Web Services resources ignored by Trusted Advisor because information was unavailable.</p>"""
    resources_suppressed: "capo_support.types.long.Long"
    """<p>The number of Amazon Web Services resources ignored by Trusted Advisor because they were marked as suppressed by the user.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrustedAdvisorResourcesSummary) -> dict:
    out: dict = {}
    out["resourcesProcessed"] = value.get("resources_processed", 0)
    out["resourcesFlagged"] = value.get("resources_flagged", 0)
    out["resourcesIgnored"] = value.get("resources_ignored", 0)
    out["resourcesSuppressed"] = value.get("resources_suppressed", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> TrustedAdvisorResourcesSummary:
    out: TrustedAdvisorResourcesSummary = {}  # type: ignore[typeddict-item]
    if "resourcesProcessed" in data:
        out["resources_processed"] = data["resourcesProcessed"]
    else:
        out["resources_processed"] = 0
    if "resourcesFlagged" in data:
        out["resources_flagged"] = data["resourcesFlagged"]
    else:
        out["resources_flagged"] = 0
    if "resourcesIgnored" in data:
        out["resources_ignored"] = data["resourcesIgnored"]
    else:
        out["resources_ignored"] = 0
    if "resourcesSuppressed" in data:
        out["resources_suppressed"] = data["resourcesSuppressed"]
    else:
        out["resources_suppressed"] = 0
    return out
