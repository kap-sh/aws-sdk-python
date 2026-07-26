"""Generated from Smithy shape ``com.amazonaws.quicksight#PerformanceConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.unique_key_list


class PerformanceConfiguration(TypedDict, closed=True):
    unique_keys: NotRequired["capo_quicksight.types.unique_key_list.UniqueKeyList"]
    """<p>A <code>UniqueKey</code> configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PerformanceConfiguration) -> dict:
    out: dict = {}
    if "unique_keys" in value:
        import capo_quicksight.types.unique_key_list

        out["UniqueKeys"] = capo_quicksight.types.unique_key_list.serialize_json(
            value["unique_keys"]
        )
    return out


def deserialize_json(data: dict) -> PerformanceConfiguration:
    out: PerformanceConfiguration = {}  # type: ignore[typeddict-item]
    if "UniqueKeys" in data:
        import capo_quicksight.types.unique_key_list

        out["unique_keys"] = capo_quicksight.types.unique_key_list.deserialize_json(
            data["UniqueKeys"]
        )
    return out
