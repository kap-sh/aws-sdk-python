"""Generated from Smithy shape ``com.amazonaws.workspaces#ModifyStreamingPropertiesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_workspaces.errors import DeserializationError

if TYPE_CHECKING:
    import capo_workspaces.types.directory_id
    import capo_workspaces.types.streaming_properties


class ModifyStreamingPropertiesRequest(TypedDict, closed=True):
    resource_id: "capo_workspaces.types.directory_id.DirectoryId"
    """<p>The identifier of the resource.</p>"""
    streaming_properties: NotRequired[
        "capo_workspaces.types.streaming_properties.StreamingProperties"
    ]
    """<p>The streaming properties to configure.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModifyStreamingPropertiesRequest) -> dict:
    out: dict = {}
    out["ResourceId"] = value["resource_id"]
    if "streaming_properties" in value:
        import capo_workspaces.types.streaming_properties

        out["StreamingProperties"] = (
            capo_workspaces.types.streaming_properties.serialize_aws_json_1_1(
                value["streaming_properties"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ModifyStreamingPropertiesRequest:
    out: ModifyStreamingPropertiesRequest = {}  # type: ignore[typeddict-item]
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    else:
        raise DeserializationError(
            "ModifyStreamingPropertiesRequest.resource_id required"
        )
    if "StreamingProperties" in data:
        import capo_workspaces.types.streaming_properties

        out["streaming_properties"] = (
            capo_workspaces.types.streaming_properties.deserialize_aws_json_1_1(
                data["StreamingProperties"]
            )
        )
    return out
