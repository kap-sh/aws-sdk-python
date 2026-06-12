"""Generated from Smithy shape ``com.amazonaws.mgn#DescribeSourceServersRequestFilters``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_mgn.types.describe_source_servers_request_application_i_ds
    import aws_sdk_mgn.types.describe_source_servers_request_filters_i_ds
    import aws_sdk_mgn.types.life_cycle_states
    import aws_sdk_mgn.types.replication_types

class DescribeSourceServersRequestFilters(TypedDict):
    source_server_i_ds: NotRequired["aws_sdk_mgn.types.describe_source_servers_request_filters_i_ds.DescribeSourceServersRequestFiltersIDs"]
    """<p>Request to filter Source Servers list by Source Server ID.</p>"""
    is_archived: NotRequired["bool"]
    """<p>Request to filter Source Servers list by archived.</p>"""
    replication_types: NotRequired["aws_sdk_mgn.types.replication_types.ReplicationTypes"]
    """<p>Request to filter Source Servers list by replication type.</p>"""
    life_cycle_states: NotRequired["aws_sdk_mgn.types.life_cycle_states.LifeCycleStates"]
    """<p>Request to filter Source Servers list by life cycle states.</p>"""
    application_i_ds: NotRequired["aws_sdk_mgn.types.describe_source_servers_request_application_i_ds.DescribeSourceServersRequestApplicationIDs"]
    """<p>Request to filter Source Servers list by application IDs.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: DescribeSourceServersRequestFilters) -> dict:
    out: dict = {}
    if "source_server_i_ds" in value:
        import aws_sdk_mgn.types.describe_source_servers_request_filters_i_ds
        out["sourceServerIDs"] = aws_sdk_mgn.types.describe_source_servers_request_filters_i_ds.serialize_json(value["source_server_i_ds"])
    if "is_archived" in value:
        out["isArchived"] = value["is_archived"]
    if "replication_types" in value:
        import aws_sdk_mgn.types.replication_types
        out["replicationTypes"] = aws_sdk_mgn.types.replication_types.serialize_json(value["replication_types"])
    if "life_cycle_states" in value:
        import aws_sdk_mgn.types.life_cycle_states
        out["lifeCycleStates"] = aws_sdk_mgn.types.life_cycle_states.serialize_json(value["life_cycle_states"])
    if "application_i_ds" in value:
        import aws_sdk_mgn.types.describe_source_servers_request_application_i_ds
        out["applicationIDs"] = aws_sdk_mgn.types.describe_source_servers_request_application_i_ds.serialize_json(value["application_i_ds"])
    return out


def deserialize_json(data: dict) -> DescribeSourceServersRequestFilters:
    out: DescribeSourceServersRequestFilters = {}  # type: ignore[typeddict-item]
    if "sourceServerIDs" in data:
        import aws_sdk_mgn.types.describe_source_servers_request_filters_i_ds
        out["source_server_i_ds"] = aws_sdk_mgn.types.describe_source_servers_request_filters_i_ds.deserialize_json(data["sourceServerIDs"])
    if "isArchived" in data:
        out["is_archived"] = data["isArchived"]
    if "replicationTypes" in data:
        import aws_sdk_mgn.types.replication_types
        out["replication_types"] = aws_sdk_mgn.types.replication_types.deserialize_json(data["replicationTypes"])
    if "lifeCycleStates" in data:
        import aws_sdk_mgn.types.life_cycle_states
        out["life_cycle_states"] = aws_sdk_mgn.types.life_cycle_states.deserialize_json(data["lifeCycleStates"])
    if "applicationIDs" in data:
        import aws_sdk_mgn.types.describe_source_servers_request_application_i_ds
        out["application_i_ds"] = aws_sdk_mgn.types.describe_source_servers_request_application_i_ds.deserialize_json(data["applicationIDs"])
    return out