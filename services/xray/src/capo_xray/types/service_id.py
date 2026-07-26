"""Generated from Smithy shape ``com.amazonaws.xray#ServiceId``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_xray.types.service_names
    import capo_xray.types.string


class ServiceId(TypedDict, closed=True):
    name: NotRequired["capo_xray.types.string.String"]
    """<p></p>"""
    names: NotRequired["capo_xray.types.service_names.ServiceNames"]
    """<p></p>"""
    account_id: NotRequired["capo_xray.types.string.String"]
    """<p></p>"""
    type: NotRequired["capo_xray.types.string.String"]
    """<p></p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceId) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "names" in value:
        import capo_xray.types.service_names

        out["Names"] = capo_xray.types.service_names.serialize_json(value["names"])
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "type" in value:
        out["Type"] = value["type"]
    return out


def deserialize_json(data: dict) -> ServiceId:
    out: ServiceId = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Names" in data:
        import capo_xray.types.service_names

        out["names"] = capo_xray.types.service_names.deserialize_json(data["Names"])
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    if "Type" in data:
        out["type"] = data["Type"]
    return out
