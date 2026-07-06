"""Generated from Smithy shape ``com.amazonaws.sesv2#PutConfigurationSetVdmOptionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.configuration_set_name
    import aws_sdk_sesv2.types.vdm_options


class PutConfigurationSetVdmOptionsRequest(TypedDict, closed=True):
    configuration_set_name: (
        "aws_sdk_sesv2.types.configuration_set_name.ConfigurationSetName"
    )
    """<p>The name of the configuration set.</p>"""
    vdm_options: NotRequired["aws_sdk_sesv2.types.vdm_options.VdmOptions"]
    """<p>The VDM options to apply to the configuration set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutConfigurationSetVdmOptionsRequest) -> dict:
    out: dict = {}
    if "vdm_options" in value:
        import aws_sdk_sesv2.types.vdm_options

        out["VdmOptions"] = aws_sdk_sesv2.types.vdm_options.serialize_json(
            value["vdm_options"]
        )
    return out


def deserialize_json(data: dict) -> PutConfigurationSetVdmOptionsRequest:
    out: PutConfigurationSetVdmOptionsRequest = {}  # type: ignore[typeddict-item]
    if "VdmOptions" in data:
        import aws_sdk_sesv2.types.vdm_options

        out["vdm_options"] = aws_sdk_sesv2.types.vdm_options.deserialize_json(
            data["VdmOptions"]
        )
    return out
