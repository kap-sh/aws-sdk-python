"""Generated from Smithy shape ``com.amazonaws.appsync#CreateDataSourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appsync.types.data_source


class CreateDataSourceResponse(TypedDict, closed=True):
    data_source: NotRequired["capo_appsync.types.data_source.DataSource"]
    """<p>The <code>DataSource</code> object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDataSourceResponse) -> dict:
    out: dict = {}
    if "data_source" in value:
        import capo_appsync.types.data_source

        out["dataSource"] = capo_appsync.types.data_source.serialize_json(
            value["data_source"]
        )
    return out


def deserialize_json(data: dict) -> CreateDataSourceResponse:
    out: CreateDataSourceResponse = {}  # type: ignore[typeddict-item]
    if "dataSource" in data:
        import capo_appsync.types.data_source

        out["data_source"] = capo_appsync.types.data_source.deserialize_json(
            data["dataSource"]
        )
    return out
