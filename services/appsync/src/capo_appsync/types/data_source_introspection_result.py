"""Generated from Smithy shape ``com.amazonaws.appsync#DataSourceIntrospectionResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appsync.types.data_source_introspection_models
    import capo_appsync.types.pagination_token


class DataSourceIntrospectionResult(TypedDict, closed=True):
    models: NotRequired[
        "capo_appsync.types.data_source_introspection_models.DataSourceIntrospectionModels"
    ]
    """<p>The array of <code>DataSourceIntrospectionModel</code> objects.</p>"""
    next_token: NotRequired["capo_appsync.types.pagination_token.PaginationToken"]
    """<p>Determines the number of types to be returned in a single response before paginating. This value is typically taken from <code>nextToken</code> value from the previous response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataSourceIntrospectionResult) -> dict:
    out: dict = {}
    if "models" in value:
        import capo_appsync.types.data_source_introspection_models

        out["models"] = (
            capo_appsync.types.data_source_introspection_models.serialize_json(
                value["models"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> DataSourceIntrospectionResult:
    out: DataSourceIntrospectionResult = {}  # type: ignore[typeddict-item]
    if "models" in data:
        import capo_appsync.types.data_source_introspection_models

        out["models"] = (
            capo_appsync.types.data_source_introspection_models.deserialize_json(
                data["models"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
