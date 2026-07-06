"""Generated from Smithy shape ``com.amazonaws.sesv2#GuardianOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.feature_status


class GuardianOptions(TypedDict, closed=True):
    optimized_shared_delivery: NotRequired[
        "aws_sdk_sesv2.types.feature_status.FeatureStatus"
    ]
    """<p>Specifies the status of your VDM optimized shared delivery. Can be one of the following:</p> <ul> <li> <p> <code>ENABLED</code> – Amazon SES enables optimized shared delivery for the configuration set.</p> </li> <li> <p> <code>DISABLED</code> – Amazon SES disables optimized shared delivery for the configuration set.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardianOptions) -> dict:
    out: dict = {}
    if "optimized_shared_delivery" in value:
        import aws_sdk_sesv2.types.feature_status

        out["OptimizedSharedDelivery"] = (
            aws_sdk_sesv2.types.feature_status.serialize_json(
                value["optimized_shared_delivery"]
            )
        )
    return out


def deserialize_json(data: dict) -> GuardianOptions:
    out: GuardianOptions = {}  # type: ignore[typeddict-item]
    if "OptimizedSharedDelivery" in data:
        import aws_sdk_sesv2.types.feature_status

        out["optimized_shared_delivery"] = (
            aws_sdk_sesv2.types.feature_status.deserialize_json(
                data["OptimizedSharedDelivery"]
            )
        )
    return out
