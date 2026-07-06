"""Generated from Smithy shape ``com.amazonaws.fms#DiscoveredResource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fms.types.aws_account_id
    import aws_sdk_fms.types.identifier
    import aws_sdk_fms.types.resource_name
    import aws_sdk_fms.types.resource_type


class DiscoveredResource(TypedDict, closed=True):
    uri: NotRequired["aws_sdk_fms.types.identifier.Identifier"]
    """<p>The universal resource identifier (URI) of the discovered resource.</p>"""
    account_id: NotRequired["aws_sdk_fms.types.aws_account_id.AWSAccountId"]
    """<p>The Amazon Web Services account ID associated with the discovered resource.</p>"""
    type: NotRequired["aws_sdk_fms.types.resource_type.ResourceType"]
    """<p>The type of the discovered resource.</p>"""
    name: NotRequired["aws_sdk_fms.types.resource_name.ResourceName"]
    """<p>The name of the discovered resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DiscoveredResource) -> dict:
    out: dict = {}
    if "uri" in value:
        out["URI"] = value["uri"]
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "type" in value:
        out["Type"] = value["type"]
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DiscoveredResource:
    out: DiscoveredResource = {}  # type: ignore[typeddict-item]
    if "URI" in data:
        out["uri"] = data["URI"]
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    if "Type" in data:
        out["type"] = data["Type"]
    if "Name" in data:
        out["name"] = data["Name"]
    return out
