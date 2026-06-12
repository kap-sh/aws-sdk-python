"""Generated from Smithy shape ``com.amazonaws.opensearch#UpdateDataSourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_opensearch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.data_source_description
    import aws_sdk_opensearch.types.data_source_name
    import aws_sdk_opensearch.types.data_source_status
    import aws_sdk_opensearch.types.data_source_type
    import aws_sdk_opensearch.types.domain_name


class UpdateDataSourceRequest(TypedDict):
    domain_name: "aws_sdk_opensearch.types.domain_name.DomainName"
    """<p>The name of the domain.</p>"""
    name: "aws_sdk_opensearch.types.data_source_name.DataSourceName"
    """<p>The name of the data source to modify.</p>"""
    data_source_type: "aws_sdk_opensearch.types.data_source_type.DataSourceType"
    """<p>The type of data source.</p>"""
    description: NotRequired[
        "aws_sdk_opensearch.types.data_source_description.DataSourceDescription"
    ]
    """<p>A new description of the data source.</p>"""
    status: NotRequired["aws_sdk_opensearch.types.data_source_status.DataSourceStatus"]
    """<p>The status of the data source update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDataSourceRequest) -> dict:
    out: dict = {}
    import aws_sdk_opensearch.types.data_source_type

    out["DataSourceType"] = aws_sdk_opensearch.types.data_source_type.serialize_json(
        value["data_source_type"]
    )
    if "description" in value:
        out["Description"] = value["description"]
    if "status" in value:
        import aws_sdk_opensearch.types.data_source_status

        out["Status"] = aws_sdk_opensearch.types.data_source_status.serialize_json(
            value["status"]
        )
    return out


def deserialize_json(data: dict) -> UpdateDataSourceRequest:
    out: UpdateDataSourceRequest = {}  # type: ignore[typeddict-item]
    if "DataSourceType" in data:
        import aws_sdk_opensearch.types.data_source_type

        out["data_source_type"] = (
            aws_sdk_opensearch.types.data_source_type.deserialize_json(
                data["DataSourceType"]
            )
        )
    else:
        raise DeserializationError("UpdateDataSourceRequest.data_source_type required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "Status" in data:
        import aws_sdk_opensearch.types.data_source_status

        out["status"] = aws_sdk_opensearch.types.data_source_status.deserialize_json(
            data["Status"]
        )
    return out
