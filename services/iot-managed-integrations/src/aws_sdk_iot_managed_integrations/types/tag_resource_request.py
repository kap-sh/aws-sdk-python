"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_iot_managed_integrations.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.io_t_managed_integrations_resource_arn
    import aws_sdk_iot_managed_integrations.types.tags_map


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "aws_sdk_iot_managed_integrations.types.io_t_managed_integrations_resource_arn.IoTManagedIntegrationsResourceARN"
    """<p>The Amazon Resource Name (ARN) of the resource to which to add tags.</p>"""
    tags: "aws_sdk_iot_managed_integrations.types.tags_map.TagsMap"
    """<p>A set of key/value pairs that are used to manage the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import aws_sdk_iot_managed_integrations.types.tags_map

    out["Tags"] = aws_sdk_iot_managed_integrations.types.tags_map.serialize_json(
        value["tags"]
    )
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import aws_sdk_iot_managed_integrations.types.tags_map

        out["tags"] = aws_sdk_iot_managed_integrations.types.tags_map.deserialize_json(
            data["Tags"]
        )
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out
