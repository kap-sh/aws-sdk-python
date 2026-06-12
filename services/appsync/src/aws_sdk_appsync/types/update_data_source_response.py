"""Generated from Smithy shape ``com.amazonaws.appsync#UpdateDataSourceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appsync.types.data_source


class UpdateDataSourceResponse(TypedDict):
    data_source: NotRequired["aws_sdk_appsync.types.data_source.DataSource"]
    """<p>The updated <code>DataSource</code> object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDataSourceResponse) -> dict:
    out: dict = {}
    if "data_source" in value:
        import aws_sdk_appsync.types.data_source

        out["dataSource"] = aws_sdk_appsync.types.data_source.serialize_json(
            value["data_source"]
        )
    return out


def deserialize_json(data: dict) -> UpdateDataSourceResponse:
    out: UpdateDataSourceResponse = {}  # type: ignore[typeddict-item]
    if "dataSource" in data:
        import aws_sdk_appsync.types.data_source

        out["data_source"] = aws_sdk_appsync.types.data_source.deserialize_json(
            data["dataSource"]
        )
    return out
