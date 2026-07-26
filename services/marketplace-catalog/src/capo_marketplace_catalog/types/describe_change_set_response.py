"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#DescribeChangeSetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.arn
    import capo_marketplace_catalog.types.change_set_description
    import capo_marketplace_catalog.types.change_set_name
    import capo_marketplace_catalog.types.change_status
    import capo_marketplace_catalog.types.date_time_iso8601
    import capo_marketplace_catalog.types.exception_message_content
    import capo_marketplace_catalog.types.failure_code
    import capo_marketplace_catalog.types.intent
    import capo_marketplace_catalog.types.resource_id


class DescribeChangeSetResponse(TypedDict, closed=True):
    change_set_id: NotRequired["capo_marketplace_catalog.types.resource_id.ResourceId"]
    """<p>Required. The unique identifier for the change set referenced in this request.</p>"""
    change_set_arn: NotRequired["capo_marketplace_catalog.types.arn.ARN"]
    """<p>The ARN associated with the unique identifier for the change set referenced in this request.</p>"""
    change_set_name: NotRequired[
        "capo_marketplace_catalog.types.change_set_name.ChangeSetName"
    ]
    """<p>The optional name provided in the <code>StartChangeSet</code> request. If you do not provide a name, one is set by default.</p>"""
    intent: NotRequired["capo_marketplace_catalog.types.intent.Intent"]
    """<p>The optional intent provided in the <code>StartChangeSet</code> request. If you do not provide an intent, <code>APPLY</code> is set by default.</p>"""
    start_time: NotRequired[
        "capo_marketplace_catalog.types.date_time_iso8601.DateTimeISO8601"
    ]
    """<p>The date and time, in ISO 8601 format (2018-02-27T13:45:22Z), the request started. </p>"""
    end_time: NotRequired[
        "capo_marketplace_catalog.types.date_time_iso8601.DateTimeISO8601"
    ]
    """<p>The date and time, in ISO 8601 format (2018-02-27T13:45:22Z), the request transitioned to a terminal state. The change cannot transition to a different state. Null if the request is not in a terminal state. </p>"""
    status: NotRequired["capo_marketplace_catalog.types.change_status.ChangeStatus"]
    """<p>The status of the change request.</p>"""
    failure_code: NotRequired["capo_marketplace_catalog.types.failure_code.FailureCode"]
    """<p>Returned if the change set is in <code>FAILED</code> status. Can be either <code>CLIENT_ERROR</code>, which means that there are issues with the request (see the <code>ErrorDetailList</code>), or <code>SERVER_FAULT</code>, which means that there is a problem in the system, and you should retry your request.</p>"""
    failure_description: NotRequired[
        "capo_marketplace_catalog.types.exception_message_content.ExceptionMessageContent"
    ]
    """<p>Returned if there is a failure on the change set, but that failure is not related to any of the changes in the request.</p>"""
    change_set: NotRequired[
        "capo_marketplace_catalog.types.change_set_description.ChangeSetDescription"
    ]
    """<p>An array of <code>ChangeSummary</code> objects.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeChangeSetResponse) -> dict:
    out: dict = {}
    if "change_set_id" in value:
        out["ChangeSetId"] = value["change_set_id"]
    if "change_set_arn" in value:
        out["ChangeSetArn"] = value["change_set_arn"]
    if "change_set_name" in value:
        out["ChangeSetName"] = value["change_set_name"]
    if "intent" in value:
        import capo_marketplace_catalog.types.intent

        out["Intent"] = capo_marketplace_catalog.types.intent.serialize_json(
            value["intent"]
        )
    if "start_time" in value:
        out["StartTime"] = value["start_time"]
    if "end_time" in value:
        out["EndTime"] = value["end_time"]
    if "status" in value:
        import capo_marketplace_catalog.types.change_status

        out["Status"] = capo_marketplace_catalog.types.change_status.serialize_json(
            value["status"]
        )
    if "failure_code" in value:
        import capo_marketplace_catalog.types.failure_code

        out["FailureCode"] = capo_marketplace_catalog.types.failure_code.serialize_json(
            value["failure_code"]
        )
    if "failure_description" in value:
        out["FailureDescription"] = value["failure_description"]
    if "change_set" in value:
        import capo_marketplace_catalog.types.change_set_description

        out["ChangeSet"] = (
            capo_marketplace_catalog.types.change_set_description.serialize_json(
                value["change_set"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeChangeSetResponse:
    out: DescribeChangeSetResponse = {}  # type: ignore[typeddict-item]
    if "ChangeSetId" in data:
        out["change_set_id"] = data["ChangeSetId"]
    if "ChangeSetArn" in data:
        out["change_set_arn"] = data["ChangeSetArn"]
    if "ChangeSetName" in data:
        out["change_set_name"] = data["ChangeSetName"]
    if "Intent" in data:
        import capo_marketplace_catalog.types.intent

        out["intent"] = capo_marketplace_catalog.types.intent.deserialize_json(
            data["Intent"]
        )
    if "StartTime" in data:
        out["start_time"] = data["StartTime"]
    if "EndTime" in data:
        out["end_time"] = data["EndTime"]
    if "Status" in data:
        import capo_marketplace_catalog.types.change_status

        out["status"] = capo_marketplace_catalog.types.change_status.deserialize_json(
            data["Status"]
        )
    if "FailureCode" in data:
        import capo_marketplace_catalog.types.failure_code

        out["failure_code"] = (
            capo_marketplace_catalog.types.failure_code.deserialize_json(
                data["FailureCode"]
            )
        )
    if "FailureDescription" in data:
        out["failure_description"] = data["FailureDescription"]
    if "ChangeSet" in data:
        import capo_marketplace_catalog.types.change_set_description

        out["change_set"] = (
            capo_marketplace_catalog.types.change_set_description.deserialize_json(
                data["ChangeSet"]
            )
        )
    return out
