"""Generated from Smithy shape ``com.amazonaws.bedrock#SupportTerm``."""

from typing import TypedDict

from typing_extensions import NotRequired


class SupportTerm(TypedDict):
    refund_policy_description: NotRequired["str"]
    """<p>Describes the refund policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SupportTerm) -> dict:
    out: dict = {}
    if "refund_policy_description" in value:
        out["refundPolicyDescription"] = value["refund_policy_description"]
    return out


def deserialize_json(data: dict) -> SupportTerm:
    out: SupportTerm = {}  # type: ignore[typeddict-item]
    if "refundPolicyDescription" in data:
        out["refund_policy_description"] = data["refundPolicyDescription"]
    return out
