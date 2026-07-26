"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#GetLoggingOptionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iotfleetwise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotfleetwise.types.cloud_watch_log_delivery_options


class GetLoggingOptionsResponse(TypedDict, closed=True):
    cloud_watch_log_delivery: "capo_iotfleetwise.types.cloud_watch_log_delivery_options.CloudWatchLogDeliveryOptions"
    """<p>Returns information about log delivery to Amazon CloudWatch Logs.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetLoggingOptionsResponse) -> dict:
    out: dict = {}
    import capo_iotfleetwise.types.cloud_watch_log_delivery_options

    out["cloudWatchLogDelivery"] = (
        capo_iotfleetwise.types.cloud_watch_log_delivery_options.serialize_aws_json_1_0(
            value["cloud_watch_log_delivery"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetLoggingOptionsResponse:
    out: GetLoggingOptionsResponse = {}  # type: ignore[typeddict-item]
    if "cloudWatchLogDelivery" in data:
        import capo_iotfleetwise.types.cloud_watch_log_delivery_options

        out["cloud_watch_log_delivery"] = (
            capo_iotfleetwise.types.cloud_watch_log_delivery_options.deserialize_aws_json_1_0(
                data["cloudWatchLogDelivery"]
            )
        )
    else:
        raise DeserializationError(
            "GetLoggingOptionsResponse.cloud_watch_log_delivery required"
        )
    return out
