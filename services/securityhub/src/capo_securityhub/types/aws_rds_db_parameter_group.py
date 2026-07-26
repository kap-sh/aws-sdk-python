"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsRdsDbParameterGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string


class AwsRdsDbParameterGroup(TypedDict, closed=True):
    db_parameter_group_name: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The name of the parameter group.</p>"""
    parameter_apply_status: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
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
