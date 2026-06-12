"""Generated from Smithy shape ``com.amazonaws.auditmanager#UpdateControlResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.control


class UpdateControlResponse(TypedDict):
    control: NotRequired["aws_sdk_auditmanager.types.control.Control"]
    """<p> The name of the updated control set that the <code>UpdateControl</code> API returned. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateControlResponse) -> dict:
    out: dict = {}
    if "control" in value:
        import aws_sdk_auditmanager.types.control

        out["control"] = aws_sdk_auditmanager.types.control.serialize_json(
            value["control"]
        )
    return out


def deserialize_json(data: dict) -> UpdateControlResponse:
    out: UpdateControlResponse = {}  # type: ignore[typeddict-item]
    if "control" in data:
        import aws_sdk_auditmanager.types.control

        out["control"] = aws_sdk_auditmanager.types.control.deserialize_json(
            data["control"]
        )
    return out
