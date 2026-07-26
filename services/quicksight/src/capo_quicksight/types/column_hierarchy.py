"""Generated from Smithy shape ``com.amazonaws.quicksight#ColumnHierarchy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.date_time_hierarchy
    import capo_quicksight.types.explicit_hierarchy
    import capo_quicksight.types.predefined_hierarchy


class ColumnHierarchy(TypedDict, closed=True):
    explicit_hierarchy: NotRequired[
        "capo_quicksight.types.explicit_hierarchy.ExplicitHierarchy"
    ]
    """<p>The option that determines the hierarchy of the fields that are built within a visual's field wells. These fields can't be duplicated to other visuals.</p>"""
    date_time_hierarchy: NotRequired[
        "capo_quicksight.types.date_time_hierarchy.DateTimeHierarchy"
    ]
    """<p>The option that determines the hierarchy of any <code>DateTime</code> fields.</p>"""
    predefined_hierarchy: NotRequired[
        "capo_quicksight.types.predefined_hierarchy.PredefinedHierarchy"
    ]
    """<p>The option that determines the hierarchy of the fields that are defined during data preparation. These fields are available to use in any analysis that uses the data source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ColumnHierarchy) -> dict:
    out: dict = {}
    if "explicit_hierarchy" in value:
        import capo_quicksight.types.explicit_hierarchy

        out["ExplicitHierarchy"] = (
            capo_quicksight.types.explicit_hierarchy.serialize_json(
                value["explicit_hierarchy"]
            )
        )
    if "date_time_hierarchy" in value:
        import capo_quicksight.types.date_time_hierarchy

        out["DateTimeHierarchy"] = (
            capo_quicksight.types.date_time_hierarchy.serialize_json(
                value["date_time_hierarchy"]
            )
        )
    if "predefined_hierarchy" in value:
        import capo_quicksight.types.predefined_hierarchy

        out["PredefinedHierarchy"] = (
            capo_quicksight.types.predefined_hierarchy.serialize_json(
                value["predefined_hierarchy"]
            )
        )
    return out


def deserialize_json(data: dict) -> ColumnHierarchy:
    out: ColumnHierarchy = {}  # type: ignore[typeddict-item]
    if "ExplicitHierarchy" in data:
        import capo_quicksight.types.explicit_hierarchy

        out["explicit_hierarchy"] = (
            capo_quicksight.types.explicit_hierarchy.deserialize_json(
                data["ExplicitHierarchy"]
            )
        )
    if "DateTimeHierarchy" in data:
        import capo_quicksight.types.date_time_hierarchy

        out["date_time_hierarchy"] = (
            capo_quicksight.types.date_time_hierarchy.deserialize_json(
                data["DateTimeHierarchy"]
            )
        )
    if "PredefinedHierarchy" in data:
        import capo_quicksight.types.predefined_hierarchy

        out["predefined_hierarchy"] = (
            capo_quicksight.types.predefined_hierarchy.deserialize_json(
                data["PredefinedHierarchy"]
            )
        )
    return out
