"""Generated from Smithy shape ``com.amazonaws.appsync#GetDataSourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appsync.types.resource_name
    import aws_sdk_appsync.types.string


class GetDataSourceRequest(TypedDict):
    api_id: "aws_sdk_appsync.types.string.String"
    """<p>The API ID.</p>"""
    name: "aws_sdk_appsync.types.resource_name.ResourceName"
    """<p>The name of the data source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDataSourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDataSourceRequest:
    out: GetDataSourceRequest = {}  # type: ignore[typeddict-item]
    return out
