"""Generated from Smithy shape ``com.amazonaws.finspace#TickerplantLogConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_finspace.types.tickerplant_log_volumes


class TickerplantLogConfiguration(TypedDict, closed=True):
    tickerplant_log_volumes: NotRequired[
        "aws_sdk_finspace.types.tickerplant_log_volumes.TickerplantLogVolumes"
    ]
    """<p> The name of the volumes for tickerplant logs. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TickerplantLogConfiguration) -> dict:
    out: dict = {}
    if "tickerplant_log_volumes" in value:
        import aws_sdk_finspace.types.tickerplant_log_volumes

        out["tickerplantLogVolumes"] = (
            aws_sdk_finspace.types.tickerplant_log_volumes.serialize_json(
                value["tickerplant_log_volumes"]
            )
        )
    return out


def deserialize_json(data: dict) -> TickerplantLogConfiguration:
    out: TickerplantLogConfiguration = {}  # type: ignore[typeddict-item]
    if "tickerplantLogVolumes" in data:
        import aws_sdk_finspace.types.tickerplant_log_volumes

        out["tickerplant_log_volumes"] = (
            aws_sdk_finspace.types.tickerplant_log_volumes.deserialize_json(
                data["tickerplantLogVolumes"]
            )
        )
    return out
