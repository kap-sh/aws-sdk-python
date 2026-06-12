"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#GetLoggingOptionsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iotfleetwise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.cloud_watch_log_delivery_options


class GetLoggingOptionsResponse(TypedDict):
    cloud_watch_log_delivery: "aws_sdk_iotfleetwise.types.cloud_watch_log_delivery_options.CloudWatchLogDeliveryOptions"
    """<p>Returns information about log delivery to Amazon CloudWatch Logs.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetLoggingOptionsResponse) -> dict:
    out: dict = {}
    import aws_sdk_iotfleetwise.types.cloud_watch_log_delivery_options

    out["cloudWatchLogDelivery"] = (
        aws_sdk_iotfleetwise.types.cloud_watch_log_delivery_options.serialize_aws_json_1_0(
            value["cloud_watch_log_delivery"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetLoggingOptionsResponse:
    out: GetLoggingOptionsResponse = {}  # type: ignore[typeddict-item]
    if "cloudWatchLogDelivery" in data:
        import aws_sdk_iotfleetwise.types.cloud_watch_log_delivery_options

        out["cloud_watch_log_delivery"] = (
            aws_sdk_iotfleetwise.types.cloud_watch_log_delivery_options.deserialize_aws_json_1_0(
                data["cloudWatchLogDelivery"]
            )
        )
    else:
        raise DeserializationError(
            "GetLoggingOptionsResponse.cloud_watch_log_delivery required"
        )
    return out
