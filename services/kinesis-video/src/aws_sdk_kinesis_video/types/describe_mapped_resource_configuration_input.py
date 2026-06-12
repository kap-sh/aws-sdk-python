"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#DescribeMappedResourceConfigurationInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kinesis_video.types.mapped_resource_configuration_list_limit
    import aws_sdk_kinesis_video.types.next_token
    import aws_sdk_kinesis_video.types.resource_arn
    import aws_sdk_kinesis_video.types.stream_name


class DescribeMappedResourceConfigurationInput(TypedDict):
    stream_name: NotRequired["aws_sdk_kinesis_video.types.stream_name.StreamName"]
    """<p>The name of the stream.</p>"""
    stream_arn: NotRequired["aws_sdk_kinesis_video.types.resource_arn.ResourceARN"]
    """<p>The Amazon Resource Name (ARN) of the stream.</p>"""
    max_results: NotRequired[
        "aws_sdk_kinesis_video.types.mapped_resource_configuration_list_limit.MappedResourceConfigurationListLimit"
    ]
    """<p>The maximum number of results to return in the response.</p>"""
    next_token: NotRequired["aws_sdk_kinesis_video.types.next_token.NextToken"]
    """<p>The token to provide in your next request, to get another batch of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeMappedResourceConfigurationInput) -> dict:
    out: dict = {}
    if "stream_name" in value:
        out["StreamName"] = value["stream_name"]
    if "stream_arn" in value:
        out["StreamARN"] = value["stream_arn"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> DescribeMappedResourceConfigurationInput:
    out: DescribeMappedResourceConfigurationInput = {}  # type: ignore[typeddict-item]
    if "StreamName" in data:
        out["stream_name"] = data["StreamName"]
    if "StreamARN" in data:
        out["stream_arn"] = data["StreamARN"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
