"""Generated from Smithy shape ``com.amazonaws.appsync#DeleteDataSourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appsync.types.resource_name
    import aws_sdk_appsync.types.string


class DeleteDataSourceRequest(TypedDict):
    api_id: "aws_sdk_appsync.types.string.String"
    """<p>The API ID.</p>"""
    name: "aws_sdk_appsync.types.resource_name.ResourceName"
    """<p>The name of the data source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDataSourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteDataSourceRequest:
    out: DeleteDataSourceRequest = {}  # type: ignore[typeddict-item]
    return out
