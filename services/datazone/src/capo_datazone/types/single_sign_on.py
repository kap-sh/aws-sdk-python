"""Generated from Smithy shape ``com.amazonaws.datazone#SingleSignOn``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.auth_type
    import capo_datazone.types.user_assignment


class SingleSignOn(TypedDict, closed=True):
    type: NotRequired["capo_datazone.types.auth_type.AuthType"]
    """<p>The type of single sign-on in Amazon DataZone.</p>"""
    user_assignment: NotRequired["capo_datazone.types.user_assignment.UserAssignment"]
    """<p>The single sign-on user assignment in Amazon DataZone.</p>"""
    idc_instance_arn: NotRequired["str"]
    """<p>The ARN of the IDC instance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SingleSignOn) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_datazone.types.auth_type

        out["type"] = capo_datazone.types.auth_type.serialize_json(value["type"])
    if "user_assignment" in value:
        import capo_datazone.types.user_assignment

        out["userAssignment"] = capo_datazone.types.user_assignment.serialize_json(
            value["user_assignment"]
        )
    if "idc_instance_arn" in value:
        out["idcInstanceArn"] = value["idc_instance_arn"]
    return out


def deserialize_json(data: dict) -> SingleSignOn:
    out: SingleSignOn = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import capo_datazone.types.auth_type

        out["type"] = capo_datazone.types.auth_type.deserialize_json(data["type"])
    if "userAssignment" in data:
        import capo_datazone.types.user_assignment

        out["user_assignment"] = capo_datazone.types.user_assignment.deserialize_json(
            data["userAssignment"]
        )
    if "idcInstanceArn" in data:
        out["idc_instance_arn"] = data["idcInstanceArn"]
    return out
