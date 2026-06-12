"""Generated from Smithy shape ``com.amazonaws.route53recoveryreadiness#UpdateReadinessCheckResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_route53_recovery_readiness.types.__string_max64_pattern_aazaz09_z
    import aws_sdk_route53_recovery_readiness.types.__string_max256
    import aws_sdk_route53_recovery_readiness.types.tags


class UpdateReadinessCheckResponse(TypedDict):
    readiness_check_arn: NotRequired[
        "aws_sdk_route53_recovery_readiness.types.__string_max256.__stringMax256"
    ]
    """<p>The Amazon Resource Name (ARN) associated with a readiness check.</p>"""
    readiness_check_name: NotRequired[
        "aws_sdk_route53_recovery_readiness.types.__string_max64_pattern_aazaz09_z.__stringMax64PatternAAZAZ09Z"
    ]
    """<p>Name of a readiness check.</p>"""
    resource_set: NotRequired[
        "aws_sdk_route53_recovery_readiness.types.__string_max64_pattern_aazaz09_z.__stringMax64PatternAAZAZ09Z"
    ]
    """<p>Name of the resource set to be checked.</p>"""
    tags: NotRequired["aws_sdk_route53_recovery_readiness.types.tags.Tags"]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateReadinessCheckResponse) -> dict:
    out: dict = {}
    if "readiness_check_arn" in value:
        out["readinessCheckArn"] = value["readiness_check_arn"]
    if "readiness_check_name" in value:
        out["readinessCheckName"] = value["readiness_check_name"]
    if "resource_set" in value:
        out["resourceSet"] = value["resource_set"]
    if "tags" in value:
        import aws_sdk_route53_recovery_readiness.types.tags

        out["tags"] = aws_sdk_route53_recovery_readiness.types.tags.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> UpdateReadinessCheckResponse:
    out: UpdateReadinessCheckResponse = {}  # type: ignore[typeddict-item]
    if "readinessCheckArn" in data:
        out["readiness_check_arn"] = data["readinessCheckArn"]
    if "readinessCheckName" in data:
        out["readiness_check_name"] = data["readinessCheckName"]
    if "resourceSet" in data:
        out["resource_set"] = data["resourceSet"]
    if "tags" in data:
        import aws_sdk_route53_recovery_readiness.types.tags

        out["tags"] = aws_sdk_route53_recovery_readiness.types.tags.deserialize_json(
            data["tags"]
        )
    return out
