"""Generated from Smithy shape ``com.amazonaws.route53recoveryreadiness#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53_recovery_readiness.types.__string
    import capo_route53_recovery_readiness.types.tags


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_route53_recovery_readiness.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) for a resource.</p>"""
    tags: NotRequired["capo_route53_recovery_readiness.types.tags.Tags"]
    """<p></p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_route53_recovery_readiness.types.tags

        out["tags"] = capo_route53_recovery_readiness.types.tags.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import capo_route53_recovery_readiness.types.tags

        out["tags"] = capo_route53_recovery_readiness.types.tags.deserialize_json(
            data["tags"]
        )
    return out
