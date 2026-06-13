"""Generated from Smithy shape ``com.amazonaws.s3tables#UpdateTableMetadataLocationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_s3tables.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_s3tables.types.metadata_location
    import aws_sdk_s3tables.types.namespace_list
    import aws_sdk_s3tables.types.table_arn
    import aws_sdk_s3tables.types.table_name
    import aws_sdk_s3tables.types.version_token


class UpdateTableMetadataLocationResponse(TypedDict):
    name: "aws_sdk_s3tables.types.table_name.TableName"
    """<p>The name of the table.</p>"""
    table_arn: "aws_sdk_s3tables.types.table_arn.TableARN"
    """<p>The Amazon Resource Name (ARN) of the table.</p>"""
    namespace: "aws_sdk_s3tables.types.namespace_list.NamespaceList"
    """<p>The namespace the table is associated with.</p>"""
    version_token: "aws_sdk_s3tables.types.version_token.VersionToken"
    """<p>The version token of the table.</p>"""
    metadata_location: "aws_sdk_s3tables.types.metadata_location.MetadataLocation"
    """<p>The metadata location of the table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateTableMetadataLocationResponse) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["tableARN"] = value["table_arn"]
    import aws_sdk_s3tables.types.namespace_list

    out["namespace"] = aws_sdk_s3tables.types.namespace_list.serialize_json(
        value["namespace"]
    )
    out["versionToken"] = value["version_token"]
    out["metadataLocation"] = value["metadata_location"]
    return out


def deserialize_json(data: dict) -> UpdateTableMetadataLocationResponse:
    out: UpdateTableMetadataLocationResponse = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("UpdateTableMetadataLocationResponse.name required")
    if "tableARN" in data:
        out["table_arn"] = data["tableARN"]
    else:
        raise DeserializationError(
            "UpdateTableMetadataLocationResponse.table_arn required"
        )
    if "namespace" in data:
        import aws_sdk_s3tables.types.namespace_list

        out["namespace"] = aws_sdk_s3tables.types.namespace_list.deserialize_json(
            data["namespace"]
        )
    else:
        raise DeserializationError(
            "UpdateTableMetadataLocationResponse.namespace required"
        )
    if "versionToken" in data:
        out["version_token"] = data["versionToken"]
    else:
        raise DeserializationError(
            "UpdateTableMetadataLocationResponse.version_token required"
        )
    if "metadataLocation" in data:
        out["metadata_location"] = data["metadataLocation"]
    else:
        raise DeserializationError(
            "UpdateTableMetadataLocationResponse.metadata_location required"
        )
    return out
