"""Generated from Smithy shape ``com.amazonaws.glue#Session``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.connections_list
    import aws_sdk_glue.types.description_string
    import aws_sdk_glue.types.double_value
    import aws_sdk_glue.types.glue_version_string
    import aws_sdk_glue.types.idle_timeout
    import aws_sdk_glue.types.name_string
    import aws_sdk_glue.types.nullable_double
    import aws_sdk_glue.types.nullable_integer
    import aws_sdk_glue.types.orchestration_arguments_map
    import aws_sdk_glue.types.orchestration_role_arn
    import aws_sdk_glue.types.session_command
    import aws_sdk_glue.types.session_status
    import aws_sdk_glue.types.session_type
    import aws_sdk_glue.types.timestamp_value
    import aws_sdk_glue.types.worker_type


class Session(TypedDict, closed=True):
    id: NotRequired["aws_sdk_glue.types.name_string.NameString"]
    """<p>The ID of the session.</p>"""
    created_on: NotRequired["aws_sdk_glue.types.timestamp_value.TimestampValue"]
    """<p>The time and date when the session was created.</p>"""
    status: NotRequired["aws_sdk_glue.types.session_status.SessionStatus"]
    """<p>The session status. </p>"""
    error_message: NotRequired[
        "aws_sdk_glue.types.description_string.DescriptionString"
    ]
    """<p>The error message displayed during the session.</p>"""
    description: NotRequired["aws_sdk_glue.types.description_string.DescriptionString"]
    """<p>The description of the session.</p>"""
    role: NotRequired["aws_sdk_glue.types.orchestration_role_arn.OrchestrationRoleArn"]
    """<p>The name or Amazon Resource Name (ARN) of the IAM role associated with the Session.</p>"""
    command: NotRequired["aws_sdk_glue.types.session_command.SessionCommand"]
    """<p>The command object.See SessionCommand.</p>"""
    default_arguments: NotRequired[
        "aws_sdk_glue.types.orchestration_arguments_map.OrchestrationArgumentsMap"
    ]
    """<p>A map array of key-value pairs. Max is 75 pairs. </p>"""
    connections: NotRequired["aws_sdk_glue.types.connections_list.ConnectionsList"]
    """<p>The number of connections used for the session.</p>"""
    progress: "aws_sdk_glue.types.double_value.DoubleValue"
    """<p>The code execution progress of the session.</p>"""
    max_capacity: NotRequired["aws_sdk_glue.types.nullable_double.NullableDouble"]
    """<p>The number of Glue data processing units (DPUs) that can be allocated when the job runs. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB memory. </p>"""
    security_configuration: NotRequired["aws_sdk_glue.types.name_string.NameString"]
    """<p>The name of the SecurityConfiguration structure to be used with the session.</p>"""
    glue_version: NotRequired[
        "aws_sdk_glue.types.glue_version_string.GlueVersionString"
    ]
    """<p>The Glue version determines the versions of Apache Spark and Python that Glue supports. The GlueVersion must be greater than 2.0.</p>"""
    number_of_workers: NotRequired[
        "aws_sdk_glue.types.nullable_integer.NullableInteger"
    ]
    """<p>The number of workers of a defined <code>WorkerType</code> to use for the session.</p>"""
    worker_type: NotRequired["aws_sdk_glue.types.worker_type.WorkerType"]
    """<p>The type of predefined worker that is allocated when a session runs. Accepts a value of <code>G.1X</code>, <code>G.2X</code>, <code>G.4X</code>, or <code>G.8X</code> for Spark sessions. Accepts the value <code>Z.2X</code> for Ray sessions.</p>"""
    completed_on: NotRequired["aws_sdk_glue.types.timestamp_value.TimestampValue"]
    """<p>The date and time that this session is completed.</p>"""
    execution_time: NotRequired["aws_sdk_glue.types.nullable_double.NullableDouble"]
    """<p>The total time the session ran for.</p>"""
    dpu_seconds: NotRequired["aws_sdk_glue.types.nullable_double.NullableDouble"]
    """<p>The DPUs consumed by the session (formula: ExecutionTime * MaxCapacity).</p>"""
    idle_timeout: NotRequired["aws_sdk_glue.types.idle_timeout.IdleTimeout"]
    """<p>The number of minutes when idle before the session times out.</p>"""
    profile_name: NotRequired["aws_sdk_glue.types.name_string.NameString"]
    """<p>The name of an Glue usage profile associated with the session.</p>"""
    session_type: NotRequired["aws_sdk_glue.types.session_type.SessionType"]
    """<p>The type of the session.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Session) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "created_on" in value:
        import aws_sdk_glue.types.timestamp_value

        out["CreatedOn"] = aws_sdk_glue.types.timestamp_value.serialize_aws_json_1_1(
            value["created_on"]
        )
    if "status" in value:
        import aws_sdk_glue.types.session_status

        out["Status"] = aws_sdk_glue.types.session_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    if "description" in value:
        out["Description"] = value["description"]
    if "role" in value:
        out["Role"] = value["role"]
    if "command" in value:
        import aws_sdk_glue.types.session_command

        out["Command"] = aws_sdk_glue.types.session_command.serialize_aws_json_1_1(
            value["command"]
        )
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
    out["Progress"] = value.get("progress", 0)
    if "max_capacity" in value:
        out["MaxCapacity"] = value["max_capacity"]
    if "security_configuration" in value:
        out["SecurityConfiguration"] = value["security_configuration"]
    if "glue_version" in value:
        out["GlueVersion"] = value["glue_version"]
    if "number_of_workers" in value:
        out["NumberOfWorkers"] = value["number_of_workers"]
    if "worker_type" in value:
        import aws_sdk_glue.types.worker_type

        out["WorkerType"] = aws_sdk_glue.types.worker_type.serialize_aws_json_1_1(
            value["worker_type"]
        )
    if "completed_on" in value:
        import aws_sdk_glue.types.timestamp_value

        out["CompletedOn"] = aws_sdk_glue.types.timestamp_value.serialize_aws_json_1_1(
            value["completed_on"]
        )
    if "execution_time" in value:
        out["ExecutionTime"] = value["execution_time"]
    if "dpu_seconds" in value:
        out["DPUSeconds"] = value["dpu_seconds"]
    if "idle_timeout" in value:
        out["IdleTimeout"] = value["idle_timeout"]
    if "profile_name" in value:
        out["ProfileName"] = value["profile_name"]
    if "session_type" in value:
        import aws_sdk_glue.types.session_type

        out["SessionType"] = aws_sdk_glue.types.session_type.serialize_aws_json_1_1(
            value["session_type"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Session:
    out: Session = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "CreatedOn" in data:
        import aws_sdk_glue.types.timestamp_value

        out["created_on"] = aws_sdk_glue.types.timestamp_value.deserialize_aws_json_1_1(
            data["CreatedOn"]
        )
    if "Status" in data:
        import aws_sdk_glue.types.session_status

        out["status"] = aws_sdk_glue.types.session_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Role" in data:
        out["role"] = data["Role"]
    if "Command" in data:
        import aws_sdk_glue.types.session_command

        out["command"] = aws_sdk_glue.types.session_command.deserialize_aws_json_1_1(
            data["Command"]
        )
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
    if "Progress" in data:
        out["progress"] = data["Progress"]
    else:
        out["progress"] = 0
    if "MaxCapacity" in data:
        out["max_capacity"] = data["MaxCapacity"]
    if "SecurityConfiguration" in data:
        out["security_configuration"] = data["SecurityConfiguration"]
    if "GlueVersion" in data:
        out["glue_version"] = data["GlueVersion"]
    if "NumberOfWorkers" in data:
        out["number_of_workers"] = data["NumberOfWorkers"]
    if "WorkerType" in data:
        import aws_sdk_glue.types.worker_type

        out["worker_type"] = aws_sdk_glue.types.worker_type.deserialize_aws_json_1_1(
            data["WorkerType"]
        )
    if "CompletedOn" in data:
        import aws_sdk_glue.types.timestamp_value

        out["completed_on"] = (
            aws_sdk_glue.types.timestamp_value.deserialize_aws_json_1_1(
                data["CompletedOn"]
            )
        )
    if "ExecutionTime" in data:
        out["execution_time"] = data["ExecutionTime"]
    if "DPUSeconds" in data:
        out["dpu_seconds"] = data["DPUSeconds"]
    if "IdleTimeout" in data:
        out["idle_timeout"] = data["IdleTimeout"]
    if "ProfileName" in data:
        out["profile_name"] = data["ProfileName"]
    if "SessionType" in data:
        import aws_sdk_glue.types.session_type

        out["session_type"] = aws_sdk_glue.types.session_type.deserialize_aws_json_1_1(
            data["SessionType"]
        )
    return out
