"""Generated from Smithy shape ``com.amazonaws.sesv2#VdmOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.dashboard_options
    import capo_sesv2.types.guardian_options


class VdmOptions(TypedDict, closed=True):
    dashboard_options: NotRequired[
        "capo_sesv2.types.dashboard_options.DashboardOptions"
    ]
    """<p>Specifies additional settings for your VDM configuration as applicable to the Dashboard.</p>"""
    guardian_options: NotRequired["capo_sesv2.types.guardian_options.GuardianOptions"]
    """<p>Specifies additional settings for your VDM configuration as applicable to the Guardian.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VdmOptions) -> dict:
    out: dict = {}
    if "dashboard_options" in value:
        import capo_sesv2.types.dashboard_options

        out["DashboardOptions"] = capo_sesv2.types.dashboard_options.serialize_json(
            value["dashboard_options"]
        )
    if "guardian_options" in value:
        import capo_sesv2.types.guardian_options

        out["GuardianOptions"] = capo_sesv2.types.guardian_options.serialize_json(
            value["guardian_options"]
        )
    return out


def deserialize_json(data: dict) -> VdmOptions:
    out: VdmOptions = {}  # type: ignore[typeddict-item]
    if "DashboardOptions" in data:
        import capo_sesv2.types.dashboard_options

        out["dashboard_options"] = capo_sesv2.types.dashboard_options.deserialize_json(
            data["DashboardOptions"]
        )
    if "GuardianOptions" in data:
        import capo_sesv2.types.guardian_options

        out["guardian_options"] = capo_sesv2.types.guardian_options.deserialize_json(
            data["GuardianOptions"]
        )
    return out
