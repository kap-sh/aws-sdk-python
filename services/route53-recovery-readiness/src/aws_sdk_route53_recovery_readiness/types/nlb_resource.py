"""Generated from Smithy shape ``com.amazonaws.route53recoveryreadiness#NLBResource``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_route53_recovery_readiness.types.__string


class NLBResource(TypedDict):
    arn: NotRequired["aws_sdk_route53_recovery_readiness.types.__string.__string"]
    """<p>The Network Load Balancer resource Amazon Resource Name (ARN).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NLBResource) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> NLBResource:
    out: NLBResource = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    return out
