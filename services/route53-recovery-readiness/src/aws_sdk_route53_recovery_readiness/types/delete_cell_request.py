"""Generated from Smithy shape ``com.amazonaws.route53recoveryreadiness#DeleteCellRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_route53_recovery_readiness.types.__string


class DeleteCellRequest(TypedDict, closed=True):
    cell_name: "aws_sdk_route53_recovery_readiness.types.__string.__string"
    """<p>The name of the cell.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteCellRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteCellRequest:
    out: DeleteCellRequest = {}  # type: ignore[typeddict-item]
    return out
