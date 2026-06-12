"""Generated from Smithy shape ``com.amazonaws.drs#DescribeReplicationConfigurationTemplatesRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_drs.types.pagination_token
    import aws_sdk_drs.types.replication_configuration_template_i_ds
    import aws_sdk_drs.types.strictly_positive_integer

class DescribeReplicationConfigurationTemplatesRequest(TypedDict):
    replication_configuration_template_i_ds: NotRequired["aws_sdk_drs.types.replication_configuration_template_i_ds.ReplicationConfigurationTemplateIDs"]
    """<p>The IDs of the Replication Configuration Templates to retrieve. An empty list means all Replication Configuration Templates.</p>"""
    max_results: NotRequired["aws_sdk_drs.types.strictly_positive_integer.StrictlyPositiveInteger"]
    """<p>Maximum number of Replication Configuration Templates to retrieve.</p>"""
    next_token: NotRequired["aws_sdk_drs.types.pagination_token.PaginationToken"]
    """<p>The token of the next Replication Configuration Template to retrieve.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: DescribeReplicationConfigurationTemplatesRequest) -> dict:
    out: dict = {}
    if "replication_configuration_template_i_ds" in value:
        import aws_sdk_drs.types.replication_configuration_template_i_ds
        out["replicationConfigurationTemplateIDs"] = aws_sdk_drs.types.replication_configuration_template_i_ds.serialize_json(value["replication_configuration_template_i_ds"])
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> DescribeReplicationConfigurationTemplatesRequest:
    out: DescribeReplicationConfigurationTemplatesRequest = {}  # type: ignore[typeddict-item]
    if "replicationConfigurationTemplateIDs" in data:
        import aws_sdk_drs.types.replication_configuration_template_i_ds
        out["replication_configuration_template_i_ds"] = aws_sdk_drs.types.replication_configuration_template_i_ds.deserialize_json(data["replicationConfigurationTemplateIDs"])
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out