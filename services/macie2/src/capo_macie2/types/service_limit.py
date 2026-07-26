"""Generated from Smithy shape ``com.amazonaws.macie2#ServiceLimit``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_macie2.types.__boolean
    import capo_macie2.types.__long
    import capo_macie2.types.unit


class ServiceLimit(TypedDict, closed=True):
    is_service_limited: NotRequired["capo_macie2.types.__boolean.__boolean"]
    """<p>Specifies whether the account has met the quota that corresponds to the metric specified by the UsageByAccount.type field in the response.</p>"""
    unit: NotRequired["capo_macie2.types.unit.Unit"]
    """<p>The unit of measurement for the value specified by the value field.</p>"""
    value: NotRequired["capo_macie2.types.__long.__long"]
    """<p>The value for the metric specified by the UsageByAccount.type field in the response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceLimit) -> dict:
    out: dict = {}
    if "is_service_limited" in value:
        out["isServiceLimited"] = value["is_service_limited"]
    if "unit" in value:
        import capo_macie2.types.unit

        out["unit"] = capo_macie2.types.unit.serialize_json(value["unit"])
    if "value" in value:
        out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> ServiceLimit:
    out: ServiceLimit = {}  # type: ignore[typeddict-item]
    if "isServiceLimited" in data:
        out["is_service_limited"] = data["isServiceLimited"]
    if "unit" in data:
        import capo_macie2.types.unit

        out["unit"] = capo_macie2.types.unit.deserialize_json(data["unit"])
    if "value" in data:
        out["value"] = data["value"]
    return out
