"""Generated from Smithy shape ``com.amazonaws.lightsail#ResourceReceivingAccess``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.non_empty_string


class ResourceReceivingAccess(TypedDict, closed=True):
    name: NotRequired["aws_sdk_lightsail.types.non_empty_string.NonEmptyString"]
    """<p>The name of the Lightsail instance.</p>"""
    resource_type: NotRequired[
        "aws_sdk_lightsail.types.non_empty_string.NonEmptyString"
    ]
    """<p>The Lightsail resource type (for example, <code>Instance</code>).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceReceivingAccess) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "resource_type" in value:
        out["resourceType"] = value["resource_type"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceReceivingAccess:
    out: ResourceReceivingAccess = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "resourceType" in data:
        out["resource_type"] = data["resourceType"]
    return out
