"""Generated from Smithy shape ``com.amazonaws.emr#ExecutionEngineConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr.types.execution_engine_type
    import aws_sdk_emr.types.iam_role_arn
    import aws_sdk_emr.types.xml_string_max_len256


class ExecutionEngineConfig(TypedDict):
    id: NotRequired["aws_sdk_emr.types.xml_string_max_len256.XmlStringMaxLen256"]
    """<p>The unique identifier of the execution engine. For an Amazon EMR cluster, this is the cluster ID.</p>"""
    type: NotRequired["aws_sdk_emr.types.execution_engine_type.ExecutionEngineType"]
    """<p>The type of execution engine. A value of <code>EMR</code> specifies an Amazon EMR cluster.</p>"""
    master_instance_security_group_id: NotRequired[
        "aws_sdk_emr.types.xml_string_max_len256.XmlStringMaxLen256"
    ]
    r"""<p>An optional unique ID of an Amazon EC2 security group to associate with the master instance of the Amazon EMR cluster for this notebook execution. For more information see <a href=\"https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-managed-notebooks-security-groups.html\">Specifying Amazon EC2 Security Groups for Amazon EMR Notebooks</a> in the <i>EMR Management Guide</i>.</p>"""
    execution_role_arn: NotRequired["aws_sdk_emr.types.iam_role_arn.IAMRoleArn"]
    """<p>The execution role ARN required for the notebook execution.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExecutionEngineConfig) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "type" in value:
        import aws_sdk_emr.types.execution_engine_type

        out["Type"] = aws_sdk_emr.types.execution_engine_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "master_instance_security_group_id" in value:
        out["MasterInstanceSecurityGroupId"] = value[
            "master_instance_security_group_id"
        ]
    if "execution_role_arn" in value:
        out["ExecutionRoleArn"] = value["execution_role_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ExecutionEngineConfig:
    out: ExecutionEngineConfig = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Type" in data:
        import aws_sdk_emr.types.execution_engine_type

        out["type"] = aws_sdk_emr.types.execution_engine_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    if "MasterInstanceSecurityGroupId" in data:
        out["master_instance_security_group_id"] = data["MasterInstanceSecurityGroupId"]
    if "ExecutionRoleArn" in data:
        out["execution_role_arn"] = data["ExecutionRoleArn"]
    return out
