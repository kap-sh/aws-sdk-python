"""Generated from Smithy shape ``com.amazonaws.apigateway#ApiKey``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.boolean
    import aws_sdk_api_gateway.types.list_of_string
    import aws_sdk_api_gateway.types.map_of_string_to_string
    import aws_sdk_api_gateway.types.string
    import aws_sdk_api_gateway.types.timestamp


class ApiKey(TypedDict, closed=True):
    id: NotRequired["aws_sdk_api_gateway.types.string.String"]
    """<p>The identifier of the API Key.</p>"""
    value: NotRequired["aws_sdk_api_gateway.types.string.String"]
    """<p>The value of the API Key.</p>"""
    name: NotRequired["aws_sdk_api_gateway.types.string.String"]
    """<p>The name of the API Key.</p>"""
    customer_id: NotRequired["aws_sdk_api_gateway.types.string.String"]
    """<p>An Amazon Web Services Marketplace customer identifier, when integrating with the Amazon Web Services SaaS Marketplace.</p>"""
    description: NotRequired["aws_sdk_api_gateway.types.string.String"]
    """<p>The description of the API Key.</p>"""
    enabled: "aws_sdk_api_gateway.types.boolean.Boolean"
    """<p>Specifies whether the API Key can be used by callers.</p>"""
    created_date: NotRequired["aws_sdk_api_gateway.types.timestamp.Timestamp"]
    """<p>The timestamp when the API Key was created.</p>"""
    last_updated_date: NotRequired["aws_sdk_api_gateway.types.timestamp.Timestamp"]
    """<p>The timestamp when the API Key was last updated.</p>"""
    stage_keys: NotRequired["aws_sdk_api_gateway.types.list_of_string.ListOfString"]
    """<p>A list of Stage resources that are associated with the ApiKey resource.</p>"""
    tags: NotRequired[
        "aws_sdk_api_gateway.types.map_of_string_to_string.MapOfStringToString"
    ]
    """<p>The collection of tags. Each tag element is associated with a given resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ApiKey) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "value" in value:
        out["value"] = value["value"]
    if "name" in value:
        out["name"] = value["name"]
    if "customer_id" in value:
        out["customerId"] = value["customer_id"]
    if "description" in value:
        out["description"] = value["description"]
    out["enabled"] = value.get("enabled", False)
    if "created_date" in value:
        import aws_sdk_api_gateway.types.timestamp

        out["createdDate"] = aws_sdk_api_gateway.types.timestamp.serialize_json(
            value["created_date"]
        )
    if "last_updated_date" in value:
        import aws_sdk_api_gateway.types.timestamp

        out["lastUpdatedDate"] = aws_sdk_api_gateway.types.timestamp.serialize_json(
            value["last_updated_date"]
        )
    if "stage_keys" in value:
        import aws_sdk_api_gateway.types.list_of_string

        out["stageKeys"] = aws_sdk_api_gateway.types.list_of_string.serialize_json(
            value["stage_keys"]
        )
    if "tags" in value:
        import aws_sdk_api_gateway.types.map_of_string_to_string

        out["tags"] = aws_sdk_api_gateway.types.map_of_string_to_string.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> ApiKey:
    out: ApiKey = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "value" in data:
        out["value"] = data["value"]
    if "name" in data:
        out["name"] = data["name"]
    if "customerId" in data:
        out["customer_id"] = data["customerId"]
    if "description" in data:
        out["description"] = data["description"]
    if "enabled" in data:
        out["enabled"] = data["enabled"]
    else:
        out["enabled"] = False
    if "createdDate" in data:
        import aws_sdk_api_gateway.types.timestamp

        out["created_date"] = aws_sdk_api_gateway.types.timestamp.deserialize_json(
            data["createdDate"]
        )
    if "lastUpdatedDate" in data:
        import aws_sdk_api_gateway.types.timestamp

        out["last_updated_date"] = aws_sdk_api_gateway.types.timestamp.deserialize_json(
            data["lastUpdatedDate"]
        )
    if "stageKeys" in data:
        import aws_sdk_api_gateway.types.list_of_string

        out["stage_keys"] = aws_sdk_api_gateway.types.list_of_string.deserialize_json(
            data["stageKeys"]
        )
    if "tags" in data:
        import aws_sdk_api_gateway.types.map_of_string_to_string

        out["tags"] = (
            aws_sdk_api_gateway.types.map_of_string_to_string.deserialize_json(
                data["tags"]
            )
        )
    return out
