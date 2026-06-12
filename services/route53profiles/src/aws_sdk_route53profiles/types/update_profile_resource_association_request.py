"""Generated from Smithy shape ``com.amazonaws.route53profiles#UpdateProfileResourceAssociationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_route53profiles.types.name
    import aws_sdk_route53profiles.types.resource_id
    import aws_sdk_route53profiles.types.resource_properties


class UpdateProfileResourceAssociationRequest(TypedDict):
    profile_resource_association_id: (
        "aws_sdk_route53profiles.types.resource_id.ResourceId"
    )
    """<p> ID of the resource association. </p>"""
    name: NotRequired["aws_sdk_route53profiles.types.name.Name"]
    """<p> Name of the resource association. </p>"""
    resource_properties: NotRequired[
        "aws_sdk_route53profiles.types.resource_properties.ResourceProperties"
    ]
    """<p> If you are adding a DNS Firewall rule group, include also a priority. The priority indicates the processing order for the rule groups, starting with the priority assinged the lowest value. </p> <p>The allowed values for priority are between 100 and 9900.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateProfileResourceAssociationRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "resource_properties" in value:
        out["ResourceProperties"] = value["resource_properties"]
    return out


def deserialize_json(data: dict) -> UpdateProfileResourceAssociationRequest:
    out: UpdateProfileResourceAssociationRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "ResourceProperties" in data:
        out["resource_properties"] = data["ResourceProperties"]
    return out
