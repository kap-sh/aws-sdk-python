"""Generated from Smithy shape ``com.amazonaws.health#AffectedEntity``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_health.types.account_id
    import aws_sdk_health.types.entity_arn
    import aws_sdk_health.types.entity_metadata
    import aws_sdk_health.types.entity_status_code
    import aws_sdk_health.types.entity_url
    import aws_sdk_health.types.entity_value
    import aws_sdk_health.types.event_arn
    import aws_sdk_health.types.tag_set
    import aws_sdk_health.types.timestamp


class AffectedEntity(TypedDict):
    entity_arn: NotRequired["aws_sdk_health.types.entity_arn.entityArn"]
    """<p>The unique identifier for the entity. Format: <code>arn:aws:health:<i>entity-region</i>:<i>aws-account</i>:entity/<i>entity-id</i> </code>. Example: <code>arn:aws:health:us-east-1:111222333444:entity/AVh5GGT7ul1arKr1sE1K</code> </p>"""
    event_arn: NotRequired["aws_sdk_health.types.event_arn.eventArn"]
    """<p>The unique identifier for the event. The event ARN has the <code>arn:aws:health:<i>event-region</i>::event/<i>SERVICE</i>/<i>EVENT_TYPE_CODE</i>/<i>EVENT_TYPE_PLUS_ID</i> </code> format.</p> <p>For example, an event ARN might look like the following:</p> <p> <code>arn:aws:health:us-east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-DEF456</code> </p>"""
    entity_value: NotRequired["aws_sdk_health.types.entity_value.entityValue"]
    """<p>The ID of the affected entity.</p>"""
    entity_url: NotRequired["aws_sdk_health.types.entity_url.entityUrl"]
    """<p>The URL of the affected entity.</p>"""
    aws_account_id: NotRequired["aws_sdk_health.types.account_id.accountId"]
    """<p>The 12-digit Amazon Web Services account number that contains the affected entity.</p>"""
    last_updated_time: NotRequired["aws_sdk_health.types.timestamp.timestamp"]
    """<p>The most recent time that the entity was updated.</p>"""
    status_code: NotRequired["aws_sdk_health.types.entity_status_code.entityStatusCode"]
    """<p>The most recent status of the entity affected by the event. The possible values are <code>IMPAIRED</code>, <code>UNIMPAIRED</code>, <code>UNKNOWN</code>, <code>PENDING</code>, and <code>RESOLVED</code>.</p>"""
    tags: NotRequired["aws_sdk_health.types.tag_set.tagSet"]
    """<p>A map of entity tags attached to the affected entity.</p> <note> <p>Currently, the <code>tags</code> property isn't supported.</p> </note>"""
    entity_metadata: NotRequired["aws_sdk_health.types.entity_metadata.entityMetadata"]
    """<p>Additional metadata about the affected entity.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AffectedEntity) -> dict:
    out: dict = {}
    if "entity_arn" in value:
        out["entityArn"] = value["entity_arn"]
    if "event_arn" in value:
        out["eventArn"] = value["event_arn"]
    if "entity_value" in value:
        out["entityValue"] = value["entity_value"]
    if "entity_url" in value:
        out["entityUrl"] = value["entity_url"]
    if "aws_account_id" in value:
        out["awsAccountId"] = value["aws_account_id"]
    if "last_updated_time" in value:
        import aws_sdk_health.types.timestamp

        out["lastUpdatedTime"] = aws_sdk_health.types.timestamp.serialize_aws_json_1_1(
            value["last_updated_time"]
        )
    if "status_code" in value:
        import aws_sdk_health.types.entity_status_code

        out["statusCode"] = (
            aws_sdk_health.types.entity_status_code.serialize_aws_json_1_1(
                value["status_code"]
            )
        )
    if "tags" in value:
        import aws_sdk_health.types.tag_set

        out["tags"] = aws_sdk_health.types.tag_set.serialize_aws_json_1_1(value["tags"])
    if "entity_metadata" in value:
        import aws_sdk_health.types.entity_metadata

        out["entityMetadata"] = (
            aws_sdk_health.types.entity_metadata.serialize_aws_json_1_1(
                value["entity_metadata"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AffectedEntity:
    out: AffectedEntity = {}  # type: ignore[typeddict-item]
    if "entityArn" in data:
        out["entity_arn"] = data["entityArn"]
    if "eventArn" in data:
        out["event_arn"] = data["eventArn"]
    if "entityValue" in data:
        out["entity_value"] = data["entityValue"]
    if "entityUrl" in data:
        out["entity_url"] = data["entityUrl"]
    if "awsAccountId" in data:
        out["aws_account_id"] = data["awsAccountId"]
    if "lastUpdatedTime" in data:
        import aws_sdk_health.types.timestamp

        out["last_updated_time"] = (
            aws_sdk_health.types.timestamp.deserialize_aws_json_1_1(
                data["lastUpdatedTime"]
            )
        )
    if "statusCode" in data:
        import aws_sdk_health.types.entity_status_code

        out["status_code"] = (
            aws_sdk_health.types.entity_status_code.deserialize_aws_json_1_1(
                data["statusCode"]
            )
        )
    if "tags" in data:
        import aws_sdk_health.types.tag_set

        out["tags"] = aws_sdk_health.types.tag_set.deserialize_aws_json_1_1(
            data["tags"]
        )
    if "entityMetadata" in data:
        import aws_sdk_health.types.entity_metadata

        out["entity_metadata"] = (
            aws_sdk_health.types.entity_metadata.deserialize_aws_json_1_1(
                data["entityMetadata"]
            )
        )
    return out
