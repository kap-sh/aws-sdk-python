"""Generated from Smithy shape ``com.amazonaws.sesv2#CreateMultiRegionEndpointRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_sesv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.details
    import aws_sdk_sesv2.types.endpoint_name
    import aws_sdk_sesv2.types.tag_list


class CreateMultiRegionEndpointRequest(TypedDict, closed=True):
    endpoint_name: "aws_sdk_sesv2.types.endpoint_name.EndpointName"
    """<p>The name of the multi-region endpoint (global-endpoint).</p>"""
    details: "aws_sdk_sesv2.types.details.Details"
    """<p>Contains details of a multi-region endpoint (global-endpoint) being created.</p>"""
    tags: NotRequired["aws_sdk_sesv2.types.tag_list.TagList"]
    """<p>An array of objects that define the tags (keys and values) to associate with the multi-region endpoint (global-endpoint).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMultiRegionEndpointRequest) -> dict:
    out: dict = {}
    out["EndpointName"] = value["endpoint_name"]
    import aws_sdk_sesv2.types.details

    out["Details"] = aws_sdk_sesv2.types.details.serialize_json(value["details"])
    if "tags" in value:
        import aws_sdk_sesv2.types.tag_list

        out["Tags"] = aws_sdk_sesv2.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateMultiRegionEndpointRequest:
    out: CreateMultiRegionEndpointRequest = {}  # type: ignore[typeddict-item]
    if "EndpointName" in data:
        out["endpoint_name"] = data["EndpointName"]
    else:
        raise DeserializationError(
            "CreateMultiRegionEndpointRequest.endpoint_name required"
        )
    if "Details" in data:
        import aws_sdk_sesv2.types.details

        out["details"] = aws_sdk_sesv2.types.details.deserialize_json(data["Details"])
    else:
        raise DeserializationError("CreateMultiRegionEndpointRequest.details required")
    if "Tags" in data:
        import aws_sdk_sesv2.types.tag_list

        out["tags"] = aws_sdk_sesv2.types.tag_list.deserialize_json(data["Tags"])
    return out
