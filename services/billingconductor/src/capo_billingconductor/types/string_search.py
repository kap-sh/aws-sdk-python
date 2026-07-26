"""Generated from Smithy shape ``com.amazonaws.billingconductor#StringSearch``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_billingconductor.errors import DeserializationError

if TYPE_CHECKING:
    import capo_billingconductor.types.search_option
    import capo_billingconductor.types.search_value


class StringSearch(TypedDict, closed=True):
    search_option: "capo_billingconductor.types.search_option.SearchOption"
    """<p> The search option to be applied when performing the string search. </p>"""
    search_value: "capo_billingconductor.types.search_value.SearchValue"
    """<p> The value to search for within the specified string field. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StringSearch) -> dict:
    out: dict = {}
    import capo_billingconductor.types.search_option

    out["SearchOption"] = capo_billingconductor.types.search_option.serialize_json(
        value["search_option"]
    )
    out["SearchValue"] = value["search_value"]
    return out


def deserialize_json(data: dict) -> StringSearch:
    out: StringSearch = {}  # type: ignore[typeddict-item]
    if "SearchOption" in data:
        import capo_billingconductor.types.search_option

        out["search_option"] = (
            capo_billingconductor.types.search_option.deserialize_json(
                data["SearchOption"]
            )
        )
    else:
        raise DeserializationError("StringSearch.search_option required")
    if "SearchValue" in data:
        out["search_value"] = data["SearchValue"]
    else:
        raise DeserializationError("StringSearch.search_value required")
    return out
