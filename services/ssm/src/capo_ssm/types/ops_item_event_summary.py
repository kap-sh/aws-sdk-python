"""Generated from Smithy shape ``com.amazonaws.ssm#OpsItemEventSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.date_time
    import capo_ssm.types.ops_item_identity
    import capo_ssm.types.string


class OpsItemEventSummary(TypedDict, closed=True):
    ops_item_id: NotRequired["capo_ssm.types.string.String"]
    """<p>The ID of the OpsItem.</p>"""
    event_id: NotRequired["capo_ssm.types.string.String"]
    """<p>The ID of the OpsItem event.</p>"""
    source: NotRequired["capo_ssm.types.string.String"]
    """<p>The source of the OpsItem event.</p>"""
    detail_type: NotRequired["capo_ssm.types.string.String"]
    """<p>The type of information provided as a detail.</p>"""
    detail: NotRequired["capo_ssm.types.string.String"]
    """<p>Specific information about the OpsItem event.</p>"""
    created_by: NotRequired["capo_ssm.types.ops_item_identity.OpsItemIdentity"]
    """<p>Information about the user or resource that created the OpsItem event.</p>"""
    created_time: NotRequired["capo_ssm.types.date_time.DateTime"]
    """<p>The date and time the OpsItem event was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpsItemEventSummary) -> dict:
    out: dict = {}
    if "ops_item_id" in value:
        out["OpsItemId"] = value["ops_item_id"]
    if "event_id" in value:
        out["EventId"] = value["event_id"]
    if "source" in value:
        out["Source"] = value["source"]
    if "detail_type" in value:
        out["DetailType"] = value["detail_type"]
    if "detail" in value:
        out["Detail"] = value["detail"]
    if "created_by" in value:
        import capo_ssm.types.ops_item_identity

        out["CreatedBy"] = capo_ssm.types.ops_item_identity.serialize_aws_json_1_1(
            value["created_by"]
        )
    if "created_time" in value:
        import capo_ssm.types.date_time

        out["CreatedTime"] = capo_ssm.types.date_time.serialize_aws_json_1_1(
            value["created_time"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> OpsItemEventSummary:
    out: OpsItemEventSummary = {}  # type: ignore[typeddict-item]
    if "OpsItemId" in data:
        out["ops_item_id"] = data["OpsItemId"]
    if "EventId" in data:
        out["event_id"] = data["EventId"]
    if "Source" in data:
        out["source"] = data["Source"]
    if "DetailType" in data:
        out["detail_type"] = data["DetailType"]
    if "Detail" in data:
        out["detail"] = data["Detail"]
    if "CreatedBy" in data:
        import capo_ssm.types.ops_item_identity

        out["created_by"] = capo_ssm.types.ops_item_identity.deserialize_aws_json_1_1(
            data["CreatedBy"]
        )
    if "CreatedTime" in data:
        import capo_ssm.types.date_time

        out["created_time"] = capo_ssm.types.date_time.deserialize_aws_json_1_1(
            data["CreatedTime"]
        )
    return out
