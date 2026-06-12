"""Generated from Smithy shape ``com.amazonaws.opensearch#AddDataSourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_opensearch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.data_source_description
    import aws_sdk_opensearch.types.data_source_name
    import aws_sdk_opensearch.types.data_source_type
    import aws_sdk_opensearch.types.domain_name


class AddDataSourceRequest(TypedDict):
    domain_name: "aws_sdk_opensearch.types.domain_name.DomainName"
    """<p>The name of the domain to add the data source to.</p>"""
    name: "aws_sdk_opensearch.types.data_source_name.DataSourceName"
    """<p>A name for the data source.</p>"""
    data_source_type: "aws_sdk_opensearch.types.data_source_type.DataSourceType"
    """<p>The type of data source.</p>"""
    description: NotRequired[
        "aws_sdk_opensearch.types.data_source_description.DataSourceDescription"
    ]
    """<p>A description of the data source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AddDataSourceRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import aws_sdk_opensearch.types.data_source_type

    out["DataSourceType"] = aws_sdk_opensearch.types.data_source_type.serialize_json(
        value["data_source_type"]
    )
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_json(data: dict) -> AddDataSourceRequest:
    out: AddDataSourceRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("AddDataSourceRequest.name required")
    if "DataSourceType" in data:
        import aws_sdk_opensearch.types.data_source_type

        out["data_source_type"] = (
            aws_sdk_opensearch.types.data_source_type.deserialize_json(
                data["DataSourceType"]
            )
        )
    else:
        raise DeserializationError("AddDataSourceRequest.data_source_type required")
    if "Description" in data:
        out["description"] = data["Description"]
    return out
