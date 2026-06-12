"""Generated from Smithy shape ``com.amazonaws.health#EventFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_health.types.availability_zones
    import aws_sdk_health.types.date_time_range_list
    import aws_sdk_health.types.entity_arn_list
    import aws_sdk_health.types.entity_value_list
    import aws_sdk_health.types.event_actionability_list
    import aws_sdk_health.types.event_arn_list
    import aws_sdk_health.types.event_persona_list
    import aws_sdk_health.types.event_status_code_list
    import aws_sdk_health.types.event_type_category_list2
    import aws_sdk_health.types.event_type_list2
    import aws_sdk_health.types.region_list
    import aws_sdk_health.types.service_list
    import aws_sdk_health.types.tag_filter


class EventFilter(TypedDict):
    actionabilities: NotRequired[
        "aws_sdk_health.types.event_actionability_list.EventActionabilityList"
    ]
    """<p>A list of actionability values to filter events. Use this to filter events based on whether they require action (<code>ACTION_REQUIRED</code>), may require action (<code>ACTION_MAY_BE_REQUIRED</code>) or are informational (<code>INFORMATIONAL</code>).</p>"""
    event_arns: NotRequired["aws_sdk_health.types.event_arn_list.eventArnList"]
    """<p>A list of event ARNs (unique identifiers). For example: <code>\"arn:aws:health:us-east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-CDE456\", \"arn:aws:health:us-west-1::event/EBS/AWS_EBS_LOST_VOLUME/AWS_EBS_LOST_VOLUME_CHI789_JKL101\"</code> </p>"""
    event_type_codes: NotRequired[
        "aws_sdk_health.types.event_type_list2.eventTypeList2"
    ]
    """<p>A list of unique identifiers for event types. For example, <code>\"AWS_EC2_SYSTEM_MAINTENANCE_EVENT\",\"AWS_RDS_MAINTENANCE_SCHEDULED\".</code> </p>"""
    services: NotRequired["aws_sdk_health.types.service_list.serviceList"]
    """<p>The Amazon Web Services services associated with the event. For example, <code>EC2</code>, <code>RDS</code>.</p>"""
    regions: NotRequired["aws_sdk_health.types.region_list.regionList"]
    """<p>A list of Amazon Web Services Regions.</p>"""
    availability_zones: NotRequired[
        "aws_sdk_health.types.availability_zones.availabilityZones"
    ]
    """<p>A list of Amazon Web Services Availability Zones.</p>"""
    start_times: NotRequired[
        "aws_sdk_health.types.date_time_range_list.dateTimeRangeList"
    ]
    """<p>A list of dates and times that the event began.</p>"""
    end_times: NotRequired[
        "aws_sdk_health.types.date_time_range_list.dateTimeRangeList"
    ]
    """<p>A list of dates and times that the event ended.</p>"""
    last_updated_times: NotRequired[
        "aws_sdk_health.types.date_time_range_list.dateTimeRangeList"
    ]
    """<p>A list of dates and times that the event was last updated.</p>"""
    entity_arns: NotRequired["aws_sdk_health.types.entity_arn_list.entityArnList"]
    """<p>A list of entity ARNs (unique identifiers).</p>"""
    entity_values: NotRequired["aws_sdk_health.types.entity_value_list.entityValueList"]
    """<p>A list of entity identifiers, such as EC2 instance IDs (<code>i-34ab692e</code>) or EBS volumes (<code>vol-426ab23e</code>).</p>"""
    event_type_categories: NotRequired[
        "aws_sdk_health.types.event_type_category_list2.eventTypeCategoryList2"
    ]
    """<p>A list of event type category codes. Possible values are <code>issue</code>, <code>accountNotification</code>, or <code>scheduledChange</code>. Currently, the <code>investigation</code> value isn't supported at this time.</p>"""
    tags: NotRequired["aws_sdk_health.types.tag_filter.tagFilter"]
    """<p>A map of entity tags attached to the affected entity.</p> <note> <p>Currently, the <code>tags</code> property isn't supported.</p> </note>"""
    event_status_codes: NotRequired[
        "aws_sdk_health.types.event_status_code_list.eventStatusCodeList"
    ]
    """<p>A list of event status codes.</p>"""
    personas: NotRequired["aws_sdk_health.types.event_persona_list.EventPersonaList"]
    """<p>A list of persona values to filter events. Use this to filter events based on their target audience: <code>OPERATIONS</code>, <code>SECURITY</code>, or <code>BILLING</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EventFilter) -> dict:
    out: dict = {}
    if "actionabilities" in value:
        import aws_sdk_health.types.event_actionability_list

        out["actionabilities"] = (
            aws_sdk_health.types.event_actionability_list.serialize_aws_json_1_1(
                value["actionabilities"]
            )
        )
    if "event_arns" in value:
        import aws_sdk_health.types.event_arn_list

        out["eventArns"] = aws_sdk_health.types.event_arn_list.serialize_aws_json_1_1(
            value["event_arns"]
        )
    if "event_type_codes" in value:
        import aws_sdk_health.types.event_type_list2

        out["eventTypeCodes"] = (
            aws_sdk_health.types.event_type_list2.serialize_aws_json_1_1(
                value["event_type_codes"]
            )
        )
    if "services" in value:
        import aws_sdk_health.types.service_list

        out["services"] = aws_sdk_health.types.service_list.serialize_aws_json_1_1(
            value["services"]
        )
    if "regions" in value:
        import aws_sdk_health.types.region_list

        out["regions"] = aws_sdk_health.types.region_list.serialize_aws_json_1_1(
            value["regions"]
        )
    if "availability_zones" in value:
        import aws_sdk_health.types.availability_zones

        out["availabilityZones"] = (
            aws_sdk_health.types.availability_zones.serialize_aws_json_1_1(
                value["availability_zones"]
            )
        )
    if "start_times" in value:
        import aws_sdk_health.types.date_time_range_list

        out["startTimes"] = (
            aws_sdk_health.types.date_time_range_list.serialize_aws_json_1_1(
                value["start_times"]
            )
        )
    if "end_times" in value:
        import aws_sdk_health.types.date_time_range_list

        out["endTimes"] = (
            aws_sdk_health.types.date_time_range_list.serialize_aws_json_1_1(
                value["end_times"]
            )
        )
    if "last_updated_times" in value:
        import aws_sdk_health.types.date_time_range_list

        out["lastUpdatedTimes"] = (
            aws_sdk_health.types.date_time_range_list.serialize_aws_json_1_1(
                value["last_updated_times"]
            )
        )
    if "entity_arns" in value:
        import aws_sdk_health.types.entity_arn_list

        out["entityArns"] = aws_sdk_health.types.entity_arn_list.serialize_aws_json_1_1(
            value["entity_arns"]
        )
    if "entity_values" in value:
        import aws_sdk_health.types.entity_value_list

        out["entityValues"] = (
            aws_sdk_health.types.entity_value_list.serialize_aws_json_1_1(
                value["entity_values"]
            )
        )
    if "event_type_categories" in value:
        import aws_sdk_health.types.event_type_category_list2

        out["eventTypeCategories"] = (
            aws_sdk_health.types.event_type_category_list2.serialize_aws_json_1_1(
                value["event_type_categories"]
            )
        )
    if "tags" in value:
        import aws_sdk_health.types.tag_filter

        out["tags"] = aws_sdk_health.types.tag_filter.serialize_aws_json_1_1(
            value["tags"]
        )
    if "event_status_codes" in value:
        import aws_sdk_health.types.event_status_code_list

        out["eventStatusCodes"] = (
            aws_sdk_health.types.event_status_code_list.serialize_aws_json_1_1(
                value["event_status_codes"]
            )
        )
    if "personas" in value:
        import aws_sdk_health.types.event_persona_list

        out["personas"] = (
            aws_sdk_health.types.event_persona_list.serialize_aws_json_1_1(
                value["personas"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EventFilter:
    out: EventFilter = {}  # type: ignore[typeddict-item]
    if "actionabilities" in data:
        import aws_sdk_health.types.event_actionability_list

        out["actionabilities"] = (
            aws_sdk_health.types.event_actionability_list.deserialize_aws_json_1_1(
                data["actionabilities"]
            )
        )
    if "eventArns" in data:
        import aws_sdk_health.types.event_arn_list

        out["event_arns"] = (
            aws_sdk_health.types.event_arn_list.deserialize_aws_json_1_1(
                data["eventArns"]
            )
        )
    if "eventTypeCodes" in data:
        import aws_sdk_health.types.event_type_list2

        out["event_type_codes"] = (
            aws_sdk_health.types.event_type_list2.deserialize_aws_json_1_1(
                data["eventTypeCodes"]
            )
        )
    if "services" in data:
        import aws_sdk_health.types.service_list

        out["services"] = aws_sdk_health.types.service_list.deserialize_aws_json_1_1(
            data["services"]
        )
    if "regions" in data:
        import aws_sdk_health.types.region_list

        out["regions"] = aws_sdk_health.types.region_list.deserialize_aws_json_1_1(
            data["regions"]
        )
    if "availabilityZones" in data:
        import aws_sdk_health.types.availability_zones

        out["availability_zones"] = (
            aws_sdk_health.types.availability_zones.deserialize_aws_json_1_1(
                data["availabilityZones"]
            )
        )
    if "startTimes" in data:
        import aws_sdk_health.types.date_time_range_list

        out["start_times"] = (
            aws_sdk_health.types.date_time_range_list.deserialize_aws_json_1_1(
                data["startTimes"]
            )
        )
    if "endTimes" in data:
        import aws_sdk_health.types.date_time_range_list

        out["end_times"] = (
            aws_sdk_health.types.date_time_range_list.deserialize_aws_json_1_1(
                data["endTimes"]
            )
        )
    if "lastUpdatedTimes" in data:
        import aws_sdk_health.types.date_time_range_list

        out["last_updated_times"] = (
            aws_sdk_health.types.date_time_range_list.deserialize_aws_json_1_1(
                data["lastUpdatedTimes"]
            )
        )
    if "entityArns" in data:
        import aws_sdk_health.types.entity_arn_list

        out["entity_arns"] = (
            aws_sdk_health.types.entity_arn_list.deserialize_aws_json_1_1(
                data["entityArns"]
            )
        )
    if "entityValues" in data:
        import aws_sdk_health.types.entity_value_list

        out["entity_values"] = (
            aws_sdk_health.types.entity_value_list.deserialize_aws_json_1_1(
                data["entityValues"]
            )
        )
    if "eventTypeCategories" in data:
        import aws_sdk_health.types.event_type_category_list2

        out["event_type_categories"] = (
            aws_sdk_health.types.event_type_category_list2.deserialize_aws_json_1_1(
                data["eventTypeCategories"]
            )
        )
    if "tags" in data:
        import aws_sdk_health.types.tag_filter

        out["tags"] = aws_sdk_health.types.tag_filter.deserialize_aws_json_1_1(
            data["tags"]
        )
    if "eventStatusCodes" in data:
        import aws_sdk_health.types.event_status_code_list

        out["event_status_codes"] = (
            aws_sdk_health.types.event_status_code_list.deserialize_aws_json_1_1(
                data["eventStatusCodes"]
            )
        )
    if "personas" in data:
        import aws_sdk_health.types.event_persona_list

        out["personas"] = (
            aws_sdk_health.types.event_persona_list.deserialize_aws_json_1_1(
                data["personas"]
            )
        )
    return out
