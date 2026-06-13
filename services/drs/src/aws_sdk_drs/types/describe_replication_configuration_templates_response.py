"""Generated from Smithy shape ``com.amazonaws.drs#DescribeReplicationConfigurationTemplatesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_drs.types.pagination_token
    import aws_sdk_drs.types.replication_configuration_templates


class DescribeReplicationConfigurationTemplatesResponse(TypedDict):
    items: NotRequired[
        "aws_sdk_drs.types.replication_configuration_templates.ReplicationConfigurationTemplates"
    ]
    """<p>An array of Replication Configuration Templates.</p>"""
    next_token: NotRequired["aws_sdk_drs.types.pagination_token.PaginationToken"]
    """<p>The token of the next Replication Configuration Template to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeReplicationConfigurationTemplatesResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import aws_sdk_drs.types.replication_configuration_templates

        out["items"] = (
            aws_sdk_drs.types.replication_configuration_templates.serialize_json(
                value["items"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> DescribeReplicationConfigurationTemplatesResponse:
    out: DescribeReplicationConfigurationTemplatesResponse = {}  # type: ignore[typeddict-item]
    if "items" in data:
        import aws_sdk_drs.types.replication_configuration_templates

        out["items"] = (
            aws_sdk_drs.types.replication_configuration_templates.deserialize_json(
                data["items"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
