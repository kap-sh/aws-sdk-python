"""Generated from Smithy shape ``com.amazonaws.rekognition#KinesisVideoStreamStartSelector``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.kinesis_video_stream_fragment_number
    import capo_rekognition.types.u_long


class KinesisVideoStreamStartSelector(TypedDict, closed=True):
    producer_timestamp: NotRequired["capo_rekognition.types.u_long.ULong"]
    """<p> The timestamp from the producer corresponding to the fragment, in milliseconds, expressed in unix time format. </p>"""
    fragment_number: NotRequired[
        "capo_rekognition.types.kinesis_video_stream_fragment_number.KinesisVideoStreamFragmentNumber"
    ]
    """<p> The unique identifier of the fragment. This value monotonically increases based on the ingestion order. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KinesisVideoStreamStartSelector) -> dict:
    out: dict = {}
    if "producer_timestamp" in value:
        out["ProducerTimestamp"] = value["producer_timestamp"]
    if "fragment_number" in value:
        out["FragmentNumber"] = value["fragment_number"]
    return out


def deserialize_aws_json_1_1(data: dict) -> KinesisVideoStreamStartSelector:
    out: KinesisVideoStreamStartSelector = {}  # type: ignore[typeddict-item]
    if "ProducerTimestamp" in data:
        out["producer_timestamp"] = data["ProducerTimestamp"]
    if "FragmentNumber" in data:
        out["fragment_number"] = data["FragmentNumber"]
    return out
