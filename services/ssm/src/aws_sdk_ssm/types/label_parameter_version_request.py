"""Generated from Smithy shape ``com.amazonaws.ssm#LabelParameterVersionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.parameter_label_list
    import aws_sdk_ssm.types.ps_parameter_name
    import aws_sdk_ssm.types.ps_parameter_version


class LabelParameterVersionRequest(TypedDict):
    name: "aws_sdk_ssm.types.ps_parameter_name.PSParameterName"
    """<p>The parameter name on which you want to attach one or more labels.</p> <note> <p>You can't enter the Amazon Resource Name (ARN) for a parameter, only the parameter name itself.</p> </note>"""
    parameter_version: NotRequired[
        "aws_sdk_ssm.types.ps_parameter_version.PSParameterVersion"
    ]
    """<p>The specific version of the parameter on which you want to attach one or more labels. If no version is specified, the system attaches the label to the latest version.</p>"""
    labels: "aws_sdk_ssm.types.parameter_label_list.ParameterLabelList"
    """<p>One or more labels to attach to the specified parameter version.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LabelParameterVersionRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "parameter_version" in value:
        out["ParameterVersion"] = value["parameter_version"]
    import aws_sdk_ssm.types.parameter_label_list

    out["Labels"] = aws_sdk_ssm.types.parameter_label_list.serialize_aws_json_1_1(
        value["labels"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> LabelParameterVersionRequest:
    out: LabelParameterVersionRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("LabelParameterVersionRequest.name required")
    if "ParameterVersion" in data:
        out["parameter_version"] = data["ParameterVersion"]
    if "Labels" in data:
        import aws_sdk_ssm.types.parameter_label_list

        out["labels"] = aws_sdk_ssm.types.parameter_label_list.deserialize_aws_json_1_1(
            data["Labels"]
        )
    else:
        raise DeserializationError("LabelParameterVersionRequest.labels required")
    return out
