"""Generated from Smithy shape ``com.amazonaws.sesv2#GetEmailIdentityPoliciesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.policy_map


class GetEmailIdentityPoliciesResponse(TypedDict, closed=True):
    policies: NotRequired["aws_sdk_sesv2.types.policy_map.PolicyMap"]
    """<p>A map of policy names to policies.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEmailIdentityPoliciesResponse) -> dict:
    out: dict = {}
    if "policies" in value:
        import aws_sdk_sesv2.types.policy_map

        out["Policies"] = aws_sdk_sesv2.types.policy_map.serialize_json(
            value["policies"]
        )
    return out


def deserialize_json(data: dict) -> GetEmailIdentityPoliciesResponse:
    out: GetEmailIdentityPoliciesResponse = {}  # type: ignore[typeddict-item]
    if "Policies" in data:
        import aws_sdk_sesv2.types.policy_map

        out["policies"] = aws_sdk_sesv2.types.policy_map.deserialize_json(
            data["Policies"]
        )
    return out
