"""Generated from Smithy shape ``com.amazonaws.b2bi#UpdatePartnershipRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_b2bi.types.capability_options
    import aws_sdk_b2bi.types.partner_name
    import aws_sdk_b2bi.types.partnership_capabilities
    import aws_sdk_b2bi.types.partnership_id


class UpdatePartnershipRequest(TypedDict):
    partnership_id: "aws_sdk_b2bi.types.partnership_id.PartnershipId"
    """<p>Specifies the unique, system-generated identifier for a partnership.</p>"""
    name: NotRequired["aws_sdk_b2bi.types.partner_name.PartnerName"]
    """<p>The name of the partnership, used to identify it.</p>"""
    capabilities: NotRequired[
        "aws_sdk_b2bi.types.partnership_capabilities.PartnershipCapabilities"
    ]
    """<p>List of the capabilities associated with this partnership.</p>"""
    capability_options: NotRequired[
        "aws_sdk_b2bi.types.capability_options.CapabilityOptions"
    ]
    """<p>To update, specify the structure that contains the details for the associated capabilities.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdatePartnershipRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "capabilities" in value:
        import aws_sdk_b2bi.types.partnership_capabilities

        out["capabilities"] = (
            aws_sdk_b2bi.types.partnership_capabilities.serialize_aws_json_1_0(
                value["capabilities"]
            )
        )
    if "capability_options" in value:
        import aws_sdk_b2bi.types.capability_options

        out["capabilityOptions"] = (
            aws_sdk_b2bi.types.capability_options.serialize_aws_json_1_0(
                value["capability_options"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdatePartnershipRequest:
    out: UpdatePartnershipRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "capabilities" in data:
        import aws_sdk_b2bi.types.partnership_capabilities

        out["capabilities"] = (
            aws_sdk_b2bi.types.partnership_capabilities.deserialize_aws_json_1_0(
                data["capabilities"]
            )
        )
    if "capabilityOptions" in data:
        import aws_sdk_b2bi.types.capability_options

        out["capability_options"] = (
            aws_sdk_b2bi.types.capability_options.deserialize_aws_json_1_0(
                data["capabilityOptions"]
            )
        )
    return out
