"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_timestream_influxdb.errors import DeserializationError

if TYPE_CHECKING:
    import capo_timestream_influxdb.types.arn
    import capo_timestream_influxdb.types.request_tag_map


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_timestream_influxdb.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the tagged resource.</p>"""
    tags: "capo_timestream_influxdb.types.request_tag_map.RequestTagMap"
    """<p>A list of tags used to categorize and track resources.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    import capo_timestream_influxdb.types.request_tag_map

    out["tags"] = capo_timestream_influxdb.types.request_tag_map.serialize_aws_json_1_0(
        value["tags"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    else:
        raise DeserializationError("TagResourceRequest.resource_arn required")
    if "tags" in data:
        import capo_timestream_influxdb.types.request_tag_map

        out["tags"] = (
            capo_timestream_influxdb.types.request_tag_map.deserialize_aws_json_1_0(
                data["tags"]
            )
        )
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out
