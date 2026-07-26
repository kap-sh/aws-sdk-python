"""Generated from Smithy shape ``com.amazonaws.mgn#DescribeReplicationConfigurationTemplatesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.pagination_token
    import capo_mgn.types.replication_configuration_templates


class DescribeReplicationConfigurationTemplatesResponse(TypedDict, closed=True):
    items: NotRequired[
        "capo_mgn.types.replication_configuration_templates.ReplicationConfigurationTemplates"
    ]
    """<p>Request to describe Replication Configuration template by items.</p>"""
    next_token: NotRequired["capo_mgn.types.pagination_token.PaginationToken"]
    """<p>Request to describe Replication Configuration template by next token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeReplicationConfigurationTemplatesResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import capo_mgn.types.replication_configuration_templates

        out["items"] = (
            capo_mgn.types.replication_configuration_templates.serialize_json(
                value["items"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> DescribeReplicationConfigurationTemplatesResponse:
    out: DescribeReplicationConfigurationTemplatesResponse = {}  # type: ignore[typeddict-item]
    if "items" in data:
        import capo_mgn.types.replication_configuration_templates

        out["items"] = (
            capo_mgn.types.replication_configuration_templates.deserialize_json(
                data["items"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
