"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#GeneralFlagsV4``."""

from typing import TypedDict

from typing_extensions import NotRequired


class GeneralFlagsV4(TypedDict):
    auto_enrollment: NotRequired["bool"]
    """<p>Allows certificate issuance using autoenrollment. Set to TRUE to allow autoenrollment.</p>"""
    machine_type: NotRequired["bool"]
    """<p>Defines if the template is for machines or users. Set to TRUE if the template is for machines. Set to FALSE if the template is for users</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GeneralFlagsV4) -> dict:
    out: dict = {}
    if "auto_enrollment" in value:
        out["AutoEnrollment"] = value["auto_enrollment"]
    if "machine_type" in value:
        out["MachineType"] = value["machine_type"]
    return out


def deserialize_json(data: dict) -> GeneralFlagsV4:
    out: GeneralFlagsV4 = {}  # type: ignore[typeddict-item]
    if "AutoEnrollment" in data:
        out["auto_enrollment"] = data["AutoEnrollment"]
    if "MachineType" in data:
        out["machine_type"] = data["MachineType"]
    return out
