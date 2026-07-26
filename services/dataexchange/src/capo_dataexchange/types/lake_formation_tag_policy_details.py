"""Generated from Smithy shape ``com.amazonaws.dataexchange#LakeFormationTagPolicyDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dataexchange.types.__string


class LakeFormationTagPolicyDetails(TypedDict, closed=True):
    database: NotRequired["capo_dataexchange.types.__string.__string"]
    """<p>The underlying Glue database that the notification is referring to.</p>"""
    table: NotRequired["capo_dataexchange.types.__string.__string"]
    """<p>The underlying Glue table that the notification is referring to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LakeFormationTagPolicyDetails) -> dict:
    out: dict = {}
    if "database" in value:
        out["Database"] = value["database"]
    if "table" in value:
        out["Table"] = value["table"]
    return out


def deserialize_json(data: dict) -> LakeFormationTagPolicyDetails:
    out: LakeFormationTagPolicyDetails = {}  # type: ignore[typeddict-item]
    if "Database" in data:
        out["database"] = data["Database"]
    if "Table" in data:
        out["table"] = data["Table"]
    return out
