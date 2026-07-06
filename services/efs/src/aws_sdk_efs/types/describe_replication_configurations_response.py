"""Generated from Smithy shape ``com.amazonaws.efs#DescribeReplicationConfigurationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_efs.types.replication_configuration_descriptions
    import aws_sdk_efs.types.token


class DescribeReplicationConfigurationsResponse(TypedDict, closed=True):
    replications: NotRequired[
        "aws_sdk_efs.types.replication_configuration_descriptions.ReplicationConfigurationDescriptions"
    ]
    """<p>The collection of replication configurations that is returned.</p>"""
    next_token: NotRequired["aws_sdk_efs.types.token.Token"]
    """<p>You can use the <code>NextToken</code> from the previous response in a subsequent request to fetch the additional descriptions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeReplicationConfigurationsResponse) -> dict:
    out: dict = {}
    if "replications" in value:
        import aws_sdk_efs.types.replication_configuration_descriptions

        out["Replications"] = (
            aws_sdk_efs.types.replication_configuration_descriptions.serialize_json(
                value["replications"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> DescribeReplicationConfigurationsResponse:
    out: DescribeReplicationConfigurationsResponse = {}  # type: ignore[typeddict-item]
    if "Replications" in data:
        import aws_sdk_efs.types.replication_configuration_descriptions

        out["replications"] = (
            aws_sdk_efs.types.replication_configuration_descriptions.deserialize_json(
                data["Replications"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
