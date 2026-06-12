"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsRdsDbParameterGroup``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsRdsDbParameterGroup(TypedDict):
    db_parameter_group_name: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The name of the parameter group.</p>"""
    parameter_apply_status: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The status of parameter updates.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsRdsDbParameterGroup) -> dict:
    out: dict = {}
    if "db_parameter_group_name" in value:
        out["DbParameterGroupName"] = value["db_parameter_group_name"]
    if "parameter_apply_status" in value:
        out["ParameterApplyStatus"] = value["parameter_apply_status"]
    return out


def deserialize_json(data: dict) -> AwsRdsDbParameterGroup:
    out: AwsRdsDbParameterGroup = {}  # type: ignore[typeddict-item]
    if "DbParameterGroupName" in data:
        out["db_parameter_group_name"] = data["DbParameterGroupName"]
    if "ParameterApplyStatus" in data:
        out["parameter_apply_status"] = data["ParameterApplyStatus"]
    return out
