"""Generated from Smithy shape ``com.amazonaws.connect#Contact``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.additional_email_recipients
    import capo_connect.types.agent_info
    import capo_connect.types.answering_machine_detection_status
    import capo_connect.types.arn
    import capo_connect.types.attributes
    import capo_connect.types.campaign
    import capo_connect.types.channel
    import capo_connect.types.chat_metrics
    import capo_connect.types.contact_details
    import capo_connect.types.contact_evaluations
    import capo_connect.types.contact_id
    import capo_connect.types.contact_initiation_method
    import capo_connect.types.contact_tag_map
    import capo_connect.types.customer
    import capo_connect.types.customer_id
    import capo_connect.types.customer_voice_activity
    import capo_connect.types.description
    import capo_connect.types.disconnect_details
    import capo_connect.types.endpoint_info
    import capo_connect.types.global_resiliency_metadata
    import capo_connect.types.name
    import capo_connect.types.next_contacts
    import capo_connect.types.outbound_strategy
    import capo_connect.types.quality_metrics
    import capo_connect.types.queue_info
    import capo_connect.types.queue_priority
    import capo_connect.types.queue_time_adjustment_seconds
    import capo_connect.types.recordings
    import capo_connect.types.routing_criteria
    import capo_connect.types.segment_attributes
    import capo_connect.types.string
    import capo_connect.types.task_template_info_v2
    import capo_connect.types.timestamp
    import capo_connect.types.total_pause_count
    import capo_connect.types.total_pause_duration_in_seconds
    import capo_connect.types.wisdom_info


class Contact(TypedDict, closed=True):
    arn: NotRequired["capo_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) for the contact.</p>"""
    id: NotRequired["capo_connect.types.contact_id.ContactId"]
    """<p>The identifier for the contact.</p>"""
    initial_contact_id: NotRequired["capo_connect.types.contact_id.ContactId"]
    """<p>If this contact is related to other contacts, this is the ID of the initial contact.</p>"""
    previous_contact_id: NotRequired["capo_connect.types.contact_id.ContactId"]
    """<p>If this contact is not the first contact, this is the ID of the previous contact.</p>"""
    contact_association_id: NotRequired["capo_connect.types.contact_id.ContactId"]
    """<p>This is the root contactId which is used as a unique identifier for all subsequent contacts in a contact tree.</p>"""
    initiation_method: NotRequired[
        "capo_connect.types.contact_initiation_method.ContactInitiationMethod"
    ]
    """<p>Indicates how the contact was initiated.</p>"""
    name: NotRequired["capo_connect.types.name.Name"]
    """<p>The name of the contact.</p>"""
    description: NotRequired["capo_connect.types.description.Description"]
    """<p>The description of the contact.</p>"""
    channel: NotRequired["capo_connect.types.channel.Channel"]
    """<p>How the contact reached your contact center.</p>"""
    queue_info: NotRequired["capo_connect.types.queue_info.QueueInfo"]
    """<p>If this contact was queued, this contains information about the queue. </p>"""
    agent_info: NotRequired["capo_connect.types.agent_info.AgentInfo"]
    """<p>Information about the agent who accepted the contact.</p>"""
    initiation_timestamp: NotRequired["capo_connect.types.timestamp.Timestamp"]
    """<p>The date and time this contact was initiated, in UTC time. For <code>INBOUND</code>, this is when the contact arrived. For <code>OUTBOUND</code>, this is when the agent began dialing. For <code>CALLBACK</code>, this is when the callback contact was created. For <code>TRANSFER</code> and <code>QUEUE_TRANSFER</code>, this is when the transfer was initiated. For <code>API</code>, this is when the request arrived. For <code>EXTERNAL_OUTBOUND</code>, this is when the agent started dialing the external participant. For <code>MONITOR</code>, this is when the supervisor started listening to a contact.</p>"""
    disconnect_timestamp: NotRequired["capo_connect.types.timestamp.Timestamp"]
    """<p>The date and time that the customer endpoint disconnected from the current contact, in UTC time. In transfer scenarios, the DisconnectTimestamp of the previous contact indicates the date and time when that contact ended.</p>"""
    last_update_timestamp: NotRequired["capo_connect.types.timestamp.Timestamp"]
    """<p>The timestamp when contact was last updated.</p>"""
    last_paused_timestamp: NotRequired["capo_connect.types.timestamp.Timestamp"]
    """<p>The timestamp when the contact was last paused.</p>"""
    last_resumed_timestamp: NotRequired["capo_connect.types.timestamp.Timestamp"]
    """<p>The timestamp when the contact was last resumed.</p>"""
    ring_start_timestamp: NotRequired["capo_connect.types.timestamp.Timestamp"]
    """<p>The timestamp when ringing started for a campaign call.</p>"""
    total_pause_count: NotRequired[
        "capo_connect.types.total_pause_count.TotalPauseCount"
    ]
    """<p>Total pause count for a contact.</p>"""
    total_pause_duration_in_seconds: NotRequired[
        "capo_connect.types.total_pause_duration_in_seconds.TotalPauseDurationInSeconds"
    ]
    """<p>Total pause duration for a contact in seconds.</p>"""
    scheduled_timestamp: NotRequired["capo_connect.types.timestamp.Timestamp"]
    """<p>The timestamp, in Unix epoch time format, at which to start running the inbound flow. </p>"""
    related_contact_id: NotRequired["capo_connect.types.contact_id.ContactId"]
    r"""<p>The contactId that is <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/chat-persistence.html#relatedcontactid\">related</a> to this contact.</p>"""
    wisdom_info: NotRequired["capo_connect.types.wisdom_info.WisdomInfo"]
    """<p>Information about Connect Customer Wisdom.</p>"""
    customer_id: NotRequired["capo_connect.types.customer_id.CustomerId"]
    """<p>The customer's identification number. For example, the <code>CustomerId</code> may be a customer number from your CRM. You can create a Lambda function to pull the unique customer ID of the caller from your CRM system. If you enable Connect Customer Voice ID capability, this attribute is populated with the <code>CustomerSpeakerId</code> of the caller.</p>"""
    customer_endpoint: NotRequired["capo_connect.types.endpoint_info.EndpointInfo"]
    """<p>The customer or external third party participant endpoint.</p>"""
    system_endpoint: NotRequired["capo_connect.types.endpoint_info.EndpointInfo"]
    """<p>The system endpoint. For <code>INBOUND</code>, this is the phone number or email address that the customer dialed. For <code>OUTBOUND</code> and <code>EXTERNAL_OUTBOUND</code>, this is the outbound caller ID number assigned to the outbound queue that is used to dial the customer. For callback, this shows up as Softphone for calls handled by agents with softphone.</p>"""
    queue_time_adjustment_seconds: NotRequired[
        "capo_connect.types.queue_time_adjustment_seconds.QueueTimeAdjustmentSeconds"
    ]
    """<p>An integer that represents the queue time adjust to be applied to the contact, in seconds (longer / larger queue time are routed preferentially). Cannot be specified if the QueuePriority is specified. Must be statically defined and a valid integer value.</p>"""
    queue_priority: NotRequired["capo_connect.types.queue_priority.QueuePriority"]
    """<p>An integer that represents the queue priority to be applied to the contact (lower priorities are routed preferentially). Cannot be specified if the QueueTimeAdjustmentSeconds is specified. Must be statically defined, must be larger than zero, and a valid integer value. Default Value is 5.</p>"""
    tags: NotRequired["capo_connect.types.contact_tag_map.ContactTagMap"]
    """<p>Tags associated with the contact. This contains both Amazon Web Services generated and user-defined tags.</p>"""
    connected_to_system_timestamp: NotRequired["capo_connect.types.timestamp.Timestamp"]
    """<p>The timestamp when customer endpoint connected to Connect Customer.</p>"""
    routing_criteria: NotRequired["capo_connect.types.routing_criteria.RoutingCriteria"]
    """<p>Latest routing criteria on the contact.</p>"""
    customer: NotRequired["capo_connect.types.customer.Customer"]
    """<p>Information about the Customer on the contact.</p>"""
    campaign: NotRequired["capo_connect.types.campaign.Campaign"]
    answering_machine_detection_status: NotRequired[
        "capo_connect.types.answering_machine_detection_status.AnsweringMachineDetectionStatus"
    ]
    r"""<p>Indicates how an <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/how-to-create-campaigns.html\">outbound campaign</a> call is actually disposed if the contact is connected to Connect Customer.</p>"""
    customer_voice_activity: NotRequired[
        "capo_connect.types.customer_voice_activity.CustomerVoiceActivity"
    ]
    """<p>Information about customer’s voice activity.</p>"""
    quality_metrics: NotRequired["capo_connect.types.quality_metrics.QualityMetrics"]
    """<p>Information about the quality of the participant's media connection.</p>"""
    chat_metrics: NotRequired["capo_connect.types.chat_metrics.ChatMetrics"]
    """<p>Information about how agent, bot, and customer interact in a chat contact.</p>"""
    disconnect_details: NotRequired[
        "capo_connect.types.disconnect_details.DisconnectDetails"
    ]
    """<p>Information about the call disconnect experience.</p>"""
    additional_email_recipients: NotRequired[
        "capo_connect.types.additional_email_recipients.AdditionalEmailRecipients"
    ]
    """<p>List of additional email addresses for an email contact.</p>"""
    segment_attributes: NotRequired[
        "capo_connect.types.segment_attributes.SegmentAttributes"
    ]
    """<p>A set of system defined key-value pairs stored on individual contact segments using an attribute map. The attributes are standard Connect Customer attributes and can be accessed in flows. Attribute keys can include only alphanumeric, -, and _ characters. This field can be used to show channel subtype. For example, <code>connect:Guide</code> or <code>connect:SMS</code>.</p>"""
    recordings: NotRequired["capo_connect.types.recordings.Recordings"]
    """<p>If recording was enabled, this is information about the recordings.</p>"""
    disconnect_reason: NotRequired["capo_connect.types.string.String"]
    r"""<p>The disconnect reason for the contact. For a list and description of all the possible disconnect reasons by channel, see DisconnectReason under <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/ctr-data-model.html#ctr-ContactTraceRecord\">ContactTraceRecord</a> in the <i>Connect Customer Administrator Guide</i>. </p>"""
    contact_evaluations: NotRequired[
        "capo_connect.types.contact_evaluations.ContactEvaluations"
    ]
    """<p>Information about the contact evaluations where the key is the FormId, which is a unique identifier for the form.</p>"""
    task_template_info: NotRequired[
        "capo_connect.types.task_template_info_v2.TaskTemplateInfoV2"
    ]
    """<p>If this contact was created using a task template, this contains information about the task template.</p>"""
    contact_details: NotRequired["capo_connect.types.contact_details.ContactDetails"]
    """<p>A map of string key/value pairs that contain user-defined attributes which are lightly typed within the contact. This object is used only for task contacts.</p>"""
    outbound_strategy: NotRequired[
        "capo_connect.types.outbound_strategy.OutboundStrategy"
    ]
    """<p>Information about the outbound strategy.</p>"""
    attributes: NotRequired["capo_connect.types.attributes.Attributes"]
    """<p>The attributes of the contact.</p>"""
    next_contacts: NotRequired["capo_connect.types.next_contacts.NextContacts"]
    """<p> List of next contact entries for the contact. </p>"""
    global_resiliency_metadata: NotRequired[
        "capo_connect.types.global_resiliency_metadata.GlobalResiliencyMetadata"
    ]
    """<p>Information about the global resiliency configuration for the contact, including traffic distribution details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Contact) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "id" in value:
        out["Id"] = value["id"]
    if "initial_contact_id" in value:
        out["InitialContactId"] = value["initial_contact_id"]
    if "previous_contact_id" in value:
        out["PreviousContactId"] = value["previous_contact_id"]
    if "contact_association_id" in value:
        out["ContactAssociationId"] = value["contact_association_id"]
    if "initiation_method" in value:
        import capo_connect.types.contact_initiation_method

        out["InitiationMethod"] = (
            capo_connect.types.contact_initiation_method.serialize_json(
                value["initiation_method"]
            )
        )
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "channel" in value:
        import capo_connect.types.channel

        out["Channel"] = capo_connect.types.channel.serialize_json(value["channel"])
    if "queue_info" in value:
        import capo_connect.types.queue_info

        out["QueueInfo"] = capo_connect.types.queue_info.serialize_json(
            value["queue_info"]
        )
    if "agent_info" in value:
        import capo_connect.types.agent_info

        out["AgentInfo"] = capo_connect.types.agent_info.serialize_json(
            value["agent_info"]
        )
    if "initiation_timestamp" in value:
        import capo_connect.types.timestamp

        out["InitiationTimestamp"] = capo_connect.types.timestamp.serialize_json(
            value["initiation_timestamp"]
        )
    if "disconnect_timestamp" in value:
        import capo_connect.types.timestamp

        out["DisconnectTimestamp"] = capo_connect.types.timestamp.serialize_json(
            value["disconnect_timestamp"]
        )
    if "last_update_timestamp" in value:
        import capo_connect.types.timestamp

        out["LastUpdateTimestamp"] = capo_connect.types.timestamp.serialize_json(
            value["last_update_timestamp"]
        )
    if "last_paused_timestamp" in value:
        import capo_connect.types.timestamp

        out["LastPausedTimestamp"] = capo_connect.types.timestamp.serialize_json(
            value["last_paused_timestamp"]
        )
    if "last_resumed_timestamp" in value:
        import capo_connect.types.timestamp

        out["LastResumedTimestamp"] = capo_connect.types.timestamp.serialize_json(
            value["last_resumed_timestamp"]
        )
    if "ring_start_timestamp" in value:
        import capo_connect.types.timestamp

        out["RingStartTimestamp"] = capo_connect.types.timestamp.serialize_json(
            value["ring_start_timestamp"]
        )
    if "total_pause_count" in value:
        out["TotalPauseCount"] = value["total_pause_count"]
    if "total_pause_duration_in_seconds" in value:
        out["TotalPauseDurationInSeconds"] = value["total_pause_duration_in_seconds"]
    if "scheduled_timestamp" in value:
        import capo_connect.types.timestamp

        out["ScheduledTimestamp"] = capo_connect.types.timestamp.serialize_json(
            value["scheduled_timestamp"]
        )
    if "related_contact_id" in value:
        out["RelatedContactId"] = value["related_contact_id"]
    if "wisdom_info" in value:
        import capo_connect.types.wisdom_info

        out["WisdomInfo"] = capo_connect.types.wisdom_info.serialize_json(
            value["wisdom_info"]
        )
    if "customer_id" in value:
        out["CustomerId"] = value["customer_id"]
    if "customer_endpoint" in value:
        import capo_connect.types.endpoint_info

        out["CustomerEndpoint"] = capo_connect.types.endpoint_info.serialize_json(
            value["customer_endpoint"]
        )
    if "system_endpoint" in value:
        import capo_connect.types.endpoint_info

        out["SystemEndpoint"] = capo_connect.types.endpoint_info.serialize_json(
            value["system_endpoint"]
        )
    if "queue_time_adjustment_seconds" in value:
        out["QueueTimeAdjustmentSeconds"] = value["queue_time_adjustment_seconds"]
    if "queue_priority" in value:
        out["QueuePriority"] = value["queue_priority"]
    if "tags" in value:
        import capo_connect.types.contact_tag_map

        out["Tags"] = capo_connect.types.contact_tag_map.serialize_json(value["tags"])
    if "connected_to_system_timestamp" in value:
        import capo_connect.types.timestamp

        out["ConnectedToSystemTimestamp"] = capo_connect.types.timestamp.serialize_json(
            value["connected_to_system_timestamp"]
        )
    if "routing_criteria" in value:
        import capo_connect.types.routing_criteria

        out["RoutingCriteria"] = capo_connect.types.routing_criteria.serialize_json(
            value["routing_criteria"]
        )
    if "customer" in value:
        import capo_connect.types.customer

        out["Customer"] = capo_connect.types.customer.serialize_json(value["customer"])
    if "campaign" in value:
        import capo_connect.types.campaign

        out["Campaign"] = capo_connect.types.campaign.serialize_json(value["campaign"])
    if "answering_machine_detection_status" in value:
        import capo_connect.types.answering_machine_detection_status

        out["AnsweringMachineDetectionStatus"] = (
            capo_connect.types.answering_machine_detection_status.serialize_json(
                value["answering_machine_detection_status"]
            )
        )
    if "customer_voice_activity" in value:
        import capo_connect.types.customer_voice_activity

        out["CustomerVoiceActivity"] = (
            capo_connect.types.customer_voice_activity.serialize_json(
                value["customer_voice_activity"]
            )
        )
    if "quality_metrics" in value:
        import capo_connect.types.quality_metrics

        out["QualityMetrics"] = capo_connect.types.quality_metrics.serialize_json(
            value["quality_metrics"]
        )
    if "chat_metrics" in value:
        import capo_connect.types.chat_metrics

        out["ChatMetrics"] = capo_connect.types.chat_metrics.serialize_json(
            value["chat_metrics"]
        )
    if "disconnect_details" in value:
        import capo_connect.types.disconnect_details

        out["DisconnectDetails"] = capo_connect.types.disconnect_details.serialize_json(
            value["disconnect_details"]
        )
    if "additional_email_recipients" in value:
        import capo_connect.types.additional_email_recipients

        out["AdditionalEmailRecipients"] = (
            capo_connect.types.additional_email_recipients.serialize_json(
                value["additional_email_recipients"]
            )
        )
    if "segment_attributes" in value:
        import capo_connect.types.segment_attributes

        out["SegmentAttributes"] = capo_connect.types.segment_attributes.serialize_json(
            value["segment_attributes"]
        )
    if "recordings" in value:
        import capo_connect.types.recordings

        out["Recordings"] = capo_connect.types.recordings.serialize_json(
            value["recordings"]
        )
    if "disconnect_reason" in value:
        out["DisconnectReason"] = value["disconnect_reason"]
    if "contact_evaluations" in value:
        import capo_connect.types.contact_evaluations

        out["ContactEvaluations"] = (
            capo_connect.types.contact_evaluations.serialize_json(
                value["contact_evaluations"]
            )
        )
    if "task_template_info" in value:
        import capo_connect.types.task_template_info_v2

        out["TaskTemplateInfo"] = (
            capo_connect.types.task_template_info_v2.serialize_json(
                value["task_template_info"]
            )
        )
    if "contact_details" in value:
        import capo_connect.types.contact_details

        out["ContactDetails"] = capo_connect.types.contact_details.serialize_json(
            value["contact_details"]
        )
    if "outbound_strategy" in value:
        import capo_connect.types.outbound_strategy

        out["OutboundStrategy"] = capo_connect.types.outbound_strategy.serialize_json(
            value["outbound_strategy"]
        )
    if "attributes" in value:
        import capo_connect.types.attributes

        out["Attributes"] = capo_connect.types.attributes.serialize_json(
            value["attributes"]
        )
    if "next_contacts" in value:
        import capo_connect.types.next_contacts

        out["NextContacts"] = capo_connect.types.next_contacts.serialize_json(
            value["next_contacts"]
        )
    if "global_resiliency_metadata" in value:
        import capo_connect.types.global_resiliency_metadata

        out["GlobalResiliencyMetadata"] = (
            capo_connect.types.global_resiliency_metadata.serialize_json(
                value["global_resiliency_metadata"]
            )
        )
    return out


def deserialize_json(data: dict) -> Contact:
    out: Contact = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Id" in data:
        out["id"] = data["Id"]
    if "InitialContactId" in data:
        out["initial_contact_id"] = data["InitialContactId"]
    if "PreviousContactId" in data:
        out["previous_contact_id"] = data["PreviousContactId"]
    if "ContactAssociationId" in data:
        out["contact_association_id"] = data["ContactAssociationId"]
    if "InitiationMethod" in data:
        import capo_connect.types.contact_initiation_method

        out["initiation_method"] = (
            capo_connect.types.contact_initiation_method.deserialize_json(
                data["InitiationMethod"]
            )
        )
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Channel" in data:
        import capo_connect.types.channel

        out["channel"] = capo_connect.types.channel.deserialize_json(data["Channel"])
    if "QueueInfo" in data:
        import capo_connect.types.queue_info

        out["queue_info"] = capo_connect.types.queue_info.deserialize_json(
            data["QueueInfo"]
        )
    if "AgentInfo" in data:
        import capo_connect.types.agent_info

        out["agent_info"] = capo_connect.types.agent_info.deserialize_json(
            data["AgentInfo"]
        )
    if "InitiationTimestamp" in data:
        import capo_connect.types.timestamp

        out["initiation_timestamp"] = capo_connect.types.timestamp.deserialize_json(
            data["InitiationTimestamp"]
        )
    if "DisconnectTimestamp" in data:
        import capo_connect.types.timestamp

        out["disconnect_timestamp"] = capo_connect.types.timestamp.deserialize_json(
            data["DisconnectTimestamp"]
        )
    if "LastUpdateTimestamp" in data:
        import capo_connect.types.timestamp

        out["last_update_timestamp"] = capo_connect.types.timestamp.deserialize_json(
            data["LastUpdateTimestamp"]
        )
    if "LastPausedTimestamp" in data:
        import capo_connect.types.timestamp

        out["last_paused_timestamp"] = capo_connect.types.timestamp.deserialize_json(
            data["LastPausedTimestamp"]
        )
    if "LastResumedTimestamp" in data:
        import capo_connect.types.timestamp

        out["last_resumed_timestamp"] = capo_connect.types.timestamp.deserialize_json(
            data["LastResumedTimestamp"]
        )
    if "RingStartTimestamp" in data:
        import capo_connect.types.timestamp

        out["ring_start_timestamp"] = capo_connect.types.timestamp.deserialize_json(
            data["RingStartTimestamp"]
        )
    if "TotalPauseCount" in data:
        out["total_pause_count"] = data["TotalPauseCount"]
    if "TotalPauseDurationInSeconds" in data:
        out["total_pause_duration_in_seconds"] = data["TotalPauseDurationInSeconds"]
    if "ScheduledTimestamp" in data:
        import capo_connect.types.timestamp

        out["scheduled_timestamp"] = capo_connect.types.timestamp.deserialize_json(
            data["ScheduledTimestamp"]
        )
    if "RelatedContactId" in data:
        out["related_contact_id"] = data["RelatedContactId"]
    if "WisdomInfo" in data:
        import capo_connect.types.wisdom_info

        out["wisdom_info"] = capo_connect.types.wisdom_info.deserialize_json(
            data["WisdomInfo"]
        )
    if "CustomerId" in data:
        out["customer_id"] = data["CustomerId"]
    if "CustomerEndpoint" in data:
        import capo_connect.types.endpoint_info

        out["customer_endpoint"] = capo_connect.types.endpoint_info.deserialize_json(
            data["CustomerEndpoint"]
        )
    if "SystemEndpoint" in data:
        import capo_connect.types.endpoint_info

        out["system_endpoint"] = capo_connect.types.endpoint_info.deserialize_json(
            data["SystemEndpoint"]
        )
    if "QueueTimeAdjustmentSeconds" in data:
        out["queue_time_adjustment_seconds"] = data["QueueTimeAdjustmentSeconds"]
    if "QueuePriority" in data:
        out["queue_priority"] = data["QueuePriority"]
    if "Tags" in data:
        import capo_connect.types.contact_tag_map

        out["tags"] = capo_connect.types.contact_tag_map.deserialize_json(data["Tags"])
    if "ConnectedToSystemTimestamp" in data:
        import capo_connect.types.timestamp

        out["connected_to_system_timestamp"] = (
            capo_connect.types.timestamp.deserialize_json(
                data["ConnectedToSystemTimestamp"]
            )
        )
    if "RoutingCriteria" in data:
        import capo_connect.types.routing_criteria

        out["routing_criteria"] = capo_connect.types.routing_criteria.deserialize_json(
            data["RoutingCriteria"]
        )
    if "Customer" in data:
        import capo_connect.types.customer

        out["customer"] = capo_connect.types.customer.deserialize_json(data["Customer"])
    if "Campaign" in data:
        import capo_connect.types.campaign

        out["campaign"] = capo_connect.types.campaign.deserialize_json(data["Campaign"])
    if "AnsweringMachineDetectionStatus" in data:
        import capo_connect.types.answering_machine_detection_status

        out["answering_machine_detection_status"] = (
            capo_connect.types.answering_machine_detection_status.deserialize_json(
                data["AnsweringMachineDetectionStatus"]
            )
        )
    if "CustomerVoiceActivity" in data:
        import capo_connect.types.customer_voice_activity

        out["customer_voice_activity"] = (
            capo_connect.types.customer_voice_activity.deserialize_json(
                data["CustomerVoiceActivity"]
            )
        )
    if "QualityMetrics" in data:
        import capo_connect.types.quality_metrics

        out["quality_metrics"] = capo_connect.types.quality_metrics.deserialize_json(
            data["QualityMetrics"]
        )
    if "ChatMetrics" in data:
        import capo_connect.types.chat_metrics

        out["chat_metrics"] = capo_connect.types.chat_metrics.deserialize_json(
            data["ChatMetrics"]
        )
    if "DisconnectDetails" in data:
        import capo_connect.types.disconnect_details

        out["disconnect_details"] = (
            capo_connect.types.disconnect_details.deserialize_json(
                data["DisconnectDetails"]
            )
        )
    if "AdditionalEmailRecipients" in data:
        import capo_connect.types.additional_email_recipients

        out["additional_email_recipients"] = (
            capo_connect.types.additional_email_recipients.deserialize_json(
                data["AdditionalEmailRecipients"]
            )
        )
    if "SegmentAttributes" in data:
        import capo_connect.types.segment_attributes

        out["segment_attributes"] = (
            capo_connect.types.segment_attributes.deserialize_json(
                data["SegmentAttributes"]
            )
        )
    if "Recordings" in data:
        import capo_connect.types.recordings

        out["recordings"] = capo_connect.types.recordings.deserialize_json(
            data["Recordings"]
        )
    if "DisconnectReason" in data:
        out["disconnect_reason"] = data["DisconnectReason"]
    if "ContactEvaluations" in data:
        import capo_connect.types.contact_evaluations

        out["contact_evaluations"] = (
            capo_connect.types.contact_evaluations.deserialize_json(
                data["ContactEvaluations"]
            )
        )
    if "TaskTemplateInfo" in data:
        import capo_connect.types.task_template_info_v2

        out["task_template_info"] = (
            capo_connect.types.task_template_info_v2.deserialize_json(
                data["TaskTemplateInfo"]
            )
        )
    if "ContactDetails" in data:
        import capo_connect.types.contact_details

        out["contact_details"] = capo_connect.types.contact_details.deserialize_json(
            data["ContactDetails"]
        )
    if "OutboundStrategy" in data:
        import capo_connect.types.outbound_strategy

        out["outbound_strategy"] = (
            capo_connect.types.outbound_strategy.deserialize_json(
                data["OutboundStrategy"]
            )
        )
    if "Attributes" in data:
        import capo_connect.types.attributes

        out["attributes"] = capo_connect.types.attributes.deserialize_json(
            data["Attributes"]
        )
    if "NextContacts" in data:
        import capo_connect.types.next_contacts

        out["next_contacts"] = capo_connect.types.next_contacts.deserialize_json(
            data["NextContacts"]
        )
    if "GlobalResiliencyMetadata" in data:
        import capo_connect.types.global_resiliency_metadata

        out["global_resiliency_metadata"] = (
            capo_connect.types.global_resiliency_metadata.deserialize_json(
                data["GlobalResiliencyMetadata"]
            )
        )
    return out
