"""Generated from Smithy shape ``com.amazonaws.auditmanager#ControlSet``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.control_set_name
    import aws_sdk_auditmanager.types.controls
    import aws_sdk_auditmanager.types.uuid


class ControlSet(TypedDict):
    id: NotRequired["aws_sdk_auditmanager.types.uuid.UUID"]
    """<p> The identifier of the control set in the assessment. This is the control set name in a plain string format. </p>"""
    name: NotRequired["aws_sdk_auditmanager.types.control_set_name.ControlSetName"]
    """<p> The name of the control set. </p>"""
    controls: NotRequired["aws_sdk_auditmanager.types.controls.Controls"]
    """<p> The list of controls within the control set. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ControlSet) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    if "controls" in value:
        import aws_sdk_auditmanager.types.controls

        out["controls"] = aws_sdk_auditmanager.types.controls.serialize_json(
            value["controls"]
        )
    return out


def deserialize_json(data: dict) -> ControlSet:
    out: ControlSet = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "name" in data:
        out["name"] = data["name"]
    if "controls" in data:
        import aws_sdk_auditmanager.types.controls

        out["controls"] = aws_sdk_auditmanager.types.controls.deserialize_json(
            data["controls"]
        )
    return out
