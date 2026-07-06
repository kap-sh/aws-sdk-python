"""Generated from Smithy shape ``com.amazonaws.emr#InstanceGroupDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_emr.types.date
    import aws_sdk_emr.types.instance_group_state
    import aws_sdk_emr.types.instance_role_type
    import aws_sdk_emr.types.instance_type
    import aws_sdk_emr.types.integer
    import aws_sdk_emr.types.market_type
    import aws_sdk_emr.types.xml_string
    import aws_sdk_emr.types.xml_string_max_len256


class InstanceGroupDetail(TypedDict, closed=True):
    instance_group_id: NotRequired[
        "aws_sdk_emr.types.xml_string_max_len256.XmlStringMaxLen256"
    ]
    """<p>Unique identifier for the instance group.</p>"""
    name: NotRequired["aws_sdk_emr.types.xml_string_max_len256.XmlStringMaxLen256"]
    """<p>Friendly name for the instance group.</p>"""
    market: NotRequired["aws_sdk_emr.types.market_type.MarketType"]
    """<p>Market type of the Amazon EC2 instances used to create a cluster node.</p>"""
    instance_role: NotRequired["aws_sdk_emr.types.instance_role_type.InstanceRoleType"]
    """<p>Instance group role in the cluster</p>"""
    bid_price: NotRequired["aws_sdk_emr.types.xml_string_max_len256.XmlStringMaxLen256"]
    """<p>The bid price for each Amazon EC2 Spot Instance type as defined by <code>InstanceType</code>. Expressed in USD. If neither <code>BidPrice</code> nor <code>BidPriceAsPercentageOfOnDemandPrice</code> is provided, <code>BidPriceAsPercentageOfOnDemandPrice</code> defaults to 100%.</p>"""
    instance_type: NotRequired["aws_sdk_emr.types.instance_type.InstanceType"]
    """<p>Amazon EC2 instance type.</p>"""
    instance_request_count: NotRequired["aws_sdk_emr.types.integer.Integer"]
    """<p>Target number of instances to run in the instance group.</p>"""
    instance_running_count: NotRequired["aws_sdk_emr.types.integer.Integer"]
    """<p>Actual count of running instances.</p>"""
    state: NotRequired["aws_sdk_emr.types.instance_group_state.InstanceGroupState"]
    """<p>State of instance group. The following values are no longer supported: STARTING, TERMINATED, and FAILED.</p>"""
    last_state_change_reason: NotRequired["aws_sdk_emr.types.xml_string.XmlString"]
    """<p>Details regarding the state of the instance group.</p>"""
    creation_date_time: NotRequired["aws_sdk_emr.types.date.Date"]
    """<p>The date/time the instance group was created.</p>"""
    start_date_time: NotRequired["aws_sdk_emr.types.date.Date"]
    """<p>The date/time the instance group was started.</p>"""
    ready_date_time: NotRequired["aws_sdk_emr.types.date.Date"]
    """<p>The date/time the instance group was available to the cluster.</p>"""
    end_date_time: NotRequired["aws_sdk_emr.types.date.Date"]
    """<p>The date/time the instance group was terminated.</p>"""
    custom_ami_id: NotRequired[
        "aws_sdk_emr.types.xml_string_max_len256.XmlStringMaxLen256"
    ]
    """<p>The custom AMI ID to use for the provisioned instance group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceGroupDetail) -> dict:
    out: dict = {}
    if "instance_group_id" in value:
        out["InstanceGroupId"] = value["instance_group_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "market" in value:
        import aws_sdk_emr.types.market_type

        out["Market"] = aws_sdk_emr.types.market_type.serialize_aws_json_1_1(
            value["market"]
        )
    if "instance_role" in value:
        import aws_sdk_emr.types.instance_role_type

        out["InstanceRole"] = (
            aws_sdk_emr.types.instance_role_type.serialize_aws_json_1_1(
                value["instance_role"]
            )
        )
    if "bid_price" in value:
        out["BidPrice"] = value["bid_price"]
    if "instance_type" in value:
        out["InstanceType"] = value["instance_type"]
    if "instance_request_count" in value:
        out["InstanceRequestCount"] = value["instance_request_count"]
    if "instance_running_count" in value:
        out["InstanceRunningCount"] = value["instance_running_count"]
    if "state" in value:
        import aws_sdk_emr.types.instance_group_state

        out["State"] = aws_sdk_emr.types.instance_group_state.serialize_aws_json_1_1(
            value["state"]
        )
    if "last_state_change_reason" in value:
        out["LastStateChangeReason"] = value["last_state_change_reason"]
    if "creation_date_time" in value:
        import aws_sdk_emr.types.date

        out["CreationDateTime"] = aws_sdk_emr.types.date.serialize_aws_json_1_1(
            value["creation_date_time"]
        )
    if "start_date_time" in value:
        import aws_sdk_emr.types.date

        out["StartDateTime"] = aws_sdk_emr.types.date.serialize_aws_json_1_1(
            value["start_date_time"]
        )
    if "ready_date_time" in value:
        import aws_sdk_emr.types.date

        out["ReadyDateTime"] = aws_sdk_emr.types.date.serialize_aws_json_1_1(
            value["ready_date_time"]
        )
    if "end_date_time" in value:
        import aws_sdk_emr.types.date

        out["EndDateTime"] = aws_sdk_emr.types.date.serialize_aws_json_1_1(
            value["end_date_time"]
        )
    if "custom_ami_id" in value:
        out["CustomAmiId"] = value["custom_ami_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InstanceGroupDetail:
    out: InstanceGroupDetail = {}  # type: ignore[typeddict-item]
    if "InstanceGroupId" in data:
        out["instance_group_id"] = data["InstanceGroupId"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Market" in data:
        import aws_sdk_emr.types.market_type

        out["market"] = aws_sdk_emr.types.market_type.deserialize_aws_json_1_1(
            data["Market"]
        )
    if "InstanceRole" in data:
        import aws_sdk_emr.types.instance_role_type

        out["instance_role"] = (
            aws_sdk_emr.types.instance_role_type.deserialize_aws_json_1_1(
                data["InstanceRole"]
            )
        )
    if "BidPrice" in data:
        out["bid_price"] = data["BidPrice"]
    if "InstanceType" in data:
        out["instance_type"] = data["InstanceType"]
    if "InstanceRequestCount" in data:
        out["instance_request_count"] = data["InstanceRequestCount"]
    if "InstanceRunningCount" in data:
        out["instance_running_count"] = data["InstanceRunningCount"]
    if "State" in data:
        import aws_sdk_emr.types.instance_group_state

        out["state"] = aws_sdk_emr.types.instance_group_state.deserialize_aws_json_1_1(
            data["State"]
        )
    if "LastStateChangeReason" in data:
        out["last_state_change_reason"] = data["LastStateChangeReason"]
    if "CreationDateTime" in data:
        import aws_sdk_emr.types.date

        out["creation_date_time"] = aws_sdk_emr.types.date.deserialize_aws_json_1_1(
            data["CreationDateTime"]
        )
    if "StartDateTime" in data:
        import aws_sdk_emr.types.date

        out["start_date_time"] = aws_sdk_emr.types.date.deserialize_aws_json_1_1(
            data["StartDateTime"]
        )
    if "ReadyDateTime" in data:
        import aws_sdk_emr.types.date

        out["ready_date_time"] = aws_sdk_emr.types.date.deserialize_aws_json_1_1(
            data["ReadyDateTime"]
        )
    if "EndDateTime" in data:
        import aws_sdk_emr.types.date

        out["end_date_time"] = aws_sdk_emr.types.date.deserialize_aws_json_1_1(
            data["EndDateTime"]
        )
    if "CustomAmiId" in data:
        out["custom_ami_id"] = data["CustomAmiId"]
    return out
