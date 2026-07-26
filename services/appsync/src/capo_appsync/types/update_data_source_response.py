"""Generated from Smithy shape ``com.amazonaws.appsync#UpdateDataSourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appsync.types.data_source


class UpdateDataSourceResponse(TypedDict, closed=True):
    data_source: NotRequired["capo_appsync.types.data_source.DataSource"]
    """<p>The updated <code>DataSource</code> object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDataSourceResponse) -> dict:
    out: dict = {}
    if "data_source" in value:
        import capo_appsync.types.data_source

        out["dataSource"] = capo_appsync.types.data_source.serialize_json(
            value["data_source"]
        )
    return out


def deserialize_json(data: dict) -> UpdateDataSourceResponse:
    out: UpdateDataSourceResponse = {}  # type: ignore[typeddict-item]
    if "dataSource" in data:
        import capo_appsync.types.data_source

        out["data_source"] = capo_appsync.types.data_source.deserialize_json(
            data["dataSource"]
        )
    return out
