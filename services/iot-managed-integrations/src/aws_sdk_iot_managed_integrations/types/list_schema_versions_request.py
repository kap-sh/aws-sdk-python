"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#ListSchemaVersionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.max_results
    import aws_sdk_iot_managed_integrations.types.next_token
    import aws_sdk_iot_managed_integrations.types.schema_id
    import aws_sdk_iot_managed_integrations.types.schema_version_namespace_name
    import aws_sdk_iot_managed_integrations.types.schema_version_type
    import aws_sdk_iot_managed_integrations.types.schema_version_version
    import aws_sdk_iot_managed_integrations.types.schema_version_visibility


class ListSchemaVersionsRequest(TypedDict, closed=True):
    type: "aws_sdk_iot_managed_integrations.types.schema_version_type.SchemaVersionType"
    """<p>Filter on the type of schema version.</p>"""
    max_results: NotRequired[
        "aws_sdk_iot_managed_integrations.types.max_results.MaxResults"
    ]
    """<p>The maximum number of results to return at one time.</p>"""
    next_token: NotRequired[
        "aws_sdk_iot_managed_integrations.types.next_token.NextToken"
    ]
    """<p>A token that can be used to retrieve the next set of results.</p>"""
    schema_id: NotRequired["aws_sdk_iot_managed_integrations.types.schema_id.SchemaId"]
    """<p>Filter on the id of the schema version.</p>"""
    namespace: NotRequired[
        "aws_sdk_iot_managed_integrations.types.schema_version_namespace_name.SchemaVersionNamespaceName"
    ]
    """<p>Filter on the name of the schema version.</p>"""
    visibility: NotRequired[
        "aws_sdk_iot_managed_integrations.types.schema_version_visibility.SchemaVersionVisibility"
    ]
    """<p>The visibility of the schema version.</p>"""
    semantic_version: NotRequired[
        "aws_sdk_iot_managed_integrations.types.schema_version_version.SchemaVersionVersion"
    ]
    """<p>The schema version. If this is left blank, it defaults to the latest version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSchemaVersionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListSchemaVersionsRequest:
    out: ListSchemaVersionsRequest = {}  # type: ignore[typeddict-item]
    return out
