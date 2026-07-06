"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_timestream_influxdb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_timestream_influxdb.types.arn
    import aws_sdk_timestream_influxdb.types.tag_keys


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "aws_sdk_timestream_influxdb.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the tagged resource.</p>"""
    tag_keys: "aws_sdk_timestream_influxdb.types.tag_keys.TagKeys"
    """<p>The keys used to identify the tags.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UntagResourceRequest) -> dict:
    out: dict = {}
    import aws_sdk_timestream_influxdb.types.tag_keys

    out["tagKeys"] = aws_sdk_timestream_influxdb.types.tag_keys.serialize_aws_json_1_0(
        value["tag_keys"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if "tagKeys" in data:
        import aws_sdk_timestream_influxdb.types.tag_keys

        out["tag_keys"] = (
            aws_sdk_timestream_influxdb.types.tag_keys.deserialize_aws_json_1_0(
                data["tagKeys"]
            )
        )
    else:
        raise DeserializationError("UntagResourceRequest.tag_keys required")
    return out
