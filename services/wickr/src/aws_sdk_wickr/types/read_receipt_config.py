"""Generated from Smithy shape ``com.amazonaws.wickr#ReadReceiptConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_wickr.types.status


class ReadReceiptConfig(TypedDict, closed=True):
    status: NotRequired["aws_sdk_wickr.types.status.Status"]
    """<p>The read receipt status mode for the network.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReadReceiptConfig) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_wickr.types.status

        out["status"] = aws_sdk_wickr.types.status.serialize_json(value["status"])
    return out


def deserialize_json(data: dict) -> ReadReceiptConfig:
    out: ReadReceiptConfig = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import aws_sdk_wickr.types.status

        out["status"] = aws_sdk_wickr.types.status.deserialize_json(data["status"])
    return out
