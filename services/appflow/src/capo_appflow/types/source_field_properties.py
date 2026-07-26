"""Generated from Smithy shape ``com.amazonaws.appflow#SourceFieldProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_appflow.types.boolean


class SourceFieldProperties(TypedDict, closed=True):
    is_retrievable: "capo_appflow.types.boolean.Boolean"
    """<p> Indicates whether the field can be returned in a search result. </p>"""
    is_queryable: "capo_appflow.types.boolean.Boolean"
    """<p> Indicates if the field can be queried. </p>"""
    is_timestamp_field_for_incremental_queries: "capo_appflow.types.boolean.Boolean"
    """<p>Indicates if this timestamp field can be used for incremental queries.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SourceFieldProperties) -> dict:
    out: dict = {}
    out["isRetrievable"] = value.get("is_retrievable", False)
    out["isQueryable"] = value.get("is_queryable", False)
    out["isTimestampFieldForIncrementalQueries"] = value.get(
        "is_timestamp_field_for_incremental_queries", False
    )
    return out


def deserialize_json(data: dict) -> SourceFieldProperties:
    out: SourceFieldProperties = {}  # type: ignore[typeddict-item]
    if "isRetrievable" in data:
        out["is_retrievable"] = data["isRetrievable"]
    else:
        out["is_retrievable"] = False
    if "isQueryable" in data:
        out["is_queryable"] = data["isQueryable"]
    else:
        out["is_queryable"] = False
    if "isTimestampFieldForIncrementalQueries" in data:
        out["is_timestamp_field_for_incremental_queries"] = data[
            "isTimestampFieldForIncrementalQueries"
        ]
    else:
        out["is_timestamp_field_for_incremental_queries"] = False
    return out
