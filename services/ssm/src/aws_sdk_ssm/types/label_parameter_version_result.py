"""Generated from Smithy shape ``com.amazonaws.ssm#LabelParameterVersionResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ssm.types.parameter_label_list
    import aws_sdk_ssm.types.ps_parameter_version


class LabelParameterVersionResult(TypedDict):
    invalid_labels: NotRequired[
        "aws_sdk_ssm.types.parameter_label_list.ParameterLabelList"
    ]
    r"""<p>The label doesn't meet the requirements. For information about parameter label requirements, see <a href=\"https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-paramstore-labels.html\">Working with parameter labels</a> in the <i>Amazon Web Services Systems Manager User Guide</i>.</p>"""
    parameter_version: "aws_sdk_ssm.types.ps_parameter_version.PSParameterVersion"
    """<p>The version of the parameter that has been labeled.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LabelParameterVersionResult) -> dict:
    out: dict = {}
    if "invalid_labels" in value:
        import aws_sdk_ssm.types.parameter_label_list

        out["InvalidLabels"] = (
            aws_sdk_ssm.types.parameter_label_list.serialize_aws_json_1_1(
                value["invalid_labels"]
            )
        )
    out["ParameterVersion"] = value.get("parameter_version", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> LabelParameterVersionResult:
    out: LabelParameterVersionResult = {}  # type: ignore[typeddict-item]
    if "InvalidLabels" in data:
        import aws_sdk_ssm.types.parameter_label_list

        out["invalid_labels"] = (
            aws_sdk_ssm.types.parameter_label_list.deserialize_aws_json_1_1(
                data["InvalidLabels"]
            )
        )
    if "ParameterVersion" in data:
        out["parameter_version"] = data["ParameterVersion"]
    else:
        out["parameter_version"] = 0
    return out
