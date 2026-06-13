"""Generated from Smithy shape ``com.amazonaws.snowdevicemanagement#SoftwareInformation``."""

from typing import TypedDict

from typing_extensions import NotRequired


class SoftwareInformation(TypedDict):
    installed_version: NotRequired["str"]
    """<p>The version of the software currently installed on the device.</p>"""
    installing_version: NotRequired["str"]
    """<p>The version of the software being installed on the device.</p>"""
    install_state: NotRequired["str"]
    """<p>The state of the software that is installed or that is being installed on the device.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SoftwareInformation) -> dict:
    out: dict = {}
    if "installed_version" in value:
        out["installedVersion"] = value["installed_version"]
    if "installing_version" in value:
        out["installingVersion"] = value["installing_version"]
    if "install_state" in value:
        out["installState"] = value["install_state"]
    return out


def deserialize_json(data: dict) -> SoftwareInformation:
    out: SoftwareInformation = {}  # type: ignore[typeddict-item]
    if "installedVersion" in data:
        out["installed_version"] = data["installedVersion"]
    if "installingVersion" in data:
        out["installing_version"] = data["installingVersion"]
    if "installState" in data:
        out["install_state"] = data["installState"]
    return out
