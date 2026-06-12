"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#GetSignalingChannelEndpointOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kinesis_video.types.resource_endpoint_list


class GetSignalingChannelEndpointOutput(TypedDict):
    resource_endpoint_list: NotRequired[
        "aws_sdk_kinesis_video.types.resource_endpoint_list.ResourceEndpointList"
    ]
    """<p>A list of endpoints for the specified signaling channel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSignalingChannelEndpointOutput) -> dict:
    out: dict = {}
    if "resource_endpoint_list" in value:
        import aws_sdk_kinesis_video.types.resource_endpoint_list

        out["ResourceEndpointList"] = (
            aws_sdk_kinesis_video.types.resource_endpoint_list.serialize_json(
                value["resource_endpoint_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetSignalingChannelEndpointOutput:
    out: GetSignalingChannelEndpointOutput = {}  # type: ignore[typeddict-item]
    if "ResourceEndpointList" in data:
        import aws_sdk_kinesis_video.types.resource_endpoint_list

        out["resource_endpoint_list"] = (
            aws_sdk_kinesis_video.types.resource_endpoint_list.deserialize_json(
                data["ResourceEndpointList"]
            )
        )
    return out
