"""Generated from Smithy shape ``com.amazonaws.xray#TraceUser``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_xray.types.service_ids
    import capo_xray.types.string


class TraceUser(TypedDict, closed=True):
    user_name: NotRequired["capo_xray.types.string.String"]
    """<p>The user's name.</p>"""
    service_ids: NotRequired["capo_xray.types.service_ids.ServiceIds"]
    """<p>Services that the user's request hit.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TraceUser) -> dict:
    out: dict = {}
    if "user_name" in value:
        out["UserName"] = value["user_name"]
    if "service_ids" in value:
        import capo_xray.types.service_ids

        out["ServiceIds"] = capo_xray.types.service_ids.serialize_json(
            value["service_ids"]
        )
    return out


def deserialize_json(data: dict) -> TraceUser:
    out: TraceUser = {}  # type: ignore[typeddict-item]
    if "UserName" in data:
        out["user_name"] = data["UserName"]
    if "ServiceIds" in data:
        import capo_xray.types.service_ids

        out["service_ids"] = capo_xray.types.service_ids.deserialize_json(
            data["ServiceIds"]
        )
    return out
