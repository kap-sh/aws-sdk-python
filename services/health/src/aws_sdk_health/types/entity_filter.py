"""Generated from Smithy shape ``com.amazonaws.health#EntityFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_health.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_health.types.date_time_range_list
    import aws_sdk_health.types.entity_arn_list
    import aws_sdk_health.types.entity_status_code_list
    import aws_sdk_health.types.entity_value_list
    import aws_sdk_health.types.event_arn_list
    import aws_sdk_health.types.tag_filter


class EntityFilter(TypedDict, closed=True):
    event_arns: "aws_sdk_health.types.event_arn_list.eventArnList"
    r"""<p>A list of event ARNs (unique identifiers). For example: <code>\"arn:aws:health:us-east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-CDE456\", \"arn:aws:health:us-west-1::event/EBS/AWS_EBS_LOST_VOLUME/AWS_EBS_LOST_VOLUME_CHI789_JKL101\"</code> </p>"""
    entity_arns: NotRequired["aws_sdk_health.types.entity_arn_list.entityArnList"]
    """<p>A list of entity ARNs (unique identifiers).</p>"""
    entity_values: NotRequired["aws_sdk_health.types.entity_value_list.entityValueList"]
    """<p>A list of IDs for affected entities.</p>"""
    last_updated_times: NotRequired[
        "aws_sdk_health.types.date_time_range_list.dateTimeRangeList"
    ]
    """<p>A list of the most recent dates and times that the entity was updated.</p>"""
    tags: NotRequired["aws_sdk_health.types.tag_filter.tagFilter"]
    """<p>A map of entity tags attached to the affected entity.</p> <note> <p>Currently, the <code>tags</code> property isn't supported.</p> </note>"""
    status_codes: NotRequired[
        "aws_sdk_health.types.entity_status_code_list.entityStatusCodeList"
    ]
    """<p>A list of entity status codes (<code>IMPAIRED</code>, <code>UNIMPAIRED</code>, or <code>UNKNOWN</code>).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EntityFilter) -> dict:
    out: dict = {}
    import aws_sdk_health.types.event_arn_list

    out["eventArns"] = aws_sdk_health.types.event_arn_list.serialize_aws_json_1_1(
        value["event_arns"]
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
    if "last_updated_times" in value:
        import aws_sdk_health.types.date_time_range_list

        out["lastUpdatedTimes"] = (
            aws_sdk_health.types.date_time_range_list.serialize_aws_json_1_1(
                value["last_updated_times"]
            )
        )
    if "tags" in value:
        import aws_sdk_health.types.tag_filter

        out["tags"] = aws_sdk_health.types.tag_filter.serialize_aws_json_1_1(
            value["tags"]
        )
    if "status_codes" in value:
        import aws_sdk_health.types.entity_status_code_list

        out["statusCodes"] = (
            aws_sdk_health.types.entity_status_code_list.serialize_aws_json_1_1(
                value["status_codes"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EntityFilter:
    out: EntityFilter = {}  # type: ignore[typeddict-item]
    if "eventArns" in data:
        import aws_sdk_health.types.event_arn_list

        out["event_arns"] = (
            aws_sdk_health.types.event_arn_list.deserialize_aws_json_1_1(
                data["eventArns"]
            )
        )
    else:
        raise DeserializationError("EntityFilter.event_arns required")
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
    if "lastUpdatedTimes" in data:
        import aws_sdk_health.types.date_time_range_list

        out["last_updated_times"] = (
            aws_sdk_health.types.date_time_range_list.deserialize_aws_json_1_1(
                data["lastUpdatedTimes"]
            )
        )
    if "tags" in data:
        import aws_sdk_health.types.tag_filter

        out["tags"] = aws_sdk_health.types.tag_filter.deserialize_aws_json_1_1(
            data["tags"]
        )
    if "statusCodes" in data:
        import aws_sdk_health.types.entity_status_code_list

        out["status_codes"] = (
            aws_sdk_health.types.entity_status_code_list.deserialize_aws_json_1_1(
                data["statusCodes"]
            )
        )
    return out
