"""Generated from Smithy shape ``com.amazonaws.route53recoveryreadiness#ReadinessCheckOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53_recovery_readiness.types.__string_max64_pattern_aazaz09_z
    import capo_route53_recovery_readiness.types.__string_max256
    import capo_route53_recovery_readiness.types.tags


class ReadinessCheckOutput(TypedDict, closed=True):
    readiness_check_arn: NotRequired[
        "capo_route53_recovery_readiness.types.__string_max256.__stringMax256"
    ]
    """<p>The Amazon Resource Name (ARN) associated with a readiness check.</p>"""
    readiness_check_name: NotRequired[
        "capo_route53_recovery_readiness.types.__string_max64_pattern_aazaz09_z.__stringMax64PatternAAZAZ09Z"
    ]
    """<p>Name of a readiness check.</p>"""
    resource_set: NotRequired[
        "capo_route53_recovery_readiness.types.__string_max64_pattern_aazaz09_z.__stringMax64PatternAAZAZ09Z"
    ]
    """<p>Name of the resource set to be checked.</p>"""
    tags: NotRequired["capo_route53_recovery_readiness.types.tags.Tags"]


# --- restJson1 ser/de ---
def serialize_json(value: ReadinessCheckOutput) -> dict:
    out: dict = {}
    if "readiness_check_arn" in value:
        out["readinessCheckArn"] = value["readiness_check_arn"]
    if "readiness_check_name" in value:
        out["readinessCheckName"] = value["readiness_check_name"]
    if "resource_set" in value:
        out["resourceSet"] = value["resource_set"]
    if "tags" in value:
        import capo_route53_recovery_readiness.types.tags

        out["tags"] = capo_route53_recovery_readiness.types.tags.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> ReadinessCheckOutput:
    out: ReadinessCheckOutput = {}  # type: ignore[typeddict-item]
    if "readinessCheckArn" in data:
        out["readiness_check_arn"] = data["readinessCheckArn"]
    if "readinessCheckName" in data:
        out["readiness_check_name"] = data["readinessCheckName"]
    if "resourceSet" in data:
        out["resource_set"] = data["resourceSet"]
    if "tags" in data:
        import capo_route53_recovery_readiness.types.tags

        out["tags"] = capo_route53_recovery_readiness.types.tags.deserialize_json(
            data["tags"]
        )
    return out
