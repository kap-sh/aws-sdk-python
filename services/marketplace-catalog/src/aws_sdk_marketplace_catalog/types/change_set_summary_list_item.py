"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#ChangeSetSummaryListItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_marketplace_catalog.types.arn
    import aws_sdk_marketplace_catalog.types.change_set_name
    import aws_sdk_marketplace_catalog.types.change_status
    import aws_sdk_marketplace_catalog.types.date_time_iso8601
    import aws_sdk_marketplace_catalog.types.failure_code
    import aws_sdk_marketplace_catalog.types.resource_id
    import aws_sdk_marketplace_catalog.types.resource_id_list


class ChangeSetSummaryListItem(TypedDict, closed=True):
    change_set_id: NotRequired[
        "aws_sdk_marketplace_catalog.types.resource_id.ResourceId"
    ]
    """<p>The unique identifier for a change set.</p>"""
    change_set_arn: NotRequired["aws_sdk_marketplace_catalog.types.arn.ARN"]
    """<p>The ARN associated with the unique identifier for the change set referenced in this request.</p>"""
    change_set_name: NotRequired[
        "aws_sdk_marketplace_catalog.types.change_set_name.ChangeSetName"
    ]
    """<p>The non-unique name for the change set.</p>"""
    start_time: NotRequired[
        "aws_sdk_marketplace_catalog.types.date_time_iso8601.DateTimeISO8601"
    ]
    """<p>The time, in ISO 8601 format (2018-02-27T13:45:22Z), when the change set was started.</p>"""
    end_time: NotRequired[
        "aws_sdk_marketplace_catalog.types.date_time_iso8601.DateTimeISO8601"
    ]
    """<p>The time, in ISO 8601 format (2018-02-27T13:45:22Z), when the change set was finished.</p>"""
    status: NotRequired["aws_sdk_marketplace_catalog.types.change_status.ChangeStatus"]
    """<p>The current status of the change set.</p>"""
    entity_id_list: NotRequired[
        "aws_sdk_marketplace_catalog.types.resource_id_list.ResourceIdList"
    ]
    """<p>This object is a list of entity IDs (string) that are a part of a change set. The entity ID list is a maximum of 20 entities. It must contain at least one entity.</p>"""
    failure_code: NotRequired[
        "aws_sdk_marketplace_catalog.types.failure_code.FailureCode"
    ]
    """<p>Returned if the change set is in <code>FAILED</code> status. Can be either <code>CLIENT_ERROR</code>, which means that there are issues with the request (see the <code>ErrorDetailList</code> of <code>DescribeChangeSet</code>), or <code>SERVER_FAULT</code>, which means that there is a problem in the system, and you should retry your request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChangeSetSummaryListItem) -> dict:
    out: dict = {}
    if "change_set_id" in value:
        out["ChangeSetId"] = value["change_set_id"]
    if "change_set_arn" in value:
        out["ChangeSetArn"] = value["change_set_arn"]
    if "change_set_name" in value:
        out["ChangeSetName"] = value["change_set_name"]
    if "start_time" in value:
        out["StartTime"] = value["start_time"]
    if "end_time" in value:
        out["EndTime"] = value["end_time"]
    if "status" in value:
        import aws_sdk_marketplace_catalog.types.change_status

        out["Status"] = aws_sdk_marketplace_catalog.types.change_status.serialize_json(
            value["status"]
        )
    if "entity_id_list" in value:
        import aws_sdk_marketplace_catalog.types.resource_id_list

        out["EntityIdList"] = (
            aws_sdk_marketplace_catalog.types.resource_id_list.serialize_json(
                value["entity_id_list"]
            )
        )
    if "failure_code" in value:
        import aws_sdk_marketplace_catalog.types.failure_code

        out["FailureCode"] = (
            aws_sdk_marketplace_catalog.types.failure_code.serialize_json(
                value["failure_code"]
            )
        )
    return out


def deserialize_json(data: dict) -> ChangeSetSummaryListItem:
    out: ChangeSetSummaryListItem = {}  # type: ignore[typeddict-item]
    if "ChangeSetId" in data:
        out["change_set_id"] = data["ChangeSetId"]
    if "ChangeSetArn" in data:
        out["change_set_arn"] = data["ChangeSetArn"]
    if "ChangeSetName" in data:
        out["change_set_name"] = data["ChangeSetName"]
    if "StartTime" in data:
        out["start_time"] = data["StartTime"]
    if "EndTime" in data:
        out["end_time"] = data["EndTime"]
    if "Status" in data:
        import aws_sdk_marketplace_catalog.types.change_status

        out["status"] = (
            aws_sdk_marketplace_catalog.types.change_status.deserialize_json(
                data["Status"]
            )
        )
    if "EntityIdList" in data:
        import aws_sdk_marketplace_catalog.types.resource_id_list

        out["entity_id_list"] = (
            aws_sdk_marketplace_catalog.types.resource_id_list.deserialize_json(
                data["EntityIdList"]
            )
        )
    if "FailureCode" in data:
        import aws_sdk_marketplace_catalog.types.failure_code

        out["failure_code"] = (
            aws_sdk_marketplace_catalog.types.failure_code.deserialize_json(
                data["FailureCode"]
            )
        )
    return out
