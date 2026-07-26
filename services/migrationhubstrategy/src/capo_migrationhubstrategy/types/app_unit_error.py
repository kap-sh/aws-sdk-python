"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#AppUnitError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_migrationhubstrategy.types.app_unit_error_category


class AppUnitError(TypedDict, closed=True):
    app_unit_error_category: NotRequired[
        "capo_migrationhubstrategy.types.app_unit_error_category.AppUnitErrorCategory"
    ]
    """<p>The category of the error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AppUnitError) -> dict:
    out: dict = {}
    if "app_unit_error_category" in value:
        out["appUnitErrorCategory"] = value["app_unit_error_category"]
    return out


def deserialize_json(data: dict) -> AppUnitError:
    out: AppUnitError = {}  # type: ignore[typeddict-item]
    if "appUnitErrorCategory" in data:
        out["app_unit_error_category"] = data["appUnitErrorCategory"]
    return out
