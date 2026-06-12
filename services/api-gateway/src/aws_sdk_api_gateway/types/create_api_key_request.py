"""Generated from Smithy shape ``com.amazonaws.apigateway#CreateApiKeyRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.boolean
    import aws_sdk_api_gateway.types.list_of_stage_keys
    import aws_sdk_api_gateway.types.map_of_string_to_string
    import aws_sdk_api_gateway.types.string


class CreateApiKeyRequest(TypedDict):
    name: NotRequired["aws_sdk_api_gateway.types.string.String"]
    """<p>The name of the ApiKey.</p>"""
    description: NotRequired["aws_sdk_api_gateway.types.string.String"]
    """<p>The description of the ApiKey.</p>"""
    enabled: "aws_sdk_api_gateway.types.boolean.Boolean"
    """<p>Specifies whether the ApiKey can be used by callers.</p>"""
    generate_distinct_id: "aws_sdk_api_gateway.types.boolean.Boolean"
    """<p>Specifies whether (<code>true</code>) or not (<code>false</code>) the key identifier is distinct from the created API key value. This parameter is deprecated and should not be used.</p>"""
    value: NotRequired["aws_sdk_api_gateway.types.string.String"]
    """<p>Specifies a value of the API key.</p>"""
    stage_keys: NotRequired[
        "aws_sdk_api_gateway.types.list_of_stage_keys.ListOfStageKeys"
    ]
    """<p>DEPRECATED FOR USAGE PLANS - Specifies stages associated with the API key.</p>"""
    customer_id: NotRequired["aws_sdk_api_gateway.types.string.String"]
    """<p>An Amazon Web Services Marketplace customer identifier, when integrating with the Amazon Web Services SaaS Marketplace.</p>"""
    tags: NotRequired[
        "aws_sdk_api_gateway.types.map_of_string_to_string.MapOfStringToString"
    ]
    """<p>The key-value map of strings. The valid character set is [a-zA-Z+-=._:/]. The tag key can be up to 128 characters and must not start with <code>aws:</code>. The tag value can be up to 256 characters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateApiKeyRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    out["enabled"] = value.get("enabled", False)
    out["generateDistinctId"] = value.get("generate_distinct_id", False)
    if "value" in value:
        out["value"] = value["value"]
    if "stage_keys" in value:
        import aws_sdk_api_gateway.types.list_of_stage_keys

        out["stageKeys"] = aws_sdk_api_gateway.types.list_of_stage_keys.serialize_json(
            value["stage_keys"]
        )
    if "customer_id" in value:
        out["customerId"] = value["customer_id"]
    if "tags" in value:
        import aws_sdk_api_gateway.types.map_of_string_to_string

        out["tags"] = aws_sdk_api_gateway.types.map_of_string_to_string.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateApiKeyRequest:
    out: CreateApiKeyRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "enabled" in data:
        out["enabled"] = data["enabled"]
    else:
        out["enabled"] = False
    if "generateDistinctId" in data:
        out["generate_distinct_id"] = data["generateDistinctId"]
    else:
        out["generate_distinct_id"] = False
    if "value" in data:
        out["value"] = data["value"]
    if "stageKeys" in data:
        import aws_sdk_api_gateway.types.list_of_stage_keys

        out["stage_keys"] = (
            aws_sdk_api_gateway.types.list_of_stage_keys.deserialize_json(
                data["stageKeys"]
            )
        )
    if "customerId" in data:
        out["customer_id"] = data["customerId"]
    if "tags" in data:
        import aws_sdk_api_gateway.types.map_of_string_to_string

        out["tags"] = (
            aws_sdk_api_gateway.types.map_of_string_to_string.deserialize_json(
                data["tags"]
            )
        )
    return out
