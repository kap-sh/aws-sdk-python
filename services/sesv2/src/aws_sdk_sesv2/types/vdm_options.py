"""Generated from Smithy shape ``com.amazonaws.sesv2#VdmOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.dashboard_options
    import aws_sdk_sesv2.types.guardian_options


class VdmOptions(TypedDict):
    dashboard_options: NotRequired[
        "aws_sdk_sesv2.types.dashboard_options.DashboardOptions"
    ]
    """<p>Specifies additional settings for your VDM configuration as applicable to the Dashboard.</p>"""
    guardian_options: NotRequired[
        "aws_sdk_sesv2.types.guardian_options.GuardianOptions"
    ]
    """<p>Specifies additional settings for your VDM configuration as applicable to the Guardian.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VdmOptions) -> dict:
    out: dict = {}
    if "dashboard_options" in value:
        import aws_sdk_sesv2.types.dashboard_options

        out["DashboardOptions"] = aws_sdk_sesv2.types.dashboard_options.serialize_json(
            value["dashboard_options"]
        )
    if "guardian_options" in value:
        import aws_sdk_sesv2.types.guardian_options

        out["GuardianOptions"] = aws_sdk_sesv2.types.guardian_options.serialize_json(
            value["guardian_options"]
        )
    return out


def deserialize_json(data: dict) -> VdmOptions:
    out: VdmOptions = {}  # type: ignore[typeddict-item]
    if "DashboardOptions" in data:
        import aws_sdk_sesv2.types.dashboard_options

        out["dashboard_options"] = (
            aws_sdk_sesv2.types.dashboard_options.deserialize_json(
                data["DashboardOptions"]
            )
        )
    if "GuardianOptions" in data:
        import aws_sdk_sesv2.types.guardian_options

        out["guardian_options"] = aws_sdk_sesv2.types.guardian_options.deserialize_json(
            data["GuardianOptions"]
        )
    return out
