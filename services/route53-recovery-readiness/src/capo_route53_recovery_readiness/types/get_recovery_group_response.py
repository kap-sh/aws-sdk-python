"""Generated from Smithy shape ``com.amazonaws.route53recoveryreadiness#GetRecoveryGroupResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53_recovery_readiness.types.__list_of__string
    import capo_route53_recovery_readiness.types.__string_max64_pattern_aazaz09_z
    import capo_route53_recovery_readiness.types.__string_max256
    import capo_route53_recovery_readiness.types.tags


class GetRecoveryGroupResponse(TypedDict, closed=True):
    cells: NotRequired[
        "capo_route53_recovery_readiness.types.__list_of__string.__listOf__string"
    ]
    """<p>A list of a cell's Amazon Resource Names (ARNs).</p>"""
    recovery_group_arn: NotRequired[
        "capo_route53_recovery_readiness.types.__string_max256.__stringMax256"
    ]
    """<p>The Amazon Resource Name (ARN) for the recovery group.</p>"""
    recovery_group_name: NotRequired[
        "capo_route53_recovery_readiness.types.__string_max64_pattern_aazaz09_z.__stringMax64PatternAAZAZ09Z"
    ]
    """<p>The name of the recovery group.</p>"""
    tags: NotRequired["capo_route53_recovery_readiness.types.tags.Tags"]
    """<p>The tags associated with the recovery group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRecoveryGroupResponse) -> dict:
    out: dict = {}
    if "cells" in value:
        import capo_route53_recovery_readiness.types.__list_of__string

        out["cells"] = (
            capo_route53_recovery_readiness.types.__list_of__string.serialize_json(
                value["cells"]
            )
        )
    if "recovery_group_arn" in value:
        out["recoveryGroupArn"] = value["recovery_group_arn"]
    if "recovery_group_name" in value:
        out["recoveryGroupName"] = value["recovery_group_name"]
    if "tags" in value:
        import capo_route53_recovery_readiness.types.tags

        out["tags"] = capo_route53_recovery_readiness.types.tags.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> GetRecoveryGroupResponse:
    out: GetRecoveryGroupResponse = {}  # type: ignore[typeddict-item]
    if "cells" in data:
        import capo_route53_recovery_readiness.types.__list_of__string

        out["cells"] = (
            capo_route53_recovery_readiness.types.__list_of__string.deserialize_json(
                data["cells"]
            )
        )
    if "recoveryGroupArn" in data:
        out["recovery_group_arn"] = data["recoveryGroupArn"]
    if "recoveryGroupName" in data:
        out["recovery_group_name"] = data["recoveryGroupName"]
    if "tags" in data:
        import capo_route53_recovery_readiness.types.tags

        out["tags"] = capo_route53_recovery_readiness.types.tags.deserialize_json(
            data["tags"]
        )
    return out
