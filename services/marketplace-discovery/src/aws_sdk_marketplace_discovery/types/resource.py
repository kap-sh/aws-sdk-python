"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#Resource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_marketplace_discovery.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_marketplace_discovery.types.non_empty_string
    import aws_sdk_marketplace_discovery.types.nullable_string
    import aws_sdk_marketplace_discovery.types.resource_content_type
    import aws_sdk_marketplace_discovery.types.resource_type


class Resource(TypedDict, closed=True):
    resource_type: "aws_sdk_marketplace_discovery.types.resource_type.ResourceType"
    """<p>The category of the resource, such as manufacturer support or usage instructions.</p>"""
    content_type: (
        "aws_sdk_marketplace_discovery.types.resource_content_type.ResourceContentType"
    )
    """<p>The format of the resource content, such as a URL, email address, or text.</p>"""
    value: "aws_sdk_marketplace_discovery.types.non_empty_string.NonEmptyString"
    """<p>The resource content. Interpretation depends on the content type.</p>"""
    display_name: NotRequired[
        "aws_sdk_marketplace_discovery.types.nullable_string.NullableString"
    ]
    """<p>An optional human-readable label for the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Resource) -> dict:
    out: dict = {}
    import aws_sdk_marketplace_discovery.types.resource_type

    out["resourceType"] = (
        aws_sdk_marketplace_discovery.types.resource_type.serialize_json(
            value["resource_type"]
        )
    )
    import aws_sdk_marketplace_discovery.types.resource_content_type

    out["contentType"] = (
        aws_sdk_marketplace_discovery.types.resource_content_type.serialize_json(
            value["content_type"]
        )
    )
    out["value"] = value["value"]
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    return out


def deserialize_json(data: dict) -> Resource:
    out: Resource = {}  # type: ignore[typeddict-item]
    if "resourceType" in data:
        import aws_sdk_marketplace_discovery.types.resource_type

        out["resource_type"] = (
            aws_sdk_marketplace_discovery.types.resource_type.deserialize_json(
                data["resourceType"]
            )
        )
    else:
        raise DeserializationError("Resource.resource_type required")
    if "contentType" in data:
        import aws_sdk_marketplace_discovery.types.resource_content_type

        out["content_type"] = (
            aws_sdk_marketplace_discovery.types.resource_content_type.deserialize_json(
                data["contentType"]
            )
        )
    else:
        raise DeserializationError("Resource.content_type required")
    if "value" in data:
        out["value"] = data["value"]
    else:
        raise DeserializationError("Resource.value required")
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    return out
