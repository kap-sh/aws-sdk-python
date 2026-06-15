"""Generated from Smithy shape ``com.amazonaws.connect#DescribeInstanceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.instance
    import aws_sdk_connect.types.replication_configuration


class DescribeInstanceResponse(TypedDict):
    instance: NotRequired["aws_sdk_connect.types.instance.Instance"]
    """<p>The name of the instance.</p>"""
    replication_configuration: NotRequired[
        "aws_sdk_connect.types.replication_configuration.ReplicationConfiguration"
    ]
    r"""<p>Status information about the replication process. This field is included only when you are using the <a href=\"https://docs.aws.amazon.com/connect/latest/APIReference/API_ReplicateInstance.html\">ReplicateInstance</a> API to replicate an Connect Customer instance across Amazon Web Services Regions. For information about replicating Connect Customer instances, see <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/create-replica-connect-instance.html\">Create a replica of your existing Connect Customer instance</a> in the <i>Connect Customer Administrator Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeInstanceResponse) -> dict:
    out: dict = {}
    if "instance" in value:
        import aws_sdk_connect.types.instance

        out["Instance"] = aws_sdk_connect.types.instance.serialize_json(
            value["instance"]
        )
    if "replication_configuration" in value:
        import aws_sdk_connect.types.replication_configuration

        out["ReplicationConfiguration"] = (
            aws_sdk_connect.types.replication_configuration.serialize_json(
                value["replication_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeInstanceResponse:
    out: DescribeInstanceResponse = {}  # type: ignore[typeddict-item]
    if "Instance" in data:
        import aws_sdk_connect.types.instance

        out["instance"] = aws_sdk_connect.types.instance.deserialize_json(
            data["Instance"]
        )
    if "ReplicationConfiguration" in data:
        import aws_sdk_connect.types.replication_configuration

        out["replication_configuration"] = (
            aws_sdk_connect.types.replication_configuration.deserialize_json(
                data["ReplicationConfiguration"]
            )
        )
    return out
