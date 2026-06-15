"""Generated from Smithy shape ``com.amazonaws.connect#StartTaskContactRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.attributes
    import aws_sdk_connect.types.client_token
    import aws_sdk_connect.types.contact_flow_id
    import aws_sdk_connect.types.contact_id
    import aws_sdk_connect.types.contact_references
    import aws_sdk_connect.types.description
    import aws_sdk_connect.types.instance_id
    import aws_sdk_connect.types.name
    import aws_sdk_connect.types.quick_connect_id
    import aws_sdk_connect.types.segment_attributes
    import aws_sdk_connect.types.task_attachments
    import aws_sdk_connect.types.task_template_id
    import aws_sdk_connect.types.timestamp


class StartTaskContactRequest(TypedDict):
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    r"""<p>The identifier of the Connect Customer instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    previous_contact_id: NotRequired["aws_sdk_connect.types.contact_id.ContactId"]
    """<p>The identifier of the previous chat, voice, or task contact. Any updates to user-defined attributes to task contacts linked using the same <code>PreviousContactID</code> will affect every contact in the chain. There can be a maximum of 12 linked task contacts in a chain.</p>"""
    contact_flow_id: NotRequired["aws_sdk_connect.types.contact_flow_id.ContactFlowId"]
    """<p>The identifier of the flow for initiating the tasks. To see the ContactFlowId in the Connect Customer admin website, on the navigation menu go to <b>Routing</b>, <b>Flows</b>. Choose the flow. On the flow page, under the name of the flow, choose <b>Show additional flow information</b>. The ContactFlowId is the last part of the ARN, shown here in bold: </p> <p>arn:aws:connect:us-west-2:xxxxxxxxxxxx:instance/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/contact-flow/<b>846ec553-a005-41c0-8341-xxxxxxxxxxxx</b> </p>"""
    attributes: NotRequired["aws_sdk_connect.types.attributes.Attributes"]
    """<p>A custom key-value pair using an attribute map. The attributes are standard Connect Customer attributes, and can be accessed in flows just like any other contact attributes.</p> <p>There can be up to 32,768 UTF-8 bytes across all key-value pairs per contact. Attribute keys can include only alphanumeric, dash, and underscore characters.</p>"""
    name: "aws_sdk_connect.types.name.Name"
    """<p>The name of a task that is shown to an agent in the Contact Control Panel (CCP).</p>"""
    references: NotRequired[
        "aws_sdk_connect.types.contact_references.ContactReferences"
    ]
    """<p>A formatted URL that is shown to an agent in the Contact Control Panel (CCP). Tasks can have the following reference types at the time of creation: <code>URL</code> | <code>NUMBER</code> | <code>STRING</code> | <code>DATE</code> | <code>EMAIL</code>. <code>ATTACHMENT</code> is not a supported reference type during task creation.</p>"""
    description: NotRequired["aws_sdk_connect.types.description.Description"]
    """<p>A description of the task that is shown to an agent in the Contact Control Panel (CCP).</p>"""
    client_token: NotRequired["aws_sdk_connect.types.client_token.ClientToken"]
    r"""<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href=\"https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/\">Making retries safe with idempotent APIs</a>.</p>"""
    scheduled_time: NotRequired["aws_sdk_connect.types.timestamp.Timestamp"]
    """<p>The timestamp, in Unix Epoch seconds format, at which to start running the inbound flow. The scheduled time cannot be in the past. It must be within up to 6 days in future. </p>"""
    task_template_id: NotRequired[
        "aws_sdk_connect.types.task_template_id.TaskTemplateId"
    ]
    r"""<p>A unique identifier for the task template. For more information about task templates, see <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/task-templates.html\">Create task templates</a> in the <i>Connect Customer Administrator Guide</i>. </p>"""
    quick_connect_id: NotRequired[
        "aws_sdk_connect.types.quick_connect_id.QuickConnectId"
    ]
    r"""<p>The identifier for the quick connect. Tasks that are created by using <code>QuickConnectId</code> will use the flow that is defined on agent or queue quick connect. For more information about quick connects, see <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/quick-connects.html\">Create quick connects</a>.</p>"""
    related_contact_id: NotRequired["aws_sdk_connect.types.contact_id.ContactId"]
    r"""<p>The contactId that is <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/tasks.html#linked-tasks\">related</a> to this contact. Linking tasks together by using <code>RelatedContactID</code> copies over contact attributes from the related task contact to the new task contact. All updates to user-defined attributes in the new task contact are limited to the individual contact ID, unlike what happens when tasks are linked by using <code>PreviousContactID</code>. There are no limits to the number of contacts that can be linked by using <code>RelatedContactId</code>. </p>"""
    segment_attributes: NotRequired[
        "aws_sdk_connect.types.segment_attributes.SegmentAttributes"
    ]
    r"""<p>A set of system defined key-value pairs stored on individual contact segments (unique contact ID) using an attribute map. The attributes are standard Connect Customer attributes. They can be accessed in flows.</p> <p>Attribute keys can include only alphanumeric, -, and _.</p> <p>This field can be used to set Contact Expiry as a duration in minutes and set a UserId for the User who created a task.</p> <note> <p>To set contact expiry, a ValueMap must be specified containing the integer number of minutes the contact will be active for before expiring, with <code>SegmentAttributes</code> like { <code> \"connect:ContactExpiry\": {\"ValueMap\" : { \"ExpiryDuration\": { \"ValueInteger\": 135}}}}</code>. </p> <p>To set the created by user, a valid AgentResourceId must be supplied, with <code>SegmentAttributes</code> like { <code>\"connect:CreatedByUser\" { \"ValueString\": \"arn:aws:connect:us-west-2:xxxxxxxxxxxx:instance/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/agent/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx\"}}}</code>. </p> </note>"""
    attachments: NotRequired["aws_sdk_connect.types.task_attachments.TaskAttachments"]
    """<p>List of S3 presigned URLs of task attachments and their file name. You can have a maximum of 5 attachments per task.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartTaskContactRequest) -> dict:
    out: dict = {}
    out["InstanceId"] = value["instance_id"]
    if "previous_contact_id" in value:
        out["PreviousContactId"] = value["previous_contact_id"]
    if "contact_flow_id" in value:
        out["ContactFlowId"] = value["contact_flow_id"]
    if "attributes" in value:
        import aws_sdk_connect.types.attributes

        out["Attributes"] = aws_sdk_connect.types.attributes.serialize_json(
            value["attributes"]
        )
    out["Name"] = value["name"]
    if "references" in value:
        import aws_sdk_connect.types.contact_references

        out["References"] = aws_sdk_connect.types.contact_references.serialize_json(
            value["references"]
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    if "scheduled_time" in value:
        import aws_sdk_connect.types.timestamp

        out["ScheduledTime"] = aws_sdk_connect.types.timestamp.serialize_json(
            value["scheduled_time"]
        )
    if "task_template_id" in value:
        out["TaskTemplateId"] = value["task_template_id"]
    if "quick_connect_id" in value:
        out["QuickConnectId"] = value["quick_connect_id"]
    if "related_contact_id" in value:
        out["RelatedContactId"] = value["related_contact_id"]
    if "segment_attributes" in value:
        import aws_sdk_connect.types.segment_attributes

        out["SegmentAttributes"] = (
            aws_sdk_connect.types.segment_attributes.serialize_json(
                value["segment_attributes"]
            )
        )
    if "attachments" in value:
        import aws_sdk_connect.types.task_attachments

        out["Attachments"] = aws_sdk_connect.types.task_attachments.serialize_json(
            value["attachments"]
        )
    return out


def deserialize_json(data: dict) -> StartTaskContactRequest:
    out: StartTaskContactRequest = {}  # type: ignore[typeddict-item]
    if "InstanceId" in data:
        out["instance_id"] = data["InstanceId"]
    else:
        raise DeserializationError("StartTaskContactRequest.instance_id required")
    if "PreviousContactId" in data:
        out["previous_contact_id"] = data["PreviousContactId"]
    if "ContactFlowId" in data:
        out["contact_flow_id"] = data["ContactFlowId"]
    if "Attributes" in data:
        import aws_sdk_connect.types.attributes

        out["attributes"] = aws_sdk_connect.types.attributes.deserialize_json(
            data["Attributes"]
        )
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("StartTaskContactRequest.name required")
    if "References" in data:
        import aws_sdk_connect.types.contact_references

        out["references"] = aws_sdk_connect.types.contact_references.deserialize_json(
            data["References"]
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    if "ScheduledTime" in data:
        import aws_sdk_connect.types.timestamp

        out["scheduled_time"] = aws_sdk_connect.types.timestamp.deserialize_json(
            data["ScheduledTime"]
        )
    if "TaskTemplateId" in data:
        out["task_template_id"] = data["TaskTemplateId"]
    if "QuickConnectId" in data:
        out["quick_connect_id"] = data["QuickConnectId"]
    if "RelatedContactId" in data:
        out["related_contact_id"] = data["RelatedContactId"]
    if "SegmentAttributes" in data:
        import aws_sdk_connect.types.segment_attributes

        out["segment_attributes"] = (
            aws_sdk_connect.types.segment_attributes.deserialize_json(
                data["SegmentAttributes"]
            )
        )
    if "Attachments" in data:
        import aws_sdk_connect.types.task_attachments

        out["attachments"] = aws_sdk_connect.types.task_attachments.deserialize_json(
            data["Attachments"]
        )
    return out
