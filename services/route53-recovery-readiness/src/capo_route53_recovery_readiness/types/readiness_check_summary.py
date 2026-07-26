"""Generated from Smithy shape ``com.amazonaws.route53recoveryreadiness#ReadinessCheckSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53_recovery_readiness.types.__string
    import capo_route53_recovery_readiness.types.readiness


class ReadinessCheckSummary(TypedDict, closed=True):
    readiness: NotRequired["capo_route53_recovery_readiness.types.readiness.Readiness"]
    """<p>The readiness status of this readiness check.</p>"""
    readiness_check_name: NotRequired[
        "capo_route53_recovery_readiness.types.__string.__string"
    ]
    """<p>The name of a readiness check.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReadinessCheckSummary) -> dict:
    out: dict = {}
    if "readiness" in value:
        import capo_route53_recovery_readiness.types.readiness

        out["readiness"] = (
            capo_route53_recovery_readiness.types.readiness.serialize_json(
                value["readiness"]
            )
        )
    if "readiness_check_name" in value:
        out["readinessCheckName"] = value["readiness_check_name"]
    return out


def deserialize_json(data: dict) -> ReadinessCheckSummary:
    out: ReadinessCheckSummary = {}  # type: ignore[typeddict-item]
    if "readiness" in data:
        import capo_route53_recovery_readiness.types.readiness

        out["readiness"] = (
            capo_route53_recovery_readiness.types.readiness.deserialize_json(
                data["readiness"]
            )
        )
    if "readinessCheckName" in data:
        out["readiness_check_name"] = data["readinessCheckName"]
    return out
