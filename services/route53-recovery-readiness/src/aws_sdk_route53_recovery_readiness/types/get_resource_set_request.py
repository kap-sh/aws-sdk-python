"""Generated from Smithy shape ``com.amazonaws.route53recoveryreadiness#GetResourceSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_route53_recovery_readiness.types.__string


class GetResourceSetRequest(TypedDict, closed=True):
    resource_set_name: "aws_sdk_route53_recovery_readiness.types.__string.__string"
    """<p>Name of a resource set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetResourceSetRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetResourceSetRequest:
    out: GetResourceSetRequest = {}  # type: ignore[typeddict-item]
    return out
