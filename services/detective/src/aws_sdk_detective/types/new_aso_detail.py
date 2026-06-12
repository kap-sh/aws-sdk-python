"""Generated from Smithy shape ``com.amazonaws.detective#NewAsoDetail``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_detective.types.aso
    import aws_sdk_detective.types.is_new_for_entire_account


class NewAsoDetail(TypedDict):
    aso: NotRequired["aws_sdk_detective.types.aso.Aso"]
    """<p>Details about the new Autonomous System Organization (ASO).</p>"""
    is_new_for_entire_account: (
        "aws_sdk_detective.types.is_new_for_entire_account.IsNewForEntireAccount"
    )
    """<p>Checks if the Autonomous System Organization (ASO) is new for the entire account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NewAsoDetail) -> dict:
    out: dict = {}
    if "aso" in value:
        out["Aso"] = value["aso"]
    out["IsNewForEntireAccount"] = value.get("is_new_for_entire_account", False)
    return out


def deserialize_json(data: dict) -> NewAsoDetail:
    out: NewAsoDetail = {}  # type: ignore[typeddict-item]
    if "Aso" in data:
        out["aso"] = data["Aso"]
    if "IsNewForEntireAccount" in data:
        out["is_new_for_entire_account"] = data["IsNewForEntireAccount"]
    else:
        out["is_new_for_entire_account"] = False
    return out
