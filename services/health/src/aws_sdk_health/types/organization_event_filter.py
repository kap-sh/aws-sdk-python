"""Generated from Smithy shape ``com.amazonaws.health#OrganizationEventFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_health.types.aws_account_ids_list
    import aws_sdk_health.types.date_time_range
    import aws_sdk_health.types.entity_arn_list
    import aws_sdk_health.types.entity_value_list
    import aws_sdk_health.types.event_actionability_list
    import aws_sdk_health.types.event_persona_list
    import aws_sdk_health.types.event_status_code_list
    import aws_sdk_health.types.event_type_category_list2
    import aws_sdk_health.types.event_type_list2
    import aws_sdk_health.types.region_list
    import aws_sdk_health.types.service_list


class OrganizationEventFilter(TypedDict):
    actionabilities: NotRequired[
        "aws_sdk_health.types.event_actionability_list.EventActionabilityList"
    ]
    """<p>A list of actionability values to filter events. Use this to filter events based on whether they require action (<code>ACTION_REQUIRED</code>), may require action (<code>ACTION_MAY_BE_REQUIRED</code>) or are informational (<code>INFORMATIONAL</code>).</p>"""
    event_type_codes: NotRequired[
        "aws_sdk_health.types.event_type_list2.eventTypeList2"
    ]
    """<p>A list of unique identifiers for event types. For example, <code>\"AWS_EC2_SYSTEM_MAINTENANCE_EVENT\",\"AWS_RDS_MAINTENANCE_SCHEDULED\".</code> </p>"""
    aws_account_ids: NotRequired[
        "aws_sdk_health.types.aws_account_ids_list.awsAccountIdsList"
    ]
    """<p>A list of 12-digit Amazon Web Services account numbers that contains the affected entities.</p>"""
    services: NotRequired["aws_sdk_health.types.service_list.serviceList"]
    """<p>The Amazon Web Services services associated with the event. For example, <code>EC2</code>, <code>RDS</code>.</p>"""
    regions: NotRequired["aws_sdk_health.types.region_list.regionList"]
    """<p>A list of Amazon Web Services Regions.</p>"""
    start_time: NotRequired["aws_sdk_health.types.date_time_range.DateTimeRange"]
    end_time: NotRequired["aws_sdk_health.types.date_time_range.DateTimeRange"]
    last_updated_time: NotRequired["aws_sdk_health.types.date_time_range.DateTimeRange"]
    entity_arns: NotRequired["aws_sdk_health.types.entity_arn_list.entityArnList"]
    """<p>A list of entity ARNs (unique identifiers).</p>"""
    entity_values: NotRequired["aws_sdk_health.types.entity_value_list.entityValueList"]
    """<p>A list of entity identifiers, such as EC2 instance IDs (i-34ab692e) or EBS volumes (vol-426ab23e).</p>"""
    event_type_categories: NotRequired[
        "aws_sdk_health.types.event_type_category_list2.eventTypeCategoryList2"
    ]
    """<p>A list of event type category codes. Possible values are <code>issue</code>, <code>accountNotification</code>, or <code>scheduledChange</code>. Currently, the <code>investigation</code> value isn't supported at this time.</p>"""
    event_status_codes: NotRequired[
        "aws_sdk_health.types.event_status_code_list.eventStatusCodeList"
    ]
    """<p>A list of event status codes.</p>"""
    personas: NotRequired["aws_sdk_health.types.event_persona_list.EventPersonaList"]
    """<p>A list of persona values to filter events. Use this to filter events based on their target audience: <code>OPERATIONS</code>, <code>SECURITY</code>, or <code>BILLING</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OrganizationEventFilter) -> dict:
    out: dict = {}
    if "actionabilities" in value:
        import aws_sdk_health.types.event_actionability_list

        out["actionabilities"] = (
            aws_sdk_health.types.event_actionability_list.serialize_aws_json_1_1(
                value["actionabilities"]
            )
        )
    if "event_type_codes" in value:
        import aws_sdk_health.types.event_type_list2

        out["eventTypeCodes"] = (
            aws_sdk_health.types.event_type_list2.serialize_aws_json_1_1(
                value["event_type_codes"]
            )
        )
    if "aws_account_ids" in value:
        import aws_sdk_health.types.aws_account_ids_list

        out["awsAccountIds"] = (
            aws_sdk_health.types.aws_account_ids_list.serialize_aws_json_1_1(
                value["aws_account_ids"]
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
    if "start_time" in value:
        import aws_sdk_health.types.date_time_range

        out["startTime"] = aws_sdk_health.types.date_time_range.serialize_aws_json_1_1(
            value["start_time"]
        )
    if "end_time" in value:
        import aws_sdk_health.types.date_time_range

        out["endTime"] = aws_sdk_health.types.date_time_range.serialize_aws_json_1_1(
            value["end_time"]
        )
    if "last_updated_time" in value:
        import aws_sdk_health.types.date_time_range

        out["lastUpdatedTime"] = (
            aws_sdk_health.types.date_time_range.serialize_aws_json_1_1(
                value["last_updated_time"]
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


def deserialize_aws_json_1_1(data: dict) -> OrganizationEventFilter:
    out: OrganizationEventFilter = {}  # type: ignore[typeddict-item]
    if "actionabilities" in data:
        import aws_sdk_health.types.event_actionability_list

        out["actionabilities"] = (
            aws_sdk_health.types.event_actionability_list.deserialize_aws_json_1_1(
                data["actionabilities"]
            )
        )
    if "eventTypeCodes" in data:
        import aws_sdk_health.types.event_type_list2

        out["event_type_codes"] = (
            aws_sdk_health.types.event_type_list2.deserialize_aws_json_1_1(
                data["eventTypeCodes"]
            )
        )
    if "awsAccountIds" in data:
        import aws_sdk_health.types.aws_account_ids_list

        out["aws_account_ids"] = (
            aws_sdk_health.types.aws_account_ids_list.deserialize_aws_json_1_1(
                data["awsAccountIds"]
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
    if "startTime" in data:
        import aws_sdk_health.types.date_time_range

        out["start_time"] = (
            aws_sdk_health.types.date_time_range.deserialize_aws_json_1_1(
                data["startTime"]
            )
        )
    if "endTime" in data:
        import aws_sdk_health.types.date_time_range

        out["end_time"] = aws_sdk_health.types.date_time_range.deserialize_aws_json_1_1(
            data["endTime"]
        )
    if "lastUpdatedTime" in data:
        import aws_sdk_health.types.date_time_range

        out["last_updated_time"] = (
            aws_sdk_health.types.date_time_range.deserialize_aws_json_1_1(
                data["lastUpdatedTime"]
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
