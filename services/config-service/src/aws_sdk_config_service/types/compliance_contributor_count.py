"""Generated from Smithy shape ``com.amazonaws.configservice#ComplianceContributorCount``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_config_service.types.boolean
    import aws_sdk_config_service.types.integer


class ComplianceContributorCount(TypedDict, closed=True):
    capped_count: "aws_sdk_config_service.types.integer.Integer"
    """<p>The number of Amazon Web Services resources or Config rules responsible for the current compliance of the item.</p>"""
    cap_exceeded: "aws_sdk_config_service.types.boolean.Boolean"
    """<p>Indicates whether the maximum count is reached.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ComplianceContributorCount) -> dict:
    out: dict = {}
    out["CappedCount"] = value.get("capped_count", 0)
    out["CapExceeded"] = value.get("cap_exceeded", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> ComplianceContributorCount:
    out: ComplianceContributorCount = {}  # type: ignore[typeddict-item]
    if "CappedCount" in data:
        out["capped_count"] = data["CappedCount"]
    else:
        out["capped_count"] = 0
    if "CapExceeded" in data:
        out["cap_exceeded"] = data["CapExceeded"]
    else:
        out["cap_exceeded"] = False
    return out
