"""Generated from Smithy shape ``com.amazonaws.kafka#ControllerNodeInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__list_of__string


class ControllerNodeInfo(TypedDict):
    endpoints: NotRequired["aws_sdk_kafka.types.__list_of__string.__listOf__string"]
    """<p>Endpoints for accessing the Controller.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ControllerNodeInfo) -> dict:
    out: dict = {}
    if "endpoints" in value:
        import aws_sdk_kafka.types.__list_of__string

        out["endpoints"] = aws_sdk_kafka.types.__list_of__string.serialize_json(
            value["endpoints"]
        )
    return out


def deserialize_json(data: dict) -> ControllerNodeInfo:
    out: ControllerNodeInfo = {}  # type: ignore[typeddict-item]
    if "endpoints" in data:
        import aws_sdk_kafka.types.__list_of__string

        out["endpoints"] = aws_sdk_kafka.types.__list_of__string.deserialize_json(
            data["endpoints"]
        )
    return out
