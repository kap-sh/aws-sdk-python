"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#DescribeMappedResourceConfigurationOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kinesis_video.types.mapped_resource_configuration_list
    import aws_sdk_kinesis_video.types.next_token


class DescribeMappedResourceConfigurationOutput(TypedDict):
    mapped_resource_configuration_list: NotRequired[
        "aws_sdk_kinesis_video.types.mapped_resource_configuration_list.MappedResourceConfigurationList"
    ]
    """<p>A structure that encapsulates, or contains, the media storage configuration properties.</p>"""
    next_token: NotRequired["aws_sdk_kinesis_video.types.next_token.NextToken"]
    """<p>The token that was used in the <code>NextToken</code>request to fetch the next set of results. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeMappedResourceConfigurationOutput) -> dict:
    out: dict = {}
    if "mapped_resource_configuration_list" in value:
        import aws_sdk_kinesis_video.types.mapped_resource_configuration_list

        out["MappedResourceConfigurationList"] = (
            aws_sdk_kinesis_video.types.mapped_resource_configuration_list.serialize_json(
                value["mapped_resource_configuration_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> DescribeMappedResourceConfigurationOutput:
    out: DescribeMappedResourceConfigurationOutput = {}  # type: ignore[typeddict-item]
    if "MappedResourceConfigurationList" in data:
        import aws_sdk_kinesis_video.types.mapped_resource_configuration_list

        out["mapped_resource_configuration_list"] = (
            aws_sdk_kinesis_video.types.mapped_resource_configuration_list.deserialize_json(
                data["MappedResourceConfigurationList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
