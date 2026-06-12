"""Generated from Smithy shape ``com.amazonaws.ssm#UnlabelParameterVersionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.parameter_label_list
    import aws_sdk_ssm.types.ps_parameter_name
    import aws_sdk_ssm.types.ps_parameter_version


class UnlabelParameterVersionRequest(TypedDict):
    name: "aws_sdk_ssm.types.ps_parameter_name.PSParameterName"
    """<p>The name of the parameter from which you want to delete one or more labels.</p> <note> <p>You can't enter the Amazon Resource Name (ARN) for a parameter, only the parameter name itself.</p> </note>"""
    parameter_version: "aws_sdk_ssm.types.ps_parameter_version.PSParameterVersion"
    """<p>The specific version of the parameter which you want to delete one or more labels from. If it isn't present, the call will fail.</p>"""
    labels: "aws_sdk_ssm.types.parameter_label_list.ParameterLabelList"
    """<p>One or more labels to delete from the specified parameter version.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UnlabelParameterVersionRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["ParameterVersion"] = value["parameter_version"]
    import aws_sdk_ssm.types.parameter_label_list

    out["Labels"] = aws_sdk_ssm.types.parameter_label_list.serialize_aws_json_1_1(
        value["labels"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UnlabelParameterVersionRequest:
    out: UnlabelParameterVersionRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("UnlabelParameterVersionRequest.name required")
    if "ParameterVersion" in data:
        out["parameter_version"] = data["ParameterVersion"]
    else:
        raise DeserializationError(
            "UnlabelParameterVersionRequest.parameter_version required"
        )
    if "Labels" in data:
        import aws_sdk_ssm.types.parameter_label_list

        out["labels"] = aws_sdk_ssm.types.parameter_label_list.deserialize_aws_json_1_1(
            data["Labels"]
        )
    else:
        raise DeserializationError("UnlabelParameterVersionRequest.labels required")
    return out
