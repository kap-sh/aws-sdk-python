"""Generated from Smithy shape ``com.amazonaws.swf#WorkflowTypeDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_swf.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_swf.types.workflow_type_configuration
    import aws_sdk_swf.types.workflow_type_info


class WorkflowTypeDetail(TypedDict, closed=True):
    type_info: "aws_sdk_swf.types.workflow_type_info.WorkflowTypeInfo"
    """<p>General information about the workflow type.</p> <p>The status of the workflow type (returned in the WorkflowTypeInfo structure) can be one of the following.</p> <ul> <li> <p> <code>REGISTERED</code> – The type is registered and available. Workers supporting this type should be running.</p> </li> <li> <p> <code>DEPRECATED</code> – The type was deprecated using <a>DeprecateWorkflowType</a>, but is still in use. You should keep workers supporting this type running. You cannot create new workflow executions of this type.</p> </li> </ul>"""
    configuration: (
        "aws_sdk_swf.types.workflow_type_configuration.WorkflowTypeConfiguration"
    )
    """<p>Configuration settings of the workflow type registered through <a>RegisterWorkflowType</a> </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: WorkflowTypeDetail) -> dict:
    out: dict = {}
    import aws_sdk_swf.types.workflow_type_info

    out["typeInfo"] = aws_sdk_swf.types.workflow_type_info.serialize_aws_json_1_0(
        value["type_info"]
    )
    import aws_sdk_swf.types.workflow_type_configuration

    out["configuration"] = (
        aws_sdk_swf.types.workflow_type_configuration.serialize_aws_json_1_0(
            value["configuration"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> WorkflowTypeDetail:
    out: WorkflowTypeDetail = {}  # type: ignore[typeddict-item]
    if "typeInfo" in data:
        import aws_sdk_swf.types.workflow_type_info

        out["type_info"] = (
            aws_sdk_swf.types.workflow_type_info.deserialize_aws_json_1_0(
                data["typeInfo"]
            )
        )
    else:
        raise DeserializationError("WorkflowTypeDetail.type_info required")
    if "configuration" in data:
        import aws_sdk_swf.types.workflow_type_configuration

        out["configuration"] = (
            aws_sdk_swf.types.workflow_type_configuration.deserialize_aws_json_1_0(
                data["configuration"]
            )
        )
    else:
        raise DeserializationError("WorkflowTypeDetail.configuration required")
    return out
