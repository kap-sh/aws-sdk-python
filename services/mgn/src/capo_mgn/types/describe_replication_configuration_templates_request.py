"""Generated from Smithy shape ``com.amazonaws.mgn#DescribeReplicationConfigurationTemplatesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.max_results_type
    import capo_mgn.types.pagination_token
    import capo_mgn.types.replication_configuration_template_i_ds


class DescribeReplicationConfigurationTemplatesRequest(TypedDict, closed=True):
    replication_configuration_template_i_ds: NotRequired[
        "capo_mgn.types.replication_configuration_template_i_ds.ReplicationConfigurationTemplateIDs"
    ]
    """<p>Request to describe Replication Configuration template by template IDs.</p>"""
    max_results: NotRequired["capo_mgn.types.max_results_type.MaxResultsType"]
    """<p>Request to describe Replication Configuration template by max results.</p>"""
    next_token: NotRequired["capo_mgn.types.pagination_token.PaginationToken"]
    """<p>Request to describe Replication Configuration template by next token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeReplicationConfigurationTemplatesRequest) -> dict:
    out: dict = {}
    if "replication_configuration_template_i_ds" in value:
        import capo_mgn.types.replication_configuration_template_i_ds

        out["replicationConfigurationTemplateIDs"] = (
            capo_mgn.types.replication_configuration_template_i_ds.serialize_json(
                value["replication_configuration_template_i_ds"]
            )
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> DescribeReplicationConfigurationTemplatesRequest:
    out: DescribeReplicationConfigurationTemplatesRequest = {}  # type: ignore[typeddict-item]
    if "replicationConfigurationTemplateIDs" in data:
        import capo_mgn.types.replication_configuration_template_i_ds

        out["replication_configuration_template_i_ds"] = (
            capo_mgn.types.replication_configuration_template_i_ds.deserialize_json(
                data["replicationConfigurationTemplateIDs"]
            )
        )
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
