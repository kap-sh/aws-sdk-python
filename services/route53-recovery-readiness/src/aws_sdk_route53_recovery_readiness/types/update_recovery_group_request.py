"""Generated from Smithy shape ``com.amazonaws.route53recoveryreadiness#UpdateRecoveryGroupRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_route53_recovery_readiness.types.__list_of__string
    import aws_sdk_route53_recovery_readiness.types.__string


class UpdateRecoveryGroupRequest(TypedDict):
    cells: NotRequired[
        "aws_sdk_route53_recovery_readiness.types.__list_of__string.__listOf__string"
    ]
    """<p>A list of cell Amazon Resource Names (ARNs). This list completely replaces the previous list.</p>"""
    recovery_group_name: "aws_sdk_route53_recovery_readiness.types.__string.__string"
    """<p>The name of a recovery group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRecoveryGroupRequest) -> dict:
    out: dict = {}
    if "cells" in value:
        import aws_sdk_route53_recovery_readiness.types.__list_of__string

        out["cells"] = (
            aws_sdk_route53_recovery_readiness.types.__list_of__string.serialize_json(
                value["cells"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateRecoveryGroupRequest:
    out: UpdateRecoveryGroupRequest = {}  # type: ignore[typeddict-item]
    if "cells" in data:
        import aws_sdk_route53_recovery_readiness.types.__list_of__string

        out["cells"] = (
            aws_sdk_route53_recovery_readiness.types.__list_of__string.deserialize_json(
                data["cells"]
            )
        )
    return out
