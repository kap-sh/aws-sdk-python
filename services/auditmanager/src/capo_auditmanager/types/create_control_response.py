"""Generated from Smithy shape ``com.amazonaws.auditmanager#CreateControlResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_auditmanager.types.control


class CreateControlResponse(TypedDict, closed=True):
    control: NotRequired["capo_auditmanager.types.control.Control"]
    """<p> The new control that the <code>CreateControl</code> API returned. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateControlResponse) -> dict:
    out: dict = {}
    if "control" in value:
        import capo_auditmanager.types.control

        out["control"] = capo_auditmanager.types.control.serialize_json(
            value["control"]
        )
    return out


def deserialize_json(data: dict) -> CreateControlResponse:
    out: CreateControlResponse = {}  # type: ignore[typeddict-item]
    if "control" in data:
        import capo_auditmanager.types.control

        out["control"] = capo_auditmanager.types.control.deserialize_json(
            data["control"]
        )
    return out
