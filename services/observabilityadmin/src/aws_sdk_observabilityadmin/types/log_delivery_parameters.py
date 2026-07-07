"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#LogDeliveryParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_observabilityadmin.types.log_types


class LogDeliveryParameters(TypedDict, closed=True):
    log_types: NotRequired["aws_sdk_observabilityadmin.types.log_types.LogTypes"]
    """<p>The type of log that the source is sending.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LogDeliveryParameters) -> dict:
    out: dict = {}
    if "log_types" in value:
        import aws_sdk_observabilityadmin.types.log_types

        out["LogTypes"] = aws_sdk_observabilityadmin.types.log_types.serialize_json(
            value["log_types"]
        )
    return out


def deserialize_json(data: dict) -> LogDeliveryParameters:
    out: LogDeliveryParameters = {}  # type: ignore[typeddict-item]
    if "LogTypes" in data:
        import aws_sdk_observabilityadmin.types.log_types

        out["log_types"] = aws_sdk_observabilityadmin.types.log_types.deserialize_json(
            data["LogTypes"]
        )
    return out
