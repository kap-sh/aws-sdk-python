"""Generated from Smithy shape ``com.amazonaws.ssm#MaintenanceWindowTaskParameterValueExpression``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.maintenance_window_task_parameter_value_list


class MaintenanceWindowTaskParameterValueExpression(TypedDict, closed=True):
    values: NotRequired[
        "capo_ssm.types.maintenance_window_task_parameter_value_list.MaintenanceWindowTaskParameterValueList"
    ]
    """<p>This field contains an array of 0 or more strings, each 1 to 255 characters in length.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: MaintenanceWindowTaskParameterValueExpression,
) -> dict:
    out: dict = {}
    if "values" in value:
        import capo_ssm.types.maintenance_window_task_parameter_value_list

        out["Values"] = (
            capo_ssm.types.maintenance_window_task_parameter_value_list.serialize_aws_json_1_1(
                value["values"]
            )
        )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> MaintenanceWindowTaskParameterValueExpression:
    out: MaintenanceWindowTaskParameterValueExpression = {}  # type: ignore[typeddict-item]
    if "Values" in data:
        import capo_ssm.types.maintenance_window_task_parameter_value_list

        out["values"] = (
            capo_ssm.types.maintenance_window_task_parameter_value_list.deserialize_aws_json_1_1(
                data["Values"]
            )
        )
    return out
