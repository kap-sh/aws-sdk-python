"""Generated from Smithy shape ``com.amazonaws.pcs#Cluster``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_pcs.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_pcs.types.cluster_slurm_configuration
    import aws_sdk_pcs.types.cluster_status
    import aws_sdk_pcs.types.endpoints
    import aws_sdk_pcs.types.error_info_list
    import aws_sdk_pcs.types.networking
    import aws_sdk_pcs.types.scheduler
    import aws_sdk_pcs.types.size


class Cluster(TypedDict, closed=True):
    name: "str"
    """<p>The name that identifies the cluster.</p>"""
    id: "str"
    """<p>The generated unique ID of the cluster.</p>"""
    arn: "str"
    """<p>The unique Amazon Resource Name (ARN) of the cluster.</p>"""
    status: "aws_sdk_pcs.types.cluster_status.ClusterStatus"
    r"""<p>The provisioning status of the cluster.</p> <note> <p>The provisioning status doesn't indicate the overall health of the cluster.</p> </note> <important> <p>The resource enters the <code>SUSPENDING</code> and <code>SUSPENDED</code> states when the scheduler is beyond end of life and we have suspended the cluster. When in these states, you can't use the cluster. The cluster controller is down and all compute instances are terminated. The resources still count toward your service quotas. You can delete a resource if its status is <code>SUSPENDED</code>. For more information, see <a href=\"https://docs.aws.amazon.com/pcs/latest/userguide/slurm-versions_faq.html\">Frequently asked questions about Slurm versions in PCS</a> in the <i>PCS User Guide</i>.</p> </important>"""
    created_at: "datetime.datetime"
    """<p>The date and time the resource was created.</p>"""
    modified_at: "datetime.datetime"
    """<p>The date and time the resource was modified.</p>"""
    scheduler: "aws_sdk_pcs.types.scheduler.Scheduler"
    size: "aws_sdk_pcs.types.size.Size"
    """<p>The size of the cluster.</p> <ul> <li> <p> <code>SMALL</code>: 32 compute nodes and 256 jobs</p> </li> <li> <p> <code>MEDIUM</code>: 512 compute nodes and 8192 jobs</p> </li> <li> <p> <code>LARGE</code>: 2048 compute nodes and 16,384 jobs</p> </li> </ul>"""
    slurm_configuration: NotRequired[
        "aws_sdk_pcs.types.cluster_slurm_configuration.ClusterSlurmConfiguration"
    ]
    """<p>Additional options related to the Slurm scheduler.</p>"""
    networking: "aws_sdk_pcs.types.networking.Networking"
    endpoints: NotRequired["aws_sdk_pcs.types.endpoints.Endpoints"]
    """<p>The list of endpoints available for interaction with the scheduler.</p>"""
    error_info: NotRequired["aws_sdk_pcs.types.error_info_list.ErrorInfoList"]
    """<p>The list of errors that occurred during cluster provisioning.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Cluster) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    import aws_sdk_pcs.types.cluster_status

    out["status"] = aws_sdk_pcs.types.cluster_status.serialize_aws_json_1_0(
        value["status"]
    )
    import aws_sdk_pcs.types._prelude.timestamp

    out["createdAt"] = aws_sdk_pcs.types._prelude.timestamp.serialize_aws_json_1_0(
        value["created_at"]
    )
    import aws_sdk_pcs.types._prelude.timestamp

    out["modifiedAt"] = aws_sdk_pcs.types._prelude.timestamp.serialize_aws_json_1_0(
        value["modified_at"]
    )
    import aws_sdk_pcs.types.scheduler

    out["scheduler"] = aws_sdk_pcs.types.scheduler.serialize_aws_json_1_0(
        value["scheduler"]
    )
    import aws_sdk_pcs.types.size

    out["size"] = aws_sdk_pcs.types.size.serialize_aws_json_1_0(value["size"])
    if "slurm_configuration" in value:
        import aws_sdk_pcs.types.cluster_slurm_configuration

        out["slurmConfiguration"] = (
            aws_sdk_pcs.types.cluster_slurm_configuration.serialize_aws_json_1_0(
                value["slurm_configuration"]
            )
        )
    import aws_sdk_pcs.types.networking

    out["networking"] = aws_sdk_pcs.types.networking.serialize_aws_json_1_0(
        value["networking"]
    )
    if "endpoints" in value:
        import aws_sdk_pcs.types.endpoints

        out["endpoints"] = aws_sdk_pcs.types.endpoints.serialize_aws_json_1_0(
            value["endpoints"]
        )
    if "error_info" in value:
        import aws_sdk_pcs.types.error_info_list

        out["errorInfo"] = aws_sdk_pcs.types.error_info_list.serialize_aws_json_1_0(
            value["error_info"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> Cluster:
    out: Cluster = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("Cluster.name required")
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("Cluster.id required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("Cluster.arn required")
    if "status" in data:
        import aws_sdk_pcs.types.cluster_status

        out["status"] = aws_sdk_pcs.types.cluster_status.deserialize_aws_json_1_0(
            data["status"]
        )
    else:
        raise DeserializationError("Cluster.status required")
    if "createdAt" in data:
        import aws_sdk_pcs.types._prelude.timestamp

        out["created_at"] = (
            aws_sdk_pcs.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("Cluster.created_at required")
    if "modifiedAt" in data:
        import aws_sdk_pcs.types._prelude.timestamp

        out["modified_at"] = (
            aws_sdk_pcs.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["modifiedAt"]
            )
        )
    else:
        raise DeserializationError("Cluster.modified_at required")
    if "scheduler" in data:
        import aws_sdk_pcs.types.scheduler

        out["scheduler"] = aws_sdk_pcs.types.scheduler.deserialize_aws_json_1_0(
            data["scheduler"]
        )
    else:
        raise DeserializationError("Cluster.scheduler required")
    if "size" in data:
        import aws_sdk_pcs.types.size

        out["size"] = aws_sdk_pcs.types.size.deserialize_aws_json_1_0(data["size"])
    else:
        raise DeserializationError("Cluster.size required")
    if "slurmConfiguration" in data:
        import aws_sdk_pcs.types.cluster_slurm_configuration

        out["slurm_configuration"] = (
            aws_sdk_pcs.types.cluster_slurm_configuration.deserialize_aws_json_1_0(
                data["slurmConfiguration"]
            )
        )
    if "networking" in data:
        import aws_sdk_pcs.types.networking

        out["networking"] = aws_sdk_pcs.types.networking.deserialize_aws_json_1_0(
            data["networking"]
        )
    else:
        raise DeserializationError("Cluster.networking required")
    if "endpoints" in data:
        import aws_sdk_pcs.types.endpoints

        out["endpoints"] = aws_sdk_pcs.types.endpoints.deserialize_aws_json_1_0(
            data["endpoints"]
        )
    if "errorInfo" in data:
        import aws_sdk_pcs.types.error_info_list

        out["error_info"] = aws_sdk_pcs.types.error_info_list.deserialize_aws_json_1_0(
            data["errorInfo"]
        )
    return out
