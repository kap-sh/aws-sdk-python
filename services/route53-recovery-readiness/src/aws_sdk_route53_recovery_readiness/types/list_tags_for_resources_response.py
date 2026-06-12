"""Generated from Smithy shape ``com.amazonaws.route53recoveryreadiness#ListTagsForResourcesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_route53_recovery_readiness.types.tags


class ListTagsForResourcesResponse(TypedDict):
    tags: NotRequired["aws_sdk_route53_recovery_readiness.types.tags.Tags"]
    """<p></p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourcesResponse) -> dict:
    out: dict = {}
    if "tags" in value:
        import aws_sdk_route53_recovery_readiness.types.tags

        out["tags"] = aws_sdk_route53_recovery_readiness.types.tags.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> ListTagsForResourcesResponse:
    out: ListTagsForResourcesResponse = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import aws_sdk_route53_recovery_readiness.types.tags

        out["tags"] = aws_sdk_route53_recovery_readiness.types.tags.deserialize_json(
            data["tags"]
        )
    return out
