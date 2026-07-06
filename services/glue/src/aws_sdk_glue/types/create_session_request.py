"""Generated from Smithy shape ``com.amazonaws.glue#CreateSessionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.connections_list
    import aws_sdk_glue.types.description_string
    import aws_sdk_glue.types.glue_version_string
    import aws_sdk_glue.types.name_string
    import aws_sdk_glue.types.nullable_double
    import aws_sdk_glue.types.nullable_integer
    import aws_sdk_glue.types.orchestration_arguments_map
    import aws_sdk_glue.types.orchestration_name_string
    import aws_sdk_glue.types.orchestration_role_arn
    import aws_sdk_glue.types.session_command
    import aws_sdk_glue.types.session_type
    import aws_sdk_glue.types.tags_map
    import aws_sdk_glue.types.timeout
    import aws_sdk_glue.types.worker_type


class CreateSessionRequest(TypedDict, closed=True):
    id: "aws_sdk_glue.types.name_string.NameString"
    """<p>The ID of the session request. </p>"""
    description: NotRequired["aws_sdk_glue.types.description_string.DescriptionString"]
    """<p>The description of the session. </p>"""
    role: "aws_sdk_glue.types.orchestration_role_arn.OrchestrationRoleArn"
    """<p>The IAM Role ARN </p>"""
    command: "aws_sdk_glue.types.session_command.SessionCommand"
    """<p>The <code>SessionCommand</code> that runs the job. </p>"""
    timeout: NotRequired["aws_sdk_glue.types.timeout.Timeout"]
    """<p> The number of minutes before session times out. Default for Spark ETL jobs is 48 hours (2880 minutes). Consult the documentation for other job types. </p>"""
    idle_timeout: NotRequired["aws_sdk_glue.types.timeout.Timeout"]
    """<p> The number of minutes when idle before session times out. Default for Spark ETL jobs is value of Timeout. Consult the documentation for other job types. </p>"""
    default_arguments: NotRequired[
        "aws_sdk_glue.types.orchestration_arguments_map.OrchestrationArgumentsMap"
    ]
    """<p>A map array of key-value pairs. Max is 75 pairs. </p>"""
    connections: NotRequired["aws_sdk_glue.types.connections_list.ConnectionsList"]
    """<p>The number of connections to use for the session. </p>"""
    max_capacity: NotRequired["aws_sdk_glue.types.nullable_double.NullableDouble"]
    """<p>The number of Glue data processing units (DPUs) that can be allocated when the job runs. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB memory. </p>"""
    number_of_workers: NotRequired[
        "aws_sdk_glue.types.nullable_integer.NullableInteger"
    ]
    """<p>The number of workers of a defined <code>WorkerType</code> to use for the session. </p>"""
    worker_type: NotRequired["aws_sdk_glue.types.worker_type.WorkerType"]
    """<p>The type of predefined worker that is allocated when a job runs. Accepts a value of G.1X, G.2X, G.4X, or G.8X for Spark jobs. Accepts the value Z.2X for Ray notebooks.</p> <ul> <li> <p>For the <code>G.1X</code> worker type, each worker maps to 1 DPU (4 vCPUs, 16 GB of memory) with 94GB disk, and provides 1 executor per worker. We recommend this worker type for workloads such as data transforms, joins, and queries, to offers a scalable and cost effective way to run most jobs.</p> </li> <li> <p>For the <code>G.2X</code> worker type, each worker maps to 2 DPU (8 vCPUs, 32 GB of memory) with 138GB disk, and provides 1 executor per worker. We recommend this worker type for workloads such as data transforms, joins, and queries, to offers a scalable and cost effective way to run most jobs.</p> </li> <li> <p>For the <code>G.4X</code> worker type, each worker maps to 4 DPU (16 vCPUs, 64 GB of memory) with 256GB disk, and provides 1 executor per worker. We recommend this worker type for jobs whose workloads contain your most demanding transforms, aggregations, joins, and queries. This worker type is available only for Glue version 3.0 or later Spark ETL jobs in the following Amazon Web Services Regions: US East (Ohio), US East (N. Virginia), US West (Oregon), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Tokyo), Canada (Central), Europe (Frankfurt), Europe (Ireland), and Europe (Stockholm).</p> </li> <li> <p>For the <code>G.8X</code> worker type, each worker maps to 8 DPU (32 vCPUs, 128 GB of memory) with 512GB disk, and provides 1 executor per worker. We recommend this worker type for jobs whose workloads contain your most demanding transforms, aggregations, joins, and queries. This worker type is available only for Glue version 3.0 or later Spark ETL jobs, in the same Amazon Web Services Regions as supported for the <code>G.4X</code> worker type.</p> </li> <li> <p>For the <code>Z.2X</code> worker type, each worker maps to 2 M-DPU (8vCPUs, 64 GB of memory) with 128 GB disk, and provides up to 8 Ray workers based on the autoscaler.</p> </li> </ul>"""
    security_configuration: NotRequired["aws_sdk_glue.types.name_string.NameString"]
    """<p>The name of the SecurityConfiguration structure to be used with the session </p>"""
    glue_version: NotRequired[
        "aws_sdk_glue.types.glue_version_string.GlueVersionString"
    ]
    """<p>The Glue version determines the versions of Apache Spark and Python that Glue supports. The GlueVersion must be greater than 2.0. </p>"""
    tags: NotRequired["aws_sdk_glue.types.tags_map.TagsMap"]
    """<p>The map of key value pairs (tags) belonging to the session.</p>"""
    request_origin: NotRequired[
        "aws_sdk_glue.types.orchestration_name_string.OrchestrationNameString"
    ]
    """<p>The origin of the request. </p>"""
    session_type: NotRequired["aws_sdk_glue.types.session_type.SessionType"]
    """<p>The type of session to create.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateSessionRequest) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    if "description" in value:
        out["Description"] = value["description"]
    out["Role"] = value["role"]
    import aws_sdk_glue.types.session_command

    out["Command"] = aws_sdk_glue.types.session_command.serialize_aws_json_1_1(
        value["command"]
    )
    if "timeout" in value:
        out["Timeout"] = value["timeout"]
    if "idle_timeout" in value:
        out["IdleTimeout"] = value["idle_timeout"]
    if "default_arguments" in value:
        import aws_sdk_glue.types.orchestration_arguments_map

        out["DefaultArguments"] = (
            aws_sdk_glue.types.orchestration_arguments_map.serialize_aws_json_1_1(
                value["default_arguments"]
            )
        )
    if "connections" in value:
        import aws_sdk_glue.types.connections_list

        out["Connections"] = aws_sdk_glue.types.connections_list.serialize_aws_json_1_1(
            value["connections"]
        )
    if "max_capacity" in value:
        out["MaxCapacity"] = value["max_capacity"]
    if "number_of_workers" in value:
        out["NumberOfWorkers"] = value["number_of_workers"]
    if "worker_type" in value:
        import aws_sdk_glue.types.worker_type

        out["WorkerType"] = aws_sdk_glue.types.worker_type.serialize_aws_json_1_1(
            value["worker_type"]
        )
    if "security_configuration" in value:
        out["SecurityConfiguration"] = value["security_configuration"]
    if "glue_version" in value:
        out["GlueVersion"] = value["glue_version"]
    if "tags" in value:
        import aws_sdk_glue.types.tags_map

        out["Tags"] = aws_sdk_glue.types.tags_map.serialize_aws_json_1_1(value["tags"])
    if "request_origin" in value:
        out["RequestOrigin"] = value["request_origin"]
    if "session_type" in value:
        import aws_sdk_glue.types.session_type

        out["SessionType"] = aws_sdk_glue.types.session_type.serialize_aws_json_1_1(
            value["session_type"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateSessionRequest:
    out: CreateSessionRequest = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("CreateSessionRequest.id required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "Role" in data:
        out["role"] = data["Role"]
    else:
        raise DeserializationError("CreateSessionRequest.role required")
    if "Command" in data:
        import aws_sdk_glue.types.session_command

        out["command"] = aws_sdk_glue.types.session_command.deserialize_aws_json_1_1(
            data["Command"]
        )
    else:
        raise DeserializationError("CreateSessionRequest.command required")
    if "Timeout" in data:
        out["timeout"] = data["Timeout"]
    if "IdleTimeout" in data:
        out["idle_timeout"] = data["IdleTimeout"]
    if "DefaultArguments" in data:
        import aws_sdk_glue.types.orchestration_arguments_map

        out["default_arguments"] = (
            aws_sdk_glue.types.orchestration_arguments_map.deserialize_aws_json_1_1(
                data["DefaultArguments"]
            )
        )
    if "Connections" in data:
        import aws_sdk_glue.types.connections_list

        out["connections"] = (
            aws_sdk_glue.types.connections_list.deserialize_aws_json_1_1(
                data["Connections"]
            )
        )
    if "MaxCapacity" in data:
        out["max_capacity"] = data["MaxCapacity"]
    if "NumberOfWorkers" in data:
        out["number_of_workers"] = data["NumberOfWorkers"]
    if "WorkerType" in data:
        import aws_sdk_glue.types.worker_type

        out["worker_type"] = aws_sdk_glue.types.worker_type.deserialize_aws_json_1_1(
            data["WorkerType"]
        )
    if "SecurityConfiguration" in data:
        out["security_configuration"] = data["SecurityConfiguration"]
    if "GlueVersion" in data:
        out["glue_version"] = data["GlueVersion"]
    if "Tags" in data:
        import aws_sdk_glue.types.tags_map

        out["tags"] = aws_sdk_glue.types.tags_map.deserialize_aws_json_1_1(data["Tags"])
    if "RequestOrigin" in data:
        out["request_origin"] = data["RequestOrigin"]
    if "SessionType" in data:
        import aws_sdk_glue.types.session_type

        out["session_type"] = aws_sdk_glue.types.session_type.deserialize_aws_json_1_1(
            data["SessionType"]
        )
    return out
