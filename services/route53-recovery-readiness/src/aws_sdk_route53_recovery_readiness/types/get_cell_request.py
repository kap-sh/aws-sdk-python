"""Generated from Smithy shape ``com.amazonaws.route53recoveryreadiness#GetCellRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_route53_recovery_readiness.types.__string


class GetCellRequest(TypedDict):
    cell_name: "aws_sdk_route53_recovery_readiness.types.__string.__string"
    """<p>The name of the cell.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCellRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetCellRequest:
    out: GetCellRequest = {}  # type: ignore[typeddict-item]
    return out
