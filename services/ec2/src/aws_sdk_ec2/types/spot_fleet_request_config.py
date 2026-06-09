"""Generated from Smithy shape ``com.amazonaws.ec2#SpotFleetRequestConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.activity_status
    import aws_sdk_ec2.types.batch_state
    import aws_sdk_ec2.types.millisecond_date_time
    import aws_sdk_ec2.types.spot_fleet_request_config_data
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list


class SpotFleetRequestConfig(TypedDict):
    activity_status: NotRequired["aws_sdk_ec2.types.activity_status.ActivityStatus"]
    """<p>The progress of the Spot Fleet request. If there is an error, the status is <code>error</code>. After all requests are placed, the status is <code>pending_fulfillment</code>. If the size of the fleet is equal to or greater than its target capacity, the status is <code>fulfilled</code>. If the size of the fleet is decreased, the status is <code>pending_termination</code> while Spot Instances are terminating.</p>"""
    create_time: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The creation date and time of the request.</p>"""
    spot_fleet_request_config: NotRequired[
        "aws_sdk_ec2.types.spot_fleet_request_config_data.SpotFleetRequestConfigData"
    ]
    """<p>The configuration of the Spot Fleet request.</p>"""
    spot_fleet_request_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Spot Fleet request.</p>"""
    spot_fleet_request_state: NotRequired["aws_sdk_ec2.types.batch_state.BatchState"]
    """<p>The state of the Spot Fleet request.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags for a Spot Fleet resource.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: SpotFleetRequestConfig, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "activity_status" in value:
        import aws_sdk_ec2.types.activity_status

        aws_sdk_ec2.types.activity_status.serialize_ec2_query(
            value["activity_status"], pairs, f"{prefix}.ActivityStatus"
        )
    if "create_time" in value:
        import aws_sdk_ec2.types.millisecond_date_time

        aws_sdk_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["create_time"], pairs, f"{prefix}.CreateTime"
        )
    if "spot_fleet_request_config" in value:
        import aws_sdk_ec2.types.spot_fleet_request_config_data

        aws_sdk_ec2.types.spot_fleet_request_config_data.serialize_ec2_query(
            value["spot_fleet_request_config"],
            pairs,
            f"{prefix}.SpotFleetRequestConfig",
        )
    if "spot_fleet_request_id" in value:
        pairs.append(
            (f"{prefix}.SpotFleetRequestId", str(value["spot_fleet_request_id"]))
        )
    if "spot_fleet_request_state" in value:
        import aws_sdk_ec2.types.batch_state

        aws_sdk_ec2.types.batch_state.serialize_ec2_query(
            value["spot_fleet_request_state"], pairs, f"{prefix}.SpotFleetRequestState"
        )
    if "tags" in value:
        import aws_sdk_ec2.types.tag_list

        aws_sdk_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{prefix}.TagSet"
        )


def deserialize_ec2_query(el: Element) -> SpotFleetRequestConfig:
    out: SpotFleetRequestConfig = {}  # type: ignore[typeddict-item]
    child_activity_status = el.find("ActivityStatus")
    if child_activity_status is not None:
        import aws_sdk_ec2.types.activity_status

        out["activity_status"] = (
            aws_sdk_ec2.types.activity_status.deserialize_ec2_query(
                child_activity_status
            )
        )
    child_create_time = el.find("CreateTime")
    if child_create_time is not None:
        import aws_sdk_ec2.types.millisecond_date_time

        out["create_time"] = (
            aws_sdk_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_create_time
            )
        )
    child_spot_fleet_request_config = el.find("SpotFleetRequestConfig")
    if child_spot_fleet_request_config is not None:
        import aws_sdk_ec2.types.spot_fleet_request_config_data

        out["spot_fleet_request_config"] = (
            aws_sdk_ec2.types.spot_fleet_request_config_data.deserialize_ec2_query(
                child_spot_fleet_request_config
            )
        )
    child_spot_fleet_request_id = el.find("SpotFleetRequestId")
    if child_spot_fleet_request_id is not None:
        out["spot_fleet_request_id"] = str(child_spot_fleet_request_id.text or "")
    child_spot_fleet_request_state = el.find("SpotFleetRequestState")
    if child_spot_fleet_request_state is not None:
        import aws_sdk_ec2.types.batch_state

        out["spot_fleet_request_state"] = (
            aws_sdk_ec2.types.batch_state.deserialize_ec2_query(
                child_spot_fleet_request_state
            )
        )
    if el.find("TagSet") is not None:
        import aws_sdk_ec2.types.tag_list

        out["tags"] = aws_sdk_ec2.types.tag_list.deserialize_ec2_query(el, "TagSet")
    return out
