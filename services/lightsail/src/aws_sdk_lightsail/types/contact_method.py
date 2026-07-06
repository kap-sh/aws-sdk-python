"""Generated from Smithy shape ``com.amazonaws.lightsail#ContactMethod``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.contact_method_status
    import aws_sdk_lightsail.types.contact_protocol
    import aws_sdk_lightsail.types.iso_date
    import aws_sdk_lightsail.types.non_empty_string
    import aws_sdk_lightsail.types.resource_location
    import aws_sdk_lightsail.types.resource_name
    import aws_sdk_lightsail.types.resource_type
    import aws_sdk_lightsail.types.string
    import aws_sdk_lightsail.types.tag_list


class ContactMethod(TypedDict, closed=True):
    contact_endpoint: NotRequired[
        "aws_sdk_lightsail.types.non_empty_string.NonEmptyString"
    ]
    """<p>The destination of the contact method, such as an email address or a mobile phone number.</p>"""
    status: NotRequired[
        "aws_sdk_lightsail.types.contact_method_status.ContactMethodStatus"
    ]
    """<p>The current status of the contact method.</p> <p>A contact method has the following possible status:</p> <ul> <li> <p> <code>PendingVerification</code> - The contact method has not yet been verified, and the verification has not yet expired.</p> </li> <li> <p> <code>Valid</code> - The contact method has been verified.</p> </li> <li> <p> <code>InValid</code> - An attempt was made to verify the contact method, but the verification has expired.</p> </li> </ul>"""
    protocol: NotRequired["aws_sdk_lightsail.types.contact_protocol.ContactProtocol"]
    """<p>The protocol of the contact method, such as email or SMS (text messaging).</p>"""
    name: NotRequired["aws_sdk_lightsail.types.resource_name.ResourceName"]
    """<p>The name of the contact method.</p>"""
    arn: NotRequired["aws_sdk_lightsail.types.non_empty_string.NonEmptyString"]
    """<p>The Amazon Resource Name (ARN) of the contact method.</p>"""
    created_at: NotRequired["aws_sdk_lightsail.types.iso_date.IsoDate"]
    """<p>The timestamp when the contact method was created.</p>"""
    location: NotRequired["aws_sdk_lightsail.types.resource_location.ResourceLocation"]
    """<p>An object that describes the location of the contact method, such as the Amazon Web Services Region and Availability Zone.</p>"""
    resource_type: NotRequired["aws_sdk_lightsail.types.resource_type.ResourceType"]
    """<p>The Lightsail resource type of the contact method.</p>"""
    support_code: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>The support code. Include this code in your email to support when you have questions about your Lightsail contact method. This code enables our support team to look up your Lightsail information more easily.</p>"""
    tags: NotRequired["aws_sdk_lightsail.types.tag_list.TagList"]
    r"""<p>The tag keys and optional values for the resource. For more information about tags in Lightsail, see the <a href=\"https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-tags\">Amazon Lightsail Developer Guide</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContactMethod) -> dict:
    out: dict = {}
    if "contact_endpoint" in value:
        out["contactEndpoint"] = value["contact_endpoint"]
    if "status" in value:
        import aws_sdk_lightsail.types.contact_method_status

        out["status"] = (
            aws_sdk_lightsail.types.contact_method_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "protocol" in value:
        import aws_sdk_lightsail.types.contact_protocol

        out["protocol"] = (
            aws_sdk_lightsail.types.contact_protocol.serialize_aws_json_1_1(
                value["protocol"]
            )
        )
    if "name" in value:
        out["name"] = value["name"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "created_at" in value:
        import aws_sdk_lightsail.types.iso_date

        out["createdAt"] = aws_sdk_lightsail.types.iso_date.serialize_aws_json_1_1(
            value["created_at"]
        )
    if "location" in value:
        import aws_sdk_lightsail.types.resource_location

        out["location"] = (
            aws_sdk_lightsail.types.resource_location.serialize_aws_json_1_1(
                value["location"]
            )
        )
    if "resource_type" in value:
        import aws_sdk_lightsail.types.resource_type

        out["resourceType"] = (
            aws_sdk_lightsail.types.resource_type.serialize_aws_json_1_1(
                value["resource_type"]
            )
        )
    if "support_code" in value:
        out["supportCode"] = value["support_code"]
    if "tags" in value:
        import aws_sdk_lightsail.types.tag_list

        out["tags"] = aws_sdk_lightsail.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ContactMethod:
    out: ContactMethod = {}  # type: ignore[typeddict-item]
    if "contactEndpoint" in data:
        out["contact_endpoint"] = data["contactEndpoint"]
    if "status" in data:
        import aws_sdk_lightsail.types.contact_method_status

        out["status"] = (
            aws_sdk_lightsail.types.contact_method_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    if "protocol" in data:
        import aws_sdk_lightsail.types.contact_protocol

        out["protocol"] = (
            aws_sdk_lightsail.types.contact_protocol.deserialize_aws_json_1_1(
                data["protocol"]
            )
        )
    if "name" in data:
        out["name"] = data["name"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "createdAt" in data:
        import aws_sdk_lightsail.types.iso_date

        out["created_at"] = aws_sdk_lightsail.types.iso_date.deserialize_aws_json_1_1(
            data["createdAt"]
        )
    if "location" in data:
        import aws_sdk_lightsail.types.resource_location

        out["location"] = (
            aws_sdk_lightsail.types.resource_location.deserialize_aws_json_1_1(
                data["location"]
            )
        )
    if "resourceType" in data:
        import aws_sdk_lightsail.types.resource_type

        out["resource_type"] = (
            aws_sdk_lightsail.types.resource_type.deserialize_aws_json_1_1(
                data["resourceType"]
            )
        )
    if "supportCode" in data:
        out["support_code"] = data["supportCode"]
    if "tags" in data:
        import aws_sdk_lightsail.types.tag_list

        out["tags"] = aws_sdk_lightsail.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    return out
