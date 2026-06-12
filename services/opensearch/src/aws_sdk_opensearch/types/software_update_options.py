"""Generated from Smithy shape ``com.amazonaws.opensearch#SoftwareUpdateOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.boolean


class SoftwareUpdateOptions(TypedDict):
    auto_software_update_enabled: NotRequired[
        "aws_sdk_opensearch.types.boolean.Boolean"
    ]
    """<p>Whether automatic service software updates are enabled for the domain.</p>"""
    use_latest_service_software_for_blue_green: NotRequired[
        "aws_sdk_opensearch.types.boolean.Boolean"
    ]
    """<p>Whether the domain should use the latest service software version during a blue/green deployment. If enabled, the domain will automatically use the latest available service software when a blue/green deployment is triggered.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SoftwareUpdateOptions) -> dict:
    out: dict = {}
    if "auto_software_update_enabled" in value:
        out["AutoSoftwareUpdateEnabled"] = value["auto_software_update_enabled"]
    if "use_latest_service_software_for_blue_green" in value:
        out["UseLatestServiceSoftwareForBlueGreen"] = value[
            "use_latest_service_software_for_blue_green"
        ]
    return out


def deserialize_json(data: dict) -> SoftwareUpdateOptions:
    out: SoftwareUpdateOptions = {}  # type: ignore[typeddict-item]
    if "AutoSoftwareUpdateEnabled" in data:
        out["auto_software_update_enabled"] = data["AutoSoftwareUpdateEnabled"]
    if "UseLatestServiceSoftwareForBlueGreen" in data:
        out["use_latest_service_software_for_blue_green"] = data[
            "UseLatestServiceSoftwareForBlueGreen"
        ]
    return out
