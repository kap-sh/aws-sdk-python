"""Generated from Smithy shape ``com.amazonaws.ssm#ResolvedTargets``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.boolean
    import capo_ssm.types.target_parameter_list


class ResolvedTargets(TypedDict, closed=True):
    parameter_values: NotRequired[
        "capo_ssm.types.target_parameter_list.TargetParameterList"
    ]
    """<p>A list of parameter values sent to targets that resolved during the Automation execution.</p>"""
    truncated: "capo_ssm.types.boolean.Boolean"
    """<p>A boolean value indicating whether the resolved target list is truncated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResolvedTargets) -> dict:
    out: dict = {}
    if "parameter_values" in value:
        import capo_ssm.types.target_parameter_list

        out["ParameterValues"] = (
            capo_ssm.types.target_parameter_list.serialize_aws_json_1_1(
                value["parameter_values"]
            )
        )
    out["Truncated"] = value.get("truncated", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> ResolvedTargets:
    out: ResolvedTargets = {}  # type: ignore[typeddict-item]
    if "ParameterValues" in data:
        import capo_ssm.types.target_parameter_list

        out["parameter_values"] = (
            capo_ssm.types.target_parameter_list.deserialize_aws_json_1_1(
                data["ParameterValues"]
            )
        )
    if "Truncated" in data:
        out["truncated"] = data["Truncated"]
    else:
        out["truncated"] = False
    return out
