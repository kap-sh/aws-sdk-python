"""Generated from Smithy shape ``com.amazonaws.route53recoverycontrolconfig#ListTagsForResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_route53_recovery_control_config.types.__string


class ListTagsForResourceRequest(TypedDict, closed=True):
    resource_arn: "aws_sdk_route53_recovery_control_config.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) for the resource that's tagged.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTagsForResourceRequest:
    out: ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
    return out
