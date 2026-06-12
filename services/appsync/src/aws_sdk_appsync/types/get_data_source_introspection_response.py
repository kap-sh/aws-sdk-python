"""Generated from Smithy shape ``com.amazonaws.appsync#GetDataSourceIntrospectionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appsync.types.data_source_introspection_result
    import aws_sdk_appsync.types.data_source_introspection_status
    import aws_sdk_appsync.types.string


class GetDataSourceIntrospectionResponse(TypedDict):
    introspection_id: NotRequired["aws_sdk_appsync.types.string.String"]
    """<p>The introspection ID. Each introspection contains a unique ID that can be used to reference the instrospection record.</p>"""
    introspection_status: NotRequired[
        "aws_sdk_appsync.types.data_source_introspection_status.DataSourceIntrospectionStatus"
    ]
    """<p>The status of the introspection during retrieval. By default, when a new instrospection is being retrieved, the status will be set to <code>PROCESSING</code>. Once the operation has been completed, the status will change to <code>SUCCESS</code> or <code>FAILED</code> depending on how the data was parsed. A <code>FAILED</code> operation will return an error and its details as an <code>introspectionStatusDetail</code>.</p>"""
    introspection_status_detail: NotRequired["aws_sdk_appsync.types.string.String"]
    """<p>The error detail field. When a <code>FAILED</code> <code>introspectionStatus</code> is returned, the <code>introspectionStatusDetail</code> will also return the exact error that was generated during the operation.</p>"""
    introspection_result: NotRequired[
        "aws_sdk_appsync.types.data_source_introspection_result.DataSourceIntrospectionResult"
    ]
    """<p>The <code>DataSourceIntrospectionResult</code> object data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDataSourceIntrospectionResponse) -> dict:
    out: dict = {}
    if "introspection_id" in value:
        out["introspectionId"] = value["introspection_id"]
    if "introspection_status" in value:
        import aws_sdk_appsync.types.data_source_introspection_status

        out["introspectionStatus"] = (
            aws_sdk_appsync.types.data_source_introspection_status.serialize_json(
                value["introspection_status"]
            )
        )
    if "introspection_status_detail" in value:
        out["introspectionStatusDetail"] = value["introspection_status_detail"]
    if "introspection_result" in value:
        import aws_sdk_appsync.types.data_source_introspection_result

        out["introspectionResult"] = (
            aws_sdk_appsync.types.data_source_introspection_result.serialize_json(
                value["introspection_result"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetDataSourceIntrospectionResponse:
    out: GetDataSourceIntrospectionResponse = {}  # type: ignore[typeddict-item]
    if "introspectionId" in data:
        out["introspection_id"] = data["introspectionId"]
    if "introspectionStatus" in data:
        import aws_sdk_appsync.types.data_source_introspection_status

        out["introspection_status"] = (
            aws_sdk_appsync.types.data_source_introspection_status.deserialize_json(
                data["introspectionStatus"]
            )
        )
    if "introspectionStatusDetail" in data:
        out["introspection_status_detail"] = data["introspectionStatusDetail"]
    if "introspectionResult" in data:
        import aws_sdk_appsync.types.data_source_introspection_result

        out["introspection_result"] = (
            aws_sdk_appsync.types.data_source_introspection_result.deserialize_json(
                data["introspectionResult"]
            )
        )
    return out
