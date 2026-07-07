"""Generated from Smithy shape ``com.amazonaws.workmail#UpdateResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_workmail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workmail.types.booking_options
    import aws_sdk_workmail.types.boolean_object
    import aws_sdk_workmail.types.entity_identifier
    import aws_sdk_workmail.types.new_resource_description
    import aws_sdk_workmail.types.organization_id
    import aws_sdk_workmail.types.resource_name
    import aws_sdk_workmail.types.resource_type


class UpdateResourceRequest(TypedDict, closed=True):
    organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId"
    """<p>The identifier associated with the organization for which the resource is updated.</p>"""
    resource_id: "aws_sdk_workmail.types.entity_identifier.EntityIdentifier"
    """<p>The identifier of the resource to be updated.</p> <p>The identifier can accept <i>ResourceId</i>, <i>Resourcename</i>, or <i>email</i>. The following identity formats are available:</p> <ul> <li> <p>Resource ID: r-0123456789a0123456789b0123456789</p> </li> <li> <p>Email address: resource@domain.tld</p> </li> <li> <p>Resource name: resource</p> </li> </ul>"""
    name: NotRequired["aws_sdk_workmail.types.resource_name.ResourceName"]
    """<p>The name of the resource to be updated.</p>"""
    booking_options: NotRequired[
        "aws_sdk_workmail.types.booking_options.BookingOptions"
    ]
    """<p>The resource's booking options to be updated.</p>"""
    description: NotRequired[
        "aws_sdk_workmail.types.new_resource_description.NewResourceDescription"
    ]
    """<p>Updates the resource description.</p>"""
    type: NotRequired["aws_sdk_workmail.types.resource_type.ResourceType"]
    """<p>Updates the resource type.</p>"""
    hidden_from_global_address_list: NotRequired[
        "aws_sdk_workmail.types.boolean_object.BooleanObject"
    ]
    """<p>If enabled, the resource is hidden from the global address list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateResourceRequest) -> dict:
    out: dict = {}
    out["OrganizationId"] = value["organization_id"]
    out["ResourceId"] = value["resource_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "booking_options" in value:
        import aws_sdk_workmail.types.booking_options

        out["BookingOptions"] = (
            aws_sdk_workmail.types.booking_options.serialize_aws_json_1_1(
                value["booking_options"]
            )
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "type" in value:
        import aws_sdk_workmail.types.resource_type

        out["Type"] = aws_sdk_workmail.types.resource_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "hidden_from_global_address_list" in value:
        out["HiddenFromGlobalAddressList"] = value["hidden_from_global_address_list"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateResourceRequest:
    out: UpdateResourceRequest = {}  # type: ignore[typeddict-item]
    if "OrganizationId" in data:
        out["organization_id"] = data["OrganizationId"]
    else:
        raise DeserializationError("UpdateResourceRequest.organization_id required")
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    else:
        raise DeserializationError("UpdateResourceRequest.resource_id required")
    if "Name" in data:
        out["name"] = data["Name"]
    if "BookingOptions" in data:
        import aws_sdk_workmail.types.booking_options

        out["booking_options"] = (
            aws_sdk_workmail.types.booking_options.deserialize_aws_json_1_1(
                data["BookingOptions"]
            )
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "Type" in data:
        import aws_sdk_workmail.types.resource_type

        out["type"] = aws_sdk_workmail.types.resource_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    if "HiddenFromGlobalAddressList" in data:
        out["hidden_from_global_address_list"] = data["HiddenFromGlobalAddressList"]
    return out
