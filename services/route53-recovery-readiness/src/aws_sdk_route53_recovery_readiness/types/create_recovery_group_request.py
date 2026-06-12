"""Generated from Smithy shape ``com.amazonaws.route53recoveryreadiness#CreateRecoveryGroupRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_route53_recovery_readiness.types.__list_of__string
    import aws_sdk_route53_recovery_readiness.types.__string
    import aws_sdk_route53_recovery_readiness.types.tags


class CreateRecoveryGroupRequest(TypedDict):
    cells: NotRequired[
        "aws_sdk_route53_recovery_readiness.types.__list_of__string.__listOf__string"
    ]
    """<p>A list of the cell Amazon Resource Names (ARNs) in the recovery group.</p>"""
    recovery_group_name: NotRequired[
        "aws_sdk_route53_recovery_readiness.types.__string.__string"
    ]
    """<p>The name of the recovery group to create.</p>"""
    tags: NotRequired["aws_sdk_route53_recovery_readiness.types.tags.Tags"]


# --- restJson1 ser/de ---
def serialize_json(value: CreateRecoveryGroupRequest) -> dict:
    out: dict = {}
    if "cells" in value:
        import aws_sdk_route53_recovery_readiness.types.__list_of__string

        out["cells"] = (
            aws_sdk_route53_recovery_readiness.types.__list_of__string.serialize_json(
                value["cells"]
            )
        )
    if "recovery_group_name" in value:
        out["recoveryGroupName"] = value["recovery_group_name"]
    if "tags" in value:
        import aws_sdk_route53_recovery_readiness.types.tags

        out["tags"] = aws_sdk_route53_recovery_readiness.types.tags.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateRecoveryGroupRequest:
    out: CreateRecoveryGroupRequest = {}  # type: ignore[typeddict-item]
    if "cells" in data:
        import aws_sdk_route53_recovery_readiness.types.__list_of__string

        out["cells"] = (
            aws_sdk_route53_recovery_readiness.types.__list_of__string.deserialize_json(
                data["cells"]
            )
        )
    if "recoveryGroupName" in data:
        out["recovery_group_name"] = data["recoveryGroupName"]
    if "tags" in data:
        import aws_sdk_route53_recovery_readiness.types.tags

        out["tags"] = aws_sdk_route53_recovery_readiness.types.tags.deserialize_json(
            data["tags"]
        )
    return out
