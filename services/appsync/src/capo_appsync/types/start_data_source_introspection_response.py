"""Generated from Smithy shape ``com.amazonaws.appsync#StartDataSourceIntrospectionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appsync.types.data_source_introspection_status
    import capo_appsync.types.string


class StartDataSourceIntrospectionResponse(TypedDict, closed=True):
    introspection_id: NotRequired["capo_appsync.types.string.String"]
    """<p>The introspection ID. Each introspection contains a unique ID that can be used to reference the instrospection record.</p>"""
    introspection_status: NotRequired[
        "capo_appsync.types.data_source_introspection_status.DataSourceIntrospectionStatus"
    ]
    """<p>The status of the introspection during creation. By default, when a new instrospection has been created, the status will be set to <code>PROCESSING</code>. Once the operation has been completed, the status will change to <code>SUCCESS</code> or <code>FAILED</code> depending on how the data was parsed. A <code>FAILED</code> operation will return an error and its details as an <code>introspectionStatusDetail</code>.</p>"""
    introspection_status_detail: NotRequired["capo_appsync.types.string.String"]
    """<p>The error detail field. When a <code>FAILED</code> <code>introspectionStatus</code> is returned, the <code>introspectionStatusDetail</code> will also return the exact error that was generated during the operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartDataSourceIntrospectionResponse) -> dict:
    out: dict = {}
    if "introspection_id" in value:
        out["introspectionId"] = value["introspection_id"]
    if "introspection_status" in value:
        import capo_appsync.types.data_source_introspection_status

        out["introspectionStatus"] = (
            capo_appsync.types.data_source_introspection_status.serialize_json(
                value["introspection_status"]
            )
        )
    if "introspection_status_detail" in value:
        out["introspectionStatusDetail"] = value["introspection_status_detail"]
    return out


def deserialize_json(data: dict) -> StartDataSourceIntrospectionResponse:
    out: StartDataSourceIntrospectionResponse = {}  # type: ignore[typeddict-item]
    if "introspectionId" in data:
        out["introspection_id"] = data["introspectionId"]
    if "introspectionStatus" in data:
        import capo_appsync.types.data_source_introspection_status

        out["introspection_status"] = (
            capo_appsync.types.data_source_introspection_status.deserialize_json(
                data["introspectionStatus"]
            )
        )
    if "introspectionStatusDetail" in data:
        out["introspection_status_detail"] = data["introspectionStatusDetail"]
    return out
