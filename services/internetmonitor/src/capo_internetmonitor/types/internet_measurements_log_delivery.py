"""Generated from Smithy shape ``com.amazonaws.internetmonitor#InternetMeasurementsLogDelivery``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_internetmonitor.types.s3_config


class InternetMeasurementsLogDelivery(TypedDict, closed=True):
    s3_config: NotRequired["capo_internetmonitor.types.s3_config.S3Config"]
    """<p>The configuration information for publishing Internet Monitor internet measurements to Amazon S3. The configuration includes the bucket name and (optionally) prefix for the S3 bucket to store the measurements, and the delivery status. The delivery status is <code>ENABLED</code> or <code>DISABLED</code>, depending on whether you choose to deliver internet measurements to S3 logs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InternetMeasurementsLogDelivery) -> dict:
    out: dict = {}
    if "s3_config" in value:
        import capo_internetmonitor.types.s3_config

        out["S3Config"] = capo_internetmonitor.types.s3_config.serialize_json(
            value["s3_config"]
        )
    return out


def deserialize_json(data: dict) -> InternetMeasurementsLogDelivery:
    out: InternetMeasurementsLogDelivery = {}  # type: ignore[typeddict-item]
    if "S3Config" in data:
        import capo_internetmonitor.types.s3_config

        out["s3_config"] = capo_internetmonitor.types.s3_config.deserialize_json(
            data["S3Config"]
        )
    return out
