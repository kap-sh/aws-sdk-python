"""Generated from Smithy shape ``com.amazonaws.glue#CreateDevEndpointResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.generic_string
    import aws_sdk_glue.types.glue_version_string
    import aws_sdk_glue.types.integer_value
    import aws_sdk_glue.types.map_value
    import aws_sdk_glue.types.name_string
    import aws_sdk_glue.types.nullable_integer
    import aws_sdk_glue.types.role_arn
    import aws_sdk_glue.types.string_list
    import aws_sdk_glue.types.timestamp_value
    import aws_sdk_glue.types.worker_type


class CreateDevEndpointResponse(TypedDict, closed=True):
    endpoint_name: NotRequired["aws_sdk_glue.types.generic_string.GenericString"]
    """<p>The name assigned to the new <code>DevEndpoint</code>.</p>"""
    status: NotRequired["aws_sdk_glue.types.generic_string.GenericString"]
    """<p>The current status of the new <code>DevEndpoint</code>.</p>"""
    security_group_ids: NotRequired["aws_sdk_glue.types.string_list.StringList"]
    """<p>The security groups assigned to the new <code>DevEndpoint</code>.</p>"""
    subnet_id: NotRequired["aws_sdk_glue.types.generic_string.GenericString"]
    """<p>The subnet ID assigned to the new <code>DevEndpoint</code>.</p>"""
    role_arn: NotRequired["aws_sdk_glue.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of the role assigned to the new <code>DevEndpoint</code>.</p>"""
    yarn_endpoint_address: NotRequired[
        "aws_sdk_glue.types.generic_string.GenericString"
    ]
    """<p>The address of the YARN endpoint used by this <code>DevEndpoint</code>.</p>"""
    zeppelin_remote_spark_interpreter_port: (
        "aws_sdk_glue.types.integer_value.IntegerValue"
    )
    """<p>The Apache Zeppelin port for the remote Apache Spark interpreter.</p>"""
    number_of_nodes: "aws_sdk_glue.types.integer_value.IntegerValue"
    """<p>The number of Glue Data Processing Units (DPUs) allocated to this DevEndpoint.</p>"""
    worker_type: NotRequired["aws_sdk_glue.types.worker_type.WorkerType"]
    """<p>The type of predefined worker that is allocated to the development endpoint. May be a value of Standard, G.1X, or G.2X.</p>"""
    glue_version: NotRequired[
        "aws_sdk_glue.types.glue_version_string.GlueVersionString"
    ]
    r"""<p>Glue version determines the versions of Apache Spark and Python that Glue supports. The Python version indicates the version supported for running your ETL scripts on development endpoints. </p> <p>For more information about the available Glue versions and corresponding Spark and Python versions, see <a href=\"https://docs.aws.amazon.com/glue/latest/dg/add-job.html\">Glue version</a> in the developer guide.</p>"""
    number_of_workers: NotRequired[
        "aws_sdk_glue.types.nullable_integer.NullableInteger"
    ]
    """<p>The number of workers of a defined <code>workerType</code> that are allocated to the development endpoint.</p>"""
    availability_zone: NotRequired["aws_sdk_glue.types.generic_string.GenericString"]
    """<p>The Amazon Web Services Availability Zone where this <code>DevEndpoint</code> is located.</p>"""
    vpc_id: NotRequired["aws_sdk_glue.types.generic_string.GenericString"]
    """<p>The ID of the virtual private cloud (VPC) used by this <code>DevEndpoint</code>.</p>"""
    extra_python_libs_s3_path: NotRequired[
        "aws_sdk_glue.types.generic_string.GenericString"
    ]
    """<p>The paths to one or more Python libraries in an S3 bucket that will be loaded in your <code>DevEndpoint</code>.</p>"""
    extra_jars_s3_path: NotRequired["aws_sdk_glue.types.generic_string.GenericString"]
    """<p>Path to one or more Java <code>.jar</code> files in an S3 bucket that will be loaded in your <code>DevEndpoint</code>.</p>"""
    failure_reason: NotRequired["aws_sdk_glue.types.generic_string.GenericString"]
    """<p>The reason for a current failure in this <code>DevEndpoint</code>.</p>"""
    security_configuration: NotRequired["aws_sdk_glue.types.name_string.NameString"]
    """<p>The name of the <code>SecurityConfiguration</code> structure being used with this <code>DevEndpoint</code>.</p>"""
    created_timestamp: NotRequired["aws_sdk_glue.types.timestamp_value.TimestampValue"]
    """<p>The point in time at which this <code>DevEndpoint</code> was created.</p>"""
    arguments: NotRequired["aws_sdk_glue.types.map_value.MapValue"]
    r"""<p>The map of arguments used to configure this <code>DevEndpoint</code>.</p> <p>Valid arguments are:</p> <ul> <li> <p> <code>\"--enable-glue-datacatalog\": \"\"</code> </p> </li> </ul> <p>You can specify a version of Python support for development endpoints by using the <code>Arguments</code> parameter in the <code>CreateDevEndpoint</code> or <code>UpdateDevEndpoint</code> APIs. If no arguments are provided, the version defaults to Python 2.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateDevEndpointResponse) -> dict:
    out: dict = {}
    if "endpoint_name" in value:
        out["EndpointName"] = value["endpoint_name"]
    if "status" in value:
        out["Status"] = value["status"]
    if "security_group_ids" in value:
        import aws_sdk_glue.types.string_list

        out["SecurityGroupIds"] = aws_sdk_glue.types.string_list.serialize_aws_json_1_1(
            value["security_group_ids"]
        )
    if "subnet_id" in value:
        out["SubnetId"] = value["subnet_id"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "yarn_endpoint_address" in value:
        out["YarnEndpointAddress"] = value["yarn_endpoint_address"]
    out["ZeppelinRemoteSparkInterpreterPort"] = value.get(
        "zeppelin_remote_spark_interpreter_port", 0
    )
    out["NumberOfNodes"] = value.get("number_of_nodes", 0)
    if "worker_type" in value:
        import aws_sdk_glue.types.worker_type

        out["WorkerType"] = aws_sdk_glue.types.worker_type.serialize_aws_json_1_1(
            value["worker_type"]
        )
    if "glue_version" in value:
        out["GlueVersion"] = value["glue_version"]
    if "number_of_workers" in value:
        out["NumberOfWorkers"] = value["number_of_workers"]
    if "availability_zone" in value:
        out["AvailabilityZone"] = value["availability_zone"]
    if "vpc_id" in value:
        out["VpcId"] = value["vpc_id"]
    if "extra_python_libs_s3_path" in value:
        out["ExtraPythonLibsS3Path"] = value["extra_python_libs_s3_path"]
    if "extra_jars_s3_path" in value:
        out["ExtraJarsS3Path"] = value["extra_jars_s3_path"]
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    if "security_configuration" in value:
        out["SecurityConfiguration"] = value["security_configuration"]
    if "created_timestamp" in value:
        import aws_sdk_glue.types.timestamp_value

        out["CreatedTimestamp"] = (
            aws_sdk_glue.types.timestamp_value.serialize_aws_json_1_1(
                value["created_timestamp"]
            )
        )
    if "arguments" in value:
        import aws_sdk_glue.types.map_value

        out["Arguments"] = aws_sdk_glue.types.map_value.serialize_aws_json_1_1(
            value["arguments"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateDevEndpointResponse:
    out: CreateDevEndpointResponse = {}  # type: ignore[typeddict-item]
    if "EndpointName" in data:
        out["endpoint_name"] = data["EndpointName"]
    if "Status" in data:
        out["status"] = data["Status"]
    if "SecurityGroupIds" in data:
        import aws_sdk_glue.types.string_list

        out["security_group_ids"] = (
            aws_sdk_glue.types.string_list.deserialize_aws_json_1_1(
                data["SecurityGroupIds"]
            )
        )
    if "SubnetId" in data:
        out["subnet_id"] = data["SubnetId"]
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    if "YarnEndpointAddress" in data:
        out["yarn_endpoint_address"] = data["YarnEndpointAddress"]
    if "ZeppelinRemoteSparkInterpreterPort" in data:
        out["zeppelin_remote_spark_interpreter_port"] = data[
            "ZeppelinRemoteSparkInterpreterPort"
        ]
    else:
        out["zeppelin_remote_spark_interpreter_port"] = 0
    if "NumberOfNodes" in data:
        out["number_of_nodes"] = data["NumberOfNodes"]
    else:
        out["number_of_nodes"] = 0
    if "WorkerType" in data:
        import aws_sdk_glue.types.worker_type

        out["worker_type"] = aws_sdk_glue.types.worker_type.deserialize_aws_json_1_1(
            data["WorkerType"]
        )
    if "GlueVersion" in data:
        out["glue_version"] = data["GlueVersion"]
    if "NumberOfWorkers" in data:
        out["number_of_workers"] = data["NumberOfWorkers"]
    if "AvailabilityZone" in data:
        out["availability_zone"] = data["AvailabilityZone"]
    if "VpcId" in data:
        out["vpc_id"] = data["VpcId"]
    if "ExtraPythonLibsS3Path" in data:
        out["extra_python_libs_s3_path"] = data["ExtraPythonLibsS3Path"]
    if "ExtraJarsS3Path" in data:
        out["extra_jars_s3_path"] = data["ExtraJarsS3Path"]
    if "FailureReason" in data:
        out["failure_reason"] = data["FailureReason"]
    if "SecurityConfiguration" in data:
        out["security_configuration"] = data["SecurityConfiguration"]
    if "CreatedTimestamp" in data:
        import aws_sdk_glue.types.timestamp_value

        out["created_timestamp"] = (
            aws_sdk_glue.types.timestamp_value.deserialize_aws_json_1_1(
                data["CreatedTimestamp"]
            )
        )
    if "Arguments" in data:
        import aws_sdk_glue.types.map_value

        out["arguments"] = aws_sdk_glue.types.map_value.deserialize_aws_json_1_1(
            data["Arguments"]
        )
    return out
