"""Generated from Smithy shape ``com.amazonaws.ssm#DeleteParametersResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm.types.parameter_name_list


class DeleteParametersResult(TypedDict, closed=True):
    deleted_parameters: NotRequired[
        "aws_sdk_ssm.types.parameter_name_list.ParameterNameList"
    ]
    """<p>The names of the deleted parameters.</p>"""
    invalid_parameters: NotRequired[
        "aws_sdk_ssm.types.parameter_name_list.ParameterNameList"
    ]
    """<p>The names of parameters that weren't deleted because the parameters aren't valid.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteParametersResult) -> dict:
    out: dict = {}
    if "deleted_parameters" in value:
        import aws_sdk_ssm.types.parameter_name_list

        out["DeletedParameters"] = (
            aws_sdk_ssm.types.parameter_name_list.serialize_aws_json_1_1(
                value["deleted_parameters"]
            )
        )
    if "invalid_parameters" in value:
        import aws_sdk_ssm.types.parameter_name_list

        out["InvalidParameters"] = (
            aws_sdk_ssm.types.parameter_name_list.serialize_aws_json_1_1(
                value["invalid_parameters"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteParametersResult:
    out: DeleteParametersResult = {}  # type: ignore[typeddict-item]
    if "DeletedParameters" in data:
        import aws_sdk_ssm.types.parameter_name_list

        out["deleted_parameters"] = (
            aws_sdk_ssm.types.parameter_name_list.deserialize_aws_json_1_1(
                data["DeletedParameters"]
            )
        )
    if "InvalidParameters" in data:
        import aws_sdk_ssm.types.parameter_name_list

        out["invalid_parameters"] = (
            aws_sdk_ssm.types.parameter_name_list.deserialize_aws_json_1_1(
                data["InvalidParameters"]
            )
        )
    return out
