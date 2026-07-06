"""Generated from Smithy shape ``com.amazonaws.finspace#KxCluster``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_finspace.types.availability_zone_id
    import aws_sdk_finspace.types.execution_role_arn
    import aws_sdk_finspace.types.initialization_script_file_path
    import aws_sdk_finspace.types.kx_az_mode
    import aws_sdk_finspace.types.kx_cluster_description
    import aws_sdk_finspace.types.kx_cluster_name
    import aws_sdk_finspace.types.kx_cluster_status
    import aws_sdk_finspace.types.kx_cluster_status_reason
    import aws_sdk_finspace.types.kx_cluster_type
    import aws_sdk_finspace.types.release_label
    import aws_sdk_finspace.types.timestamp
    import aws_sdk_finspace.types.volumes


class KxCluster(TypedDict, closed=True):
    status: NotRequired["aws_sdk_finspace.types.kx_cluster_status.KxClusterStatus"]
    """<p>The status of a cluster.</p> <ul> <li> <p>PENDING – The cluster is pending creation.</p> </li> <li> <p>CREATING –The cluster creation process is in progress.</p> </li> <li> <p>CREATE_FAILED– The cluster creation process has failed.</p> </li> <li> <p>RUNNING – The cluster creation process is running.</p> </li> <li> <p>UPDATING – The cluster is in the process of being updated.</p> </li> <li> <p> DELETING – The cluster is in the process of being deleted.</p> </li> <li> <p>DELETED – The cluster has been deleted.</p> </li> <li> <p>DELETE_FAILED – The cluster failed to delete.</p> </li> </ul>"""
    status_reason: NotRequired[
        "aws_sdk_finspace.types.kx_cluster_status_reason.KxClusterStatusReason"
    ]
    """<p>The error message when a failed state occurs. </p>"""
    cluster_name: NotRequired["aws_sdk_finspace.types.kx_cluster_name.KxClusterName"]
    """<p>A unique name for the cluster.</p>"""
    cluster_type: NotRequired["aws_sdk_finspace.types.kx_cluster_type.KxClusterType"]
    """<p>Specifies the type of KDB database that is being created. The following types are available: </p> <ul> <li> <p>HDB – A Historical Database. The data is only accessible with read-only permissions from one of the FinSpace managed kdb databases mounted to the cluster.</p> </li> <li> <p>RDB – A Realtime Database. This type of database captures all the data from a ticker plant and stores it in memory until the end of day, after which it writes all of its data to a disk and reloads the HDB. This cluster type requires local storage for temporary storage of data during the savedown process. If you specify this field in your request, you must provide the <code>savedownStorageConfiguration</code> parameter.</p> </li> <li> <p>GATEWAY – A gateway cluster allows you to access data across processes in kdb systems. It allows you to create your own routing logic using the initialization scripts and custom code. This type of cluster does not require a writable local storage.</p> </li> <li> <p>GP – A general purpose cluster allows you to quickly iterate on code during development by granting greater access to system commands and enabling a fast reload of custom code. This cluster type can optionally mount databases including cache and savedown storage. For this cluster type, the node count is fixed at 1. It does not support autoscaling and supports only <code>SINGLE</code> AZ mode.</p> </li> <li> <p>Tickerplant – A tickerplant cluster allows you to subscribe to feed handlers based on IAM permissions. It can publish to RDBs, other Tickerplants, and real-time subscribers (RTS). Tickerplants can persist messages to log, which is readable by any RDB environment. It supports only single-node that is only one kdb process.</p> </li> </ul>"""
    cluster_description: NotRequired[
        "aws_sdk_finspace.types.kx_cluster_description.KxClusterDescription"
    ]
    """<p>A description of the cluster.</p>"""
    release_label: NotRequired["aws_sdk_finspace.types.release_label.ReleaseLabel"]
    """<p>A version of the FinSpace managed kdb to run.</p>"""
    volumes: NotRequired["aws_sdk_finspace.types.volumes.Volumes"]
    """<p> A list of volumes attached to the cluster. </p>"""
    initialization_script: NotRequired[
        "aws_sdk_finspace.types.initialization_script_file_path.InitializationScriptFilePath"
    ]
    """<p>Specifies a Q program that will be run at launch of a cluster. It is a relative path within <i>.zip</i> file that contains the custom code, which will be loaded on the cluster. It must include the file name itself. For example, <code>somedir/init.q</code>.</p>"""
    execution_role: NotRequired[
        "aws_sdk_finspace.types.execution_role_arn.ExecutionRoleArn"
    ]
    """<p> An IAM role that defines a set of permissions associated with a cluster. These permissions are assumed when a cluster attempts to access another cluster. </p>"""
    az_mode: NotRequired["aws_sdk_finspace.types.kx_az_mode.KxAzMode"]
    """<p>The number of availability zones assigned per cluster. This can be one of the following:</p> <ul> <li> <p> <code>SINGLE</code> – Assigns one availability zone per cluster.</p> </li> <li> <p> <code>MULTI</code> – Assigns all the availability zones per cluster.</p> </li> </ul>"""
    availability_zone_id: NotRequired[
        "aws_sdk_finspace.types.availability_zone_id.AvailabilityZoneId"
    ]
    """<p> The availability zone identifiers for the requested regions. </p>"""
    last_modified_timestamp: NotRequired["aws_sdk_finspace.types.timestamp.Timestamp"]
    """<p>The last time that the cluster was modified. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.</p>"""
    created_timestamp: NotRequired["aws_sdk_finspace.types.timestamp.Timestamp"]
    """<p>The timestamp at which the cluster was created in FinSpace. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KxCluster) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_finspace.types.kx_cluster_status

        out["status"] = aws_sdk_finspace.types.kx_cluster_status.serialize_json(
            value["status"]
        )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    if "cluster_name" in value:
        out["clusterName"] = value["cluster_name"]
    if "cluster_type" in value:
        import aws_sdk_finspace.types.kx_cluster_type

        out["clusterType"] = aws_sdk_finspace.types.kx_cluster_type.serialize_json(
            value["cluster_type"]
        )
    if "cluster_description" in value:
        out["clusterDescription"] = value["cluster_description"]
    if "release_label" in value:
        out["releaseLabel"] = value["release_label"]
    if "volumes" in value:
        import aws_sdk_finspace.types.volumes

        out["volumes"] = aws_sdk_finspace.types.volumes.serialize_json(value["volumes"])
    if "initialization_script" in value:
        out["initializationScript"] = value["initialization_script"]
    if "execution_role" in value:
        out["executionRole"] = value["execution_role"]
    if "az_mode" in value:
        import aws_sdk_finspace.types.kx_az_mode

        out["azMode"] = aws_sdk_finspace.types.kx_az_mode.serialize_json(
            value["az_mode"]
        )
    if "availability_zone_id" in value:
        out["availabilityZoneId"] = value["availability_zone_id"]
    if "last_modified_timestamp" in value:
        import aws_sdk_finspace.types.timestamp

        out["lastModifiedTimestamp"] = aws_sdk_finspace.types.timestamp.serialize_json(
            value["last_modified_timestamp"]
        )
    if "created_timestamp" in value:
        import aws_sdk_finspace.types.timestamp

        out["createdTimestamp"] = aws_sdk_finspace.types.timestamp.serialize_json(
            value["created_timestamp"]
        )
    return out


def deserialize_json(data: dict) -> KxCluster:
    out: KxCluster = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import aws_sdk_finspace.types.kx_cluster_status

        out["status"] = aws_sdk_finspace.types.kx_cluster_status.deserialize_json(
            data["status"]
        )
    if "statusReason" in data:
        out["status_reason"] = data["statusReason"]
    if "clusterName" in data:
        out["cluster_name"] = data["clusterName"]
    if "clusterType" in data:
        import aws_sdk_finspace.types.kx_cluster_type

        out["cluster_type"] = aws_sdk_finspace.types.kx_cluster_type.deserialize_json(
            data["clusterType"]
        )
    if "clusterDescription" in data:
        out["cluster_description"] = data["clusterDescription"]
    if "releaseLabel" in data:
        out["release_label"] = data["releaseLabel"]
    if "volumes" in data:
        import aws_sdk_finspace.types.volumes

        out["volumes"] = aws_sdk_finspace.types.volumes.deserialize_json(
            data["volumes"]
        )
    if "initializationScript" in data:
        out["initialization_script"] = data["initializationScript"]
    if "executionRole" in data:
        out["execution_role"] = data["executionRole"]
    if "azMode" in data:
        import aws_sdk_finspace.types.kx_az_mode

        out["az_mode"] = aws_sdk_finspace.types.kx_az_mode.deserialize_json(
            data["azMode"]
        )
    if "availabilityZoneId" in data:
        out["availability_zone_id"] = data["availabilityZoneId"]
    if "lastModifiedTimestamp" in data:
        import aws_sdk_finspace.types.timestamp

        out["last_modified_timestamp"] = (
            aws_sdk_finspace.types.timestamp.deserialize_json(
                data["lastModifiedTimestamp"]
            )
        )
    if "createdTimestamp" in data:
        import aws_sdk_finspace.types.timestamp

        out["created_timestamp"] = aws_sdk_finspace.types.timestamp.deserialize_json(
            data["createdTimestamp"]
        )
    return out
