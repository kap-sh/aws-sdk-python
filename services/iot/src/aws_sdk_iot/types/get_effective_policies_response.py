"""Generated from Smithy shape ``com.amazonaws.iot#GetEffectivePoliciesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.effective_policies


class GetEffectivePoliciesResponse(TypedDict):
    effective_policies: NotRequired[
        "aws_sdk_iot.types.effective_policies.EffectivePolicies"
    ]
    """<p>The effective policies.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEffectivePoliciesResponse) -> dict:
    out: dict = {}
    if "effective_policies" in value:
        import aws_sdk_iot.types.effective_policies

        out["effectivePolicies"] = aws_sdk_iot.types.effective_policies.serialize_json(
            value["effective_policies"]
        )
    return out


def deserialize_json(data: dict) -> GetEffectivePoliciesResponse:
    out: GetEffectivePoliciesResponse = {}  # type: ignore[typeddict-item]
    if "effectivePolicies" in data:
        import aws_sdk_iot.types.effective_policies

        out["effective_policies"] = (
            aws_sdk_iot.types.effective_policies.deserialize_json(
                data["effectivePolicies"]
            )
        )
    return out
