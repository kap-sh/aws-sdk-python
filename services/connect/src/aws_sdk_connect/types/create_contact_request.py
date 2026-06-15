"""Generated from Smithy shape ``com.amazonaws.connect#CreateContactRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.attributes
    import aws_sdk_connect.types.channel
    import aws_sdk_connect.types.client_token
    import aws_sdk_connect.types.contact_id
    import aws_sdk_connect.types.contact_initiation_method
    import aws_sdk_connect.types.contact_references
    import aws_sdk_connect.types.description
    import aws_sdk_connect.types.expiry_duration_in_minutes
    import aws_sdk_connect.types.initiate_as
    import aws_sdk_connect.types.instance_id
    import aws_sdk_connect.types.name
    import aws_sdk_connect.types.segment_attributes
    import aws_sdk_connect.types.user_info


class CreateContactRequest(TypedDict):
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    r"""<p>The identifier of the Connect Customer instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    client_token: NotRequired["aws_sdk_connect.types.client_token.ClientToken"]
    r"""<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href=\"https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/\">Making retries safe with idempotent APIs</a>.</p>"""
    related_contact_id: NotRequired["aws_sdk_connect.types.contact_id.ContactId"]
    """<p>The identifier of the contact in this instance of Connect Customer. </p>"""
    attributes: NotRequired["aws_sdk_connect.types.attributes.Attributes"]
    """<p>A custom key-value pair using an attribute map. The attributes are standard Connect Customer attributes, and can be accessed in flows just like any other contact attributes.</p> <p>There can be up to 32,768 UTF-8 bytes across all key-value pairs per contact. Attribute keys can include only alphanumeric, dash, and underscore characters.</p>"""
    references: NotRequired[
        "aws_sdk_connect.types.contact_references.ContactReferences"
    ]
    """<p>A formatted URL that is shown to an agent in the Contact Control Panel (CCP). Tasks can have the following reference types at the time of creation: <code>URL</code> | <code>NUMBER</code> | <code>STRING</code> | <code>DATE</code> | <code>EMAIL</code> | <code>ATTACHMENT</code>.</p>"""
    channel: "aws_sdk_connect.types.channel.Channel"
    """<p>The channel for the contact.</p> <important> <p>The CHAT channel is not supported. The following information is incorrect. We're working to correct it.</p> </important>"""
    initiation_method: (
        "aws_sdk_connect.types.contact_initiation_method.ContactInitiationMethod"
    )
    """<p>Indicates how the contact was initiated. </p> <important> <p>CreateContact only supports the following initiation methods. Valid values by channel are: </p> <ul> <li> <p>For VOICE: <code>TRANSFER</code> and the subtype <code>connect:ExternalAudio</code> </p> </li> <li> <p>For EMAIL: <code>OUTBOUND</code> | <code>AGENT_REPLY</code> | <code>FLOW</code> </p> </li> <li> <p>For TASK: <code>API</code> </p> </li> </ul> <p>The other channels listed below are incorrect. We're working to correct this information.</p> </important>"""
    expiry_duration_in_minutes: NotRequired[
        "aws_sdk_connect.types.expiry_duration_in_minutes.ExpiryDurationInMinutes"
    ]
    """<p>Number of minutes the contact will be active for before expiring</p>"""
    user_info: NotRequired["aws_sdk_connect.types.user_info.UserInfo"]
    """<p>User details for the contact</p> <important> <p>UserInfo is required when creating an EMAIL contact with <code>OUTBOUND</code> and <code>AGENT_REPLY</code> contact initiation methods.</p> </important>"""
    initiate_as: NotRequired["aws_sdk_connect.types.initiate_as.InitiateAs"]
    """<p>Initial state of the contact when it's created. Only TASK channel contacts can be initiated with <code>COMPLETED</code> state.</p>"""
    name: NotRequired["aws_sdk_connect.types.name.Name"]
    """<p>The name of a the contact.</p>"""
    description: NotRequired["aws_sdk_connect.types.description.Description"]
    """<p>A description of the contact.</p>"""
    segment_attributes: NotRequired[
        "aws_sdk_connect.types.segment_attributes.SegmentAttributes"
    ]
    r"""<p>A set of system defined key-value pairs stored on individual contact segments (unique contact ID) using an attribute map. The attributes are standard Connect Customer attributes. They can be accessed in flows.</p> <p>Attribute keys can include only alphanumeric, -, and _.</p> <p>This field can be used to set Segment Contact Expiry as a duration in minutes.</p> <note> <p>To set contact expiry, a ValueMap must be specified containing the integer number of minutes the contact will be active for before expiring, with <code>SegmentAttributes</code> like { <code> \"connect:ContactExpiry\": {\"ValueMap\" : { \"ExpiryDuration\": { \"ValueInteger\": 135}}}}</code>. </p> </note>"""
    previous_contact_id: NotRequired["aws_sdk_connect.types.contact_id.ContactId"]
    r"""<p>The ID of the previous contact when creating a transfer contact. This value can be provided only for external audio contacts. For more information, see <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/contact-lens-integration.html\">Integrate Connect Customer Contact Lens with external voice systems</a> in the <i>Connect Customer Administrator Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateContactRequest) -> dict:
    out: dict = {}
    out["InstanceId"] = value["instance_id"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    if "related_contact_id" in value:
        out["RelatedContactId"] = value["related_contact_id"]
    if "attributes" in value:
        import aws_sdk_connect.types.attributes

        out["Attributes"] = aws_sdk_connect.types.attributes.serialize_json(
            value["attributes"]
        )
    if "references" in value:
        import aws_sdk_connect.types.contact_references

        out["References"] = aws_sdk_connect.types.contact_references.serialize_json(
            value["references"]
        )
    import aws_sdk_connect.types.channel

    out["Channel"] = aws_sdk_connect.types.channel.serialize_json(value["channel"])
    import aws_sdk_connect.types.contact_initiation_method

    out["InitiationMethod"] = (
        aws_sdk_connect.types.contact_initiation_method.serialize_json(
            value["initiation_method"]
        )
    )
    if "expiry_duration_in_minutes" in value:
        out["ExpiryDurationInMinutes"] = value["expiry_duration_in_minutes"]
    if "user_info" in value:
        import aws_sdk_connect.types.user_info

        out["UserInfo"] = aws_sdk_connect.types.user_info.serialize_json(
            value["user_info"]
        )
    if "initiate_as" in value:
        import aws_sdk_connect.types.initiate_as

        out["InitiateAs"] = aws_sdk_connect.types.initiate_as.serialize_json(
            value["initiate_as"]
        )
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "segment_attributes" in value:
        import aws_sdk_connect.types.segment_attributes

        out["SegmentAttributes"] = (
            aws_sdk_connect.types.segment_attributes.serialize_json(
                value["segment_attributes"]
            )
        )
    if "previous_contact_id" in value:
        out["PreviousContactId"] = value["previous_contact_id"]
    return out


def deserialize_json(data: dict) -> CreateContactRequest:
    out: CreateContactRequest = {}  # type: ignore[typeddict-item]
    if "InstanceId" in data:
        out["instance_id"] = data["InstanceId"]
    else:
        raise DeserializationError("CreateContactRequest.instance_id required")
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    if "RelatedContactId" in data:
        out["related_contact_id"] = data["RelatedContactId"]
    if "Attributes" in data:
        import aws_sdk_connect.types.attributes

        out["attributes"] = aws_sdk_connect.types.attributes.deserialize_json(
            data["Attributes"]
        )
    if "References" in data:
        import aws_sdk_connect.types.contact_references

        out["references"] = aws_sdk_connect.types.contact_references.deserialize_json(
            data["References"]
        )
    if "Channel" in data:
        import aws_sdk_connect.types.channel

        out["channel"] = aws_sdk_connect.types.channel.deserialize_json(data["Channel"])
    else:
        raise DeserializationError("CreateContactRequest.channel required")
    if "InitiationMethod" in data:
        import aws_sdk_connect.types.contact_initiation_method

        out["initiation_method"] = (
            aws_sdk_connect.types.contact_initiation_method.deserialize_json(
                data["InitiationMethod"]
            )
        )
    else:
        raise DeserializationError("CreateContactRequest.initiation_method required")
    if "ExpiryDurationInMinutes" in data:
        out["expiry_duration_in_minutes"] = data["ExpiryDurationInMinutes"]
    if "UserInfo" in data:
        import aws_sdk_connect.types.user_info

        out["user_info"] = aws_sdk_connect.types.user_info.deserialize_json(
            data["UserInfo"]
        )
    if "InitiateAs" in data:
        import aws_sdk_connect.types.initiate_as

        out["initiate_as"] = aws_sdk_connect.types.initiate_as.deserialize_json(
            data["InitiateAs"]
        )
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "SegmentAttributes" in data:
        import aws_sdk_connect.types.segment_attributes

        out["segment_attributes"] = (
            aws_sdk_connect.types.segment_attributes.deserialize_json(
                data["SegmentAttributes"]
            )
        )
    if "PreviousContactId" in data:
        out["previous_contact_id"] = data["PreviousContactId"]
    return out
