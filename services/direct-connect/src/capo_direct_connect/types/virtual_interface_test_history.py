"""Generated from Smithy shape ``com.amazonaws.directconnect#VirtualInterfaceTestHistory``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_direct_connect.types.bgp_peer_id_list
    import capo_direct_connect.types.end_time
    import capo_direct_connect.types.failure_test_history_status
    import capo_direct_connect.types.owner_account
    import capo_direct_connect.types.start_time
    import capo_direct_connect.types.test_duration
    import capo_direct_connect.types.test_id
    import capo_direct_connect.types.virtual_interface_id


class VirtualInterfaceTestHistory(TypedDict, closed=True):
    test_id: NotRequired["capo_direct_connect.types.test_id.TestId"]
    """<p>The ID of the virtual interface failover test.</p>"""
    virtual_interface_id: NotRequired[
        "capo_direct_connect.types.virtual_interface_id.VirtualInterfaceId"
    ]
    """<p>The ID of the tested virtual interface.</p>"""
    bgp_peers: NotRequired["capo_direct_connect.types.bgp_peer_id_list.BGPPeerIdList"]
    """<p>The BGP peers that were put in the DOWN state as part of the virtual interface failover test.</p>"""
    status: NotRequired[
        "capo_direct_connect.types.failure_test_history_status.FailureTestHistoryStatus"
    ]
    """<p>The status of the virtual interface failover test.</p>"""
    owner_account: NotRequired["capo_direct_connect.types.owner_account.OwnerAccount"]
    """<p>The owner ID of the tested virtual interface.</p>"""
    test_duration_in_minutes: NotRequired[
        "capo_direct_connect.types.test_duration.TestDuration"
    ]
    """<p>The time that the virtual interface failover test ran in minutes.</p>"""
    start_time: NotRequired["capo_direct_connect.types.start_time.StartTime"]
    """<p>The time that the virtual interface moves to the DOWN state.</p>"""
    end_time: NotRequired["capo_direct_connect.types.end_time.EndTime"]
    """<p>The time that the virtual interface moves out of the DOWN state.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VirtualInterfaceTestHistory) -> dict:
    out: dict = {}
    if "test_id" in value:
        out["testId"] = value["test_id"]
    if "virtual_interface_id" in value:
        out["virtualInterfaceId"] = value["virtual_interface_id"]
    if "bgp_peers" in value:
        import capo_direct_connect.types.bgp_peer_id_list

        out["bgpPeers"] = (
            capo_direct_connect.types.bgp_peer_id_list.serialize_aws_json_1_1(
                value["bgp_peers"]
            )
        )
    if "status" in value:
        out["status"] = value["status"]
    if "owner_account" in value:
        out["ownerAccount"] = value["owner_account"]
    if "test_duration_in_minutes" in value:
        out["testDurationInMinutes"] = value["test_duration_in_minutes"]
    if "start_time" in value:
        import capo_direct_connect.types.start_time

        out["startTime"] = capo_direct_connect.types.start_time.serialize_aws_json_1_1(
            value["start_time"]
        )
    if "end_time" in value:
        import capo_direct_connect.types.end_time

        out["endTime"] = capo_direct_connect.types.end_time.serialize_aws_json_1_1(
            value["end_time"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> VirtualInterfaceTestHistory:
    out: VirtualInterfaceTestHistory = {}  # type: ignore[typeddict-item]
    if "testId" in data:
        out["test_id"] = data["testId"]
    if "virtualInterfaceId" in data:
        out["virtual_interface_id"] = data["virtualInterfaceId"]
    if "bgpPeers" in data:
        import capo_direct_connect.types.bgp_peer_id_list

        out["bgp_peers"] = (
            capo_direct_connect.types.bgp_peer_id_list.deserialize_aws_json_1_1(
                data["bgpPeers"]
            )
        )
    if "status" in data:
        out["status"] = data["status"]
    if "ownerAccount" in data:
        out["owner_account"] = data["ownerAccount"]
    if "testDurationInMinutes" in data:
        out["test_duration_in_minutes"] = data["testDurationInMinutes"]
    if "startTime" in data:
        import capo_direct_connect.types.start_time

        out["start_time"] = (
            capo_direct_connect.types.start_time.deserialize_aws_json_1_1(
                data["startTime"]
            )
        )
    if "endTime" in data:
        import capo_direct_connect.types.end_time

        out["end_time"] = capo_direct_connect.types.end_time.deserialize_aws_json_1_1(
            data["endTime"]
        )
    return out
