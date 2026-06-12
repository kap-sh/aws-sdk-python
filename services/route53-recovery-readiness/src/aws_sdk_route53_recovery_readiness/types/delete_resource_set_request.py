"""Generated from Smithy shape ``com.amazonaws.route53recoveryreadiness#DeleteResourceSetRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_route53_recovery_readiness.types.__string


class DeleteResourceSetRequest(TypedDict):
    resource_set_name: "aws_sdk_route53_recovery_readiness.types.__string.__string"
    """<p>Name of a resource set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteResourceSetRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteResourceSetRequest:
    out: DeleteResourceSetRequest = {}  # type: ignore[typeddict-item]
    return out
