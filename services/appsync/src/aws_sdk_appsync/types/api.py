"""Generated from Smithy shape ``com.amazonaws.appsync#Api``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appsync.types.api_name
    import aws_sdk_appsync.types.boolean
    import aws_sdk_appsync.types.event_config
    import aws_sdk_appsync.types.map_of_string_to_string
    import aws_sdk_appsync.types.owner_contact
    import aws_sdk_appsync.types.string
    import aws_sdk_appsync.types.tag_map
    import aws_sdk_appsync.types.timestamp


class Api(TypedDict, closed=True):
    api_id: NotRequired["aws_sdk_appsync.types.string.String"]
    """<p>The <code>Api</code> ID.</p>"""
    name: NotRequired["aws_sdk_appsync.types.api_name.ApiName"]
    """<p>The name of the <code>Api</code>.</p>"""
    owner_contact: NotRequired["aws_sdk_appsync.types.owner_contact.OwnerContact"]
    """<p>The owner contact information for the <code>Api</code> </p>"""
    tags: NotRequired["aws_sdk_appsync.types.tag_map.TagMap"]
    dns: NotRequired[
        "aws_sdk_appsync.types.map_of_string_to_string.MapOfStringToString"
    ]
    """<p>The DNS records for the API. This will include an HTTP and a real-time endpoint.</p>"""
    api_arn: NotRequired["aws_sdk_appsync.types.string.String"]
    """<p>The Amazon Resource Name (ARN) for the <code>Api</code>.</p>"""
    created: NotRequired["aws_sdk_appsync.types.timestamp.Timestamp"]
    """<p>The date and time that the <code>Api</code> was created.</p>"""
    xray_enabled: "aws_sdk_appsync.types.boolean.Boolean"
    """<p>A flag indicating whether to use X-Ray tracing for this <code>Api</code>.</p>"""
    waf_web_acl_arn: NotRequired["aws_sdk_appsync.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the WAF web access control list (web ACL) associated with this <code>Api</code>, if one exists.</p>"""
    event_config: NotRequired["aws_sdk_appsync.types.event_config.EventConfig"]
    """<p>The Event API configuration. This includes the default authorization configuration for connecting, publishing, and subscribing to an Event API.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Api) -> dict:
    out: dict = {}
    if "api_id" in value:
        out["apiId"] = value["api_id"]
    if "name" in value:
        out["name"] = value["name"]
    if "owner_contact" in value:
        out["ownerContact"] = value["owner_contact"]
    if "tags" in value:
        import aws_sdk_appsync.types.tag_map

        out["tags"] = aws_sdk_appsync.types.tag_map.serialize_json(value["tags"])
    if "dns" in value:
        import aws_sdk_appsync.types.map_of_string_to_string

        out["dns"] = aws_sdk_appsync.types.map_of_string_to_string.serialize_json(
            value["dns"]
        )
    if "api_arn" in value:
        out["apiArn"] = value["api_arn"]
    if "created" in value:
        import aws_sdk_appsync.types.timestamp

        out["created"] = aws_sdk_appsync.types.timestamp.serialize_json(
            value["created"]
        )
    out["xrayEnabled"] = value.get("xray_enabled", False)
    if "waf_web_acl_arn" in value:
        out["wafWebAclArn"] = value["waf_web_acl_arn"]
    if "event_config" in value:
        import aws_sdk_appsync.types.event_config

        out["eventConfig"] = aws_sdk_appsync.types.event_config.serialize_json(
            value["event_config"]
        )
    return out


def deserialize_json(data: dict) -> Api:
    out: Api = {}  # type: ignore[typeddict-item]
    if "apiId" in data:
        out["api_id"] = data["apiId"]
    if "name" in data:
        out["name"] = data["name"]
    if "ownerContact" in data:
        out["owner_contact"] = data["ownerContact"]
    if "tags" in data:
        import aws_sdk_appsync.types.tag_map

        out["tags"] = aws_sdk_appsync.types.tag_map.deserialize_json(data["tags"])
    if "dns" in data:
        import aws_sdk_appsync.types.map_of_string_to_string

        out["dns"] = aws_sdk_appsync.types.map_of_string_to_string.deserialize_json(
            data["dns"]
        )
    if "apiArn" in data:
        out["api_arn"] = data["apiArn"]
    if "created" in data:
        import aws_sdk_appsync.types.timestamp

        out["created"] = aws_sdk_appsync.types.timestamp.deserialize_json(
            data["created"]
        )
    if "xrayEnabled" in data:
        out["xray_enabled"] = data["xrayEnabled"]
    else:
        out["xray_enabled"] = False
    if "wafWebAclArn" in data:
        out["waf_web_acl_arn"] = data["wafWebAclArn"]
    if "eventConfig" in data:
        import aws_sdk_appsync.types.event_config

        out["event_config"] = aws_sdk_appsync.types.event_config.deserialize_json(
            data["eventConfig"]
        )
    return out
