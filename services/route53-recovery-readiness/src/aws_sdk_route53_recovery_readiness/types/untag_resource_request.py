"""Generated from Smithy shape ``com.amazonaws.route53recoveryreadiness#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_route53_recovery_readiness.types.__list_of__string
    import aws_sdk_route53_recovery_readiness.types.__string


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "aws_sdk_route53_recovery_readiness.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) for a resource.</p>"""
    tag_keys: NotRequired[
        "aws_sdk_route53_recovery_readiness.types.__list_of__string.__listOf__string"
    ]
    """<p>The keys for tags you add to resources.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out
