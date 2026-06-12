"""Generated from Smithy shape ``com.amazonaws.kendra#IndexConfigurationSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kendra.types.index_edition
    import aws_sdk_kendra.types.index_id
    import aws_sdk_kendra.types.index_name
    import aws_sdk_kendra.types.index_status
    import aws_sdk_kendra.types.timestamp


class IndexConfigurationSummary(TypedDict):
    name: NotRequired["aws_sdk_kendra.types.index_name.IndexName"]
    """<p>The name of the index.</p>"""
    id: NotRequired["aws_sdk_kendra.types.index_id.IndexId"]
    """<p>A identifier for the index. Use this to identify the index when you are using APIs such as <code>Query</code>, <code>DescribeIndex</code>, <code>UpdateIndex</code>, and <code>DeleteIndex</code>.</p>"""
    edition: NotRequired["aws_sdk_kendra.types.index_edition.IndexEdition"]
    """<p>Indicates whether the index is a Enterprise Edition index or a Developer Edition index. </p>"""
    created_at: "aws_sdk_kendra.types.timestamp.Timestamp"
    """<p>The Unix timestamp when the index was created.</p>"""
    updated_at: "aws_sdk_kendra.types.timestamp.Timestamp"
    """<p>The Unix timestamp when the index was last updated.</p>"""
    status: "aws_sdk_kendra.types.index_status.IndexStatus"
    """<p>The current status of the index. When the status is <code>ACTIVE</code>, the index is ready to search.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IndexConfigurationSummary) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "id" in value:
        out["Id"] = value["id"]
    if "edition" in value:
        import aws_sdk_kendra.types.index_edition

        out["Edition"] = aws_sdk_kendra.types.index_edition.serialize_aws_json_1_1(
            value["edition"]
        )
    import aws_sdk_kendra.types.timestamp

    out["CreatedAt"] = aws_sdk_kendra.types.timestamp.serialize_aws_json_1_1(
        value["created_at"]
    )
    import aws_sdk_kendra.types.timestamp

    out["UpdatedAt"] = aws_sdk_kendra.types.timestamp.serialize_aws_json_1_1(
        value["updated_at"]
    )
    import aws_sdk_kendra.types.index_status

    out["Status"] = aws_sdk_kendra.types.index_status.serialize_aws_json_1_1(
        value["status"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> IndexConfigurationSummary:
    out: IndexConfigurationSummary = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Edition" in data:
        import aws_sdk_kendra.types.index_edition

        out["edition"] = aws_sdk_kendra.types.index_edition.deserialize_aws_json_1_1(
            data["Edition"]
        )
    if "CreatedAt" in data:
        import aws_sdk_kendra.types.timestamp

        out["created_at"] = aws_sdk_kendra.types.timestamp.deserialize_aws_json_1_1(
            data["CreatedAt"]
        )
    else:
        raise DeserializationError("IndexConfigurationSummary.created_at required")
    if "UpdatedAt" in data:
        import aws_sdk_kendra.types.timestamp

        out["updated_at"] = aws_sdk_kendra.types.timestamp.deserialize_aws_json_1_1(
            data["UpdatedAt"]
        )
    else:
        raise DeserializationError("IndexConfigurationSummary.updated_at required")
    if "Status" in data:
        import aws_sdk_kendra.types.index_status

        out["status"] = aws_sdk_kendra.types.index_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    else:
        raise DeserializationError("IndexConfigurationSummary.status required")
    return out
