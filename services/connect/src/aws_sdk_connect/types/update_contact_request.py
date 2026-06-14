"""Generated from Smithy shape ``com.amazonaws.connect#UpdateContactRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.contact_id
    import aws_sdk_connect.types.contact_references
    import aws_sdk_connect.types.description
    import aws_sdk_connect.types.endpoint
    import aws_sdk_connect.types.instance_id
    import aws_sdk_connect.types.name
    import aws_sdk_connect.types.queue_info_input
    import aws_sdk_connect.types.segment_attributes
    import aws_sdk_connect.types.user_info


class UpdateContactRequest(TypedDict):
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    r"""<p>The identifier of the Connect Customer instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    contact_id: "aws_sdk_connect.types.contact_id.ContactId"
    """<p>The identifier of the contact. This is the identifier of the contact associated with the first interaction with your contact center.</p>"""
    name: NotRequired["aws_sdk_connect.types.name.Name"]
    """<p>The name of the contact.</p>"""
    description: NotRequired["aws_sdk_connect.types.description.Description"]
    """<p>The description of the contact.</p>"""
    references: NotRequired[
        "aws_sdk_connect.types.contact_references.ContactReferences"
    ]
    """<p>Well-formed data on contact, shown to agents on Contact Control Panel (CCP).</p>"""
    segment_attributes: NotRequired[
        "aws_sdk_connect.types.segment_attributes.SegmentAttributes"
    ]
    """<p>A set of system defined key-value pairs stored on individual contact segments (unique contact ID) using an attribute map. The attributes are standard Connect Customer attributes. They can be accessed in flows.</p> <p>Attribute keys can include only alphanumeric, -, and _.</p> <p>This field can be used to show channel subtype, such as <code>connect:Guide</code>.</p> <p>Contact Expiry, and user-defined attributes (String - String) that are defined in predefined attributes, can be updated by using the UpdateContact API.</p>"""
    queue_info: NotRequired["aws_sdk_connect.types.queue_info_input.QueueInfoInput"]
    r"""<p> Information about the queue associated with a contact. This parameter can only be updated for external audio contacts. It is used when you integrate third-party systems with Contact Lens for analytics. For more information, see <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/contact-lens-integration.html\">Connect Customer Contact Lens integration</a> in the <i> Connect Customer Administrator Guide</i>.</p>"""
    user_info: NotRequired["aws_sdk_connect.types.user_info.UserInfo"]
    r"""<p>Information about the agent associated with a contact. This parameter can only be updated for external audio contacts. It is used when you integrate third-party systems with Contact Lens for analytics. For more information, see <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/contact-lens-integration.html\">Connect Customer Contact Lens integration</a> in the <i> Connect Customer Administrator Guide</i>.</p>"""
    customer_endpoint: NotRequired["aws_sdk_connect.types.endpoint.Endpoint"]
    r"""<p>The endpoint of the customer for which the contact was initiated. For external audio contacts, this is usually the end customer's phone number. This value can only be updated for external audio contacts. For more information, see <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/contact-lens-integration.html\">Connect Customer Contact Lens integration</a> in the <i>Connect Customer Administrator Guide</i>.</p>"""
    system_endpoint: NotRequired["aws_sdk_connect.types.endpoint.Endpoint"]
    r"""<p>External system endpoint for the contact was initiated. For external audio contacts, this is the phone number of the external system such as the contact center. This value can only be updated for external audio contacts. For more information, see <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/contact-lens-integration.html\">Connect Customer Contact Lens integration</a> in the <i>Connect Customer Administrator Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateContactRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "references" in value:
        import aws_sdk_connect.types.contact_references

        out["References"] = aws_sdk_connect.types.contact_references.serialize_json(
            value["references"]
        )
    if "segment_attributes" in value:
        import aws_sdk_connect.types.segment_attributes

        out["SegmentAttributes"] = (
            aws_sdk_connect.types.segment_attributes.serialize_json(
                value["segment_attributes"]
            )
        )
    if "queue_info" in value:
        import aws_sdk_connect.types.queue_info_input

        out["QueueInfo"] = aws_sdk_connect.types.queue_info_input.serialize_json(
            value["queue_info"]
        )
    if "user_info" in value:
        import aws_sdk_connect.types.user_info

        out["UserInfo"] = aws_sdk_connect.types.user_info.serialize_json(
            value["user_info"]
        )
    if "customer_endpoint" in value:
        import aws_sdk_connect.types.endpoint

        out["CustomerEndpoint"] = aws_sdk_connect.types.endpoint.serialize_json(
            value["customer_endpoint"]
        )
    if "system_endpoint" in value:
        import aws_sdk_connect.types.endpoint

        out["SystemEndpoint"] = aws_sdk_connect.types.endpoint.serialize_json(
            value["system_endpoint"]
        )
    return out


def deserialize_json(data: dict) -> UpdateContactRequest:
    out: UpdateContactRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "References" in data:
        import aws_sdk_connect.types.contact_references

        out["references"] = aws_sdk_connect.types.contact_references.deserialize_json(
            data["References"]
        )
    if "SegmentAttributes" in data:
        import aws_sdk_connect.types.segment_attributes

        out["segment_attributes"] = (
            aws_sdk_connect.types.segment_attributes.deserialize_json(
                data["SegmentAttributes"]
            )
        )
    if "QueueInfo" in data:
        import aws_sdk_connect.types.queue_info_input

        out["queue_info"] = aws_sdk_connect.types.queue_info_input.deserialize_json(
            data["QueueInfo"]
        )
    if "UserInfo" in data:
        import aws_sdk_connect.types.user_info

        out["user_info"] = aws_sdk_connect.types.user_info.deserialize_json(
            data["UserInfo"]
        )
    if "CustomerEndpoint" in data:
        import aws_sdk_connect.types.endpoint

        out["customer_endpoint"] = aws_sdk_connect.types.endpoint.deserialize_json(
            data["CustomerEndpoint"]
        )
    if "SystemEndpoint" in data:
        import aws_sdk_connect.types.endpoint

        out["system_endpoint"] = aws_sdk_connect.types.endpoint.deserialize_json(
            data["SystemEndpoint"]
        )
    return out
