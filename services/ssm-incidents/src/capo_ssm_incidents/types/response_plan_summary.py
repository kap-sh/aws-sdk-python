"""Generated from Smithy shape ``com.amazonaws.ssmincidents#ResponsePlanSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ssm_incidents.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ssm_incidents.types.arn
    import capo_ssm_incidents.types.response_plan_display_name
    import capo_ssm_incidents.types.response_plan_name


class ResponsePlanSummary(TypedDict, closed=True):
    arn: "capo_ssm_incidents.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the response plan.</p>"""
    name: "capo_ssm_incidents.types.response_plan_name.ResponsePlanName"
    """<p>The name of the response plan. This can't include spaces.</p>"""
    display_name: NotRequired[
        "capo_ssm_incidents.types.response_plan_display_name.ResponsePlanDisplayName"
    ]
    """<p>The human readable name of the response plan. This can include spaces.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResponsePlanSummary) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["name"] = value["name"]
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    return out


def deserialize_json(data: dict) -> ResponsePlanSummary:
    out: ResponsePlanSummary = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("ResponsePlanSummary.arn required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("ResponsePlanSummary.name required")
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    return out
