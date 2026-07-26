"""Generated from Smithy shape ``com.amazonaws.iotsitewise#UpdatePortalResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.portal_status


class UpdatePortalResponse(TypedDict, closed=True):
    portal_status: "capo_iotsitewise.types.portal_status.PortalStatus"
    """<p>The status of the portal, which contains a state (<code>UPDATING</code> after successfully calling this operation) and any error message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePortalResponse) -> dict:
    out: dict = {}
    import capo_iotsitewise.types.portal_status

    out["portalStatus"] = capo_iotsitewise.types.portal_status.serialize_json(
        value["portal_status"]
    )
    return out


def deserialize_json(data: dict) -> UpdatePortalResponse:
    out: UpdatePortalResponse = {}  # type: ignore[typeddict-item]
    if "portalStatus" in data:
        import capo_iotsitewise.types.portal_status

        out["portal_status"] = capo_iotsitewise.types.portal_status.deserialize_json(
            data["portalStatus"]
        )
    else:
        raise DeserializationError("UpdatePortalResponse.portal_status required")
    return out
