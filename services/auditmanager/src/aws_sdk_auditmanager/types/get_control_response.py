"""Generated from Smithy shape ``com.amazonaws.auditmanager#GetControlResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.control


class GetControlResponse(TypedDict, closed=True):
    control: NotRequired["aws_sdk_auditmanager.types.control.Control"]
    """<p> The details of the control that the <code>GetControl</code> API returned. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetControlResponse) -> dict:
    out: dict = {}
    if "control" in value:
        import aws_sdk_auditmanager.types.control

        out["control"] = aws_sdk_auditmanager.types.control.serialize_json(
            value["control"]
        )
    return out


def deserialize_json(data: dict) -> GetControlResponse:
    out: GetControlResponse = {}  # type: ignore[typeddict-item]
    if "control" in data:
        import aws_sdk_auditmanager.types.control

        out["control"] = aws_sdk_auditmanager.types.control.deserialize_json(
            data["control"]
        )
    return out
