"""Generated from Smithy shape ``com.amazonaws.neptunedata#LoaderIdResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_neptunedata.types.string_list


class LoaderIdResult(TypedDict, closed=True):
    load_ids: NotRequired["capo_neptunedata.types.string_list.StringList"]
    """<p>A list of load IDs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LoaderIdResult) -> dict:
    out: dict = {}
    if "load_ids" in value:
        import capo_neptunedata.types.string_list

        out["loadIds"] = capo_neptunedata.types.string_list.serialize_json(
            value["load_ids"]
        )
    return out


def deserialize_json(data: dict) -> LoaderIdResult:
    out: LoaderIdResult = {}  # type: ignore[typeddict-item]
    if "loadIds" in data:
        import capo_neptunedata.types.string_list

        out["load_ids"] = capo_neptunedata.types.string_list.deserialize_json(
            data["loadIds"]
        )
    return out
