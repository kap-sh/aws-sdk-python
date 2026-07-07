"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#CreateScopeInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_networkflowmonitor.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_networkflowmonitor.types.tag_map
    import aws_sdk_networkflowmonitor.types.target_resource_list
    import aws_sdk_networkflowmonitor.types.uuid_string


class CreateScopeInput(TypedDict, closed=True):
    targets: "aws_sdk_networkflowmonitor.types.target_resource_list.TargetResourceList"
    """<p>The targets to define the scope to be monitored. A target is an array of targetResources, which are currently Region-account pairs, defined by targetResource constructs.</p>"""
    client_token: NotRequired["aws_sdk_networkflowmonitor.types.uuid_string.UuidString"]
    """<p>A unique, case-sensitive string of up to 64 ASCII characters that you specify to make an idempotent API request. Don't reuse the same client token for other API requests.</p>"""
    tags: NotRequired["aws_sdk_networkflowmonitor.types.tag_map.TagMap"]
    """<p>The tags for a scope. You can add a maximum of 200 tags.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateScopeInput) -> dict:
    out: dict = {}
    import aws_sdk_networkflowmonitor.types.target_resource_list

    out["targets"] = (
        aws_sdk_networkflowmonitor.types.target_resource_list.serialize_json(
            value["targets"]
        )
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "tags" in value:
        import aws_sdk_networkflowmonitor.types.tag_map

        out["tags"] = aws_sdk_networkflowmonitor.types.tag_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateScopeInput:
    out: CreateScopeInput = {}  # type: ignore[typeddict-item]
    if "targets" in data:
        import aws_sdk_networkflowmonitor.types.target_resource_list

        out["targets"] = (
            aws_sdk_networkflowmonitor.types.target_resource_list.deserialize_json(
                data["targets"]
            )
        )
    else:
        raise DeserializationError("CreateScopeInput.targets required")
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "tags" in data:
        import aws_sdk_networkflowmonitor.types.tag_map

        out["tags"] = aws_sdk_networkflowmonitor.types.tag_map.deserialize_json(
            data["tags"]
        )
    return out
