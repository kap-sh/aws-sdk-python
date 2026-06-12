"""Generated from Smithy shape ``com.amazonaws.route53recoveryreadiness#ListTagsForResourcesRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_route53_recovery_readiness.types.__string


class ListTagsForResourcesRequest(TypedDict):
    resource_arn: "aws_sdk_route53_recovery_readiness.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) for a resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourcesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTagsForResourcesRequest:
    out: ListTagsForResourcesRequest = {}  # type: ignore[typeddict-item]
    return out
