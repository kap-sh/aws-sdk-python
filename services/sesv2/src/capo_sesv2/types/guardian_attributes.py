"""Generated from Smithy shape ``com.amazonaws.sesv2#GuardianAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.feature_status


class GuardianAttributes(TypedDict, closed=True):
    optimized_shared_delivery: NotRequired[
        "capo_sesv2.types.feature_status.FeatureStatus"
    ]
    """<p>Specifies the status of your VDM optimized shared delivery. Can be one of the following:</p> <ul> <li> <p> <code>ENABLED</code> – Amazon SES enables optimized shared delivery for your account.</p> </li> <li> <p> <code>DISABLED</code> – Amazon SES disables optimized shared delivery for your account.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardianAttributes) -> dict:
    out: dict = {}
    if "optimized_shared_delivery" in value:
        import capo_sesv2.types.feature_status

        out["OptimizedSharedDelivery"] = capo_sesv2.types.feature_status.serialize_json(
            value["optimized_shared_delivery"]
        )
    return out


def deserialize_json(data: dict) -> GuardianAttributes:
    out: GuardianAttributes = {}  # type: ignore[typeddict-item]
    if "OptimizedSharedDelivery" in data:
        import capo_sesv2.types.feature_status

        out["optimized_shared_delivery"] = (
            capo_sesv2.types.feature_status.deserialize_json(
                data["OptimizedSharedDelivery"]
            )
        )
    return out
