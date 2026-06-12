"""Generated from Smithy shape ``com.amazonaws.finspacedata#Dataset``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_finspace_data.types.alias_string
    import aws_sdk_finspace_data.types.dataset_arn
    import aws_sdk_finspace_data.types.dataset_description
    import aws_sdk_finspace_data.types.dataset_id
    import aws_sdk_finspace_data.types.dataset_kind
    import aws_sdk_finspace_data.types.dataset_owner_info
    import aws_sdk_finspace_data.types.dataset_title
    import aws_sdk_finspace_data.types.schema_union
    import aws_sdk_finspace_data.types.timestamp_epoch


class Dataset(TypedDict):
    dataset_id: NotRequired["aws_sdk_finspace_data.types.dataset_id.DatasetId"]
    """<p>An identifier for a Dataset.</p>"""
    dataset_arn: NotRequired["aws_sdk_finspace_data.types.dataset_arn.DatasetArn"]
    """<p>The ARN identifier of the Dataset.</p>"""
    dataset_title: NotRequired["aws_sdk_finspace_data.types.dataset_title.DatasetTitle"]
    """<p>Display title for a Dataset.</p>"""
    kind: NotRequired["aws_sdk_finspace_data.types.dataset_kind.DatasetKind"]
    """<p>The format in which Dataset data is structured.</p> <ul> <li> <p> <code>TABULAR</code> – Data is structured in a tabular format.</p> </li> <li> <p> <code>NON_TABULAR</code> – Data is structured in a non-tabular format.</p> </li> </ul>"""
    dataset_description: NotRequired[
        "aws_sdk_finspace_data.types.dataset_description.DatasetDescription"
    ]
    """<p>Description for a Dataset.</p>"""
    owner_info: NotRequired[
        "aws_sdk_finspace_data.types.dataset_owner_info.DatasetOwnerInfo"
    ]
    """<p>Contact information for a Dataset owner.</p>"""
    create_time: "aws_sdk_finspace_data.types.timestamp_epoch.TimestampEpoch"
    """<p>The timestamp at which the Dataset was created in FinSpace. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.</p>"""
    last_modified_time: "aws_sdk_finspace_data.types.timestamp_epoch.TimestampEpoch"
    """<p>The last time that the Dataset was modified. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.</p>"""
    schema_definition: NotRequired[
        "aws_sdk_finspace_data.types.schema_union.SchemaUnion"
    ]
    """<p>Definition for a schema on a tabular Dataset.</p>"""
    alias: NotRequired["aws_sdk_finspace_data.types.alias_string.AliasString"]
    """<p>The unique resource identifier for a Dataset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Dataset) -> dict:
    out: dict = {}
    if "dataset_id" in value:
        out["datasetId"] = value["dataset_id"]
    if "dataset_arn" in value:
        out["datasetArn"] = value["dataset_arn"]
    if "dataset_title" in value:
        out["datasetTitle"] = value["dataset_title"]
    if "kind" in value:
        import aws_sdk_finspace_data.types.dataset_kind

        out["kind"] = aws_sdk_finspace_data.types.dataset_kind.serialize_json(
            value["kind"]
        )
    if "dataset_description" in value:
        out["datasetDescription"] = value["dataset_description"]
    if "owner_info" in value:
        import aws_sdk_finspace_data.types.dataset_owner_info

        out["ownerInfo"] = (
            aws_sdk_finspace_data.types.dataset_owner_info.serialize_json(
                value["owner_info"]
            )
        )
    out["createTime"] = value.get("create_time", 0)
    out["lastModifiedTime"] = value.get("last_modified_time", 0)
    if "schema_definition" in value:
        import aws_sdk_finspace_data.types.schema_union

        out["schemaDefinition"] = (
            aws_sdk_finspace_data.types.schema_union.serialize_json(
                value["schema_definition"]
            )
        )
    if "alias" in value:
        out["alias"] = value["alias"]
    return out


def deserialize_json(data: dict) -> Dataset:
    out: Dataset = {}  # type: ignore[typeddict-item]
    if "datasetId" in data:
        out["dataset_id"] = data["datasetId"]
    if "datasetArn" in data:
        out["dataset_arn"] = data["datasetArn"]
    if "datasetTitle" in data:
        out["dataset_title"] = data["datasetTitle"]
    if "kind" in data:
        import aws_sdk_finspace_data.types.dataset_kind

        out["kind"] = aws_sdk_finspace_data.types.dataset_kind.deserialize_json(
            data["kind"]
        )
    if "datasetDescription" in data:
        out["dataset_description"] = data["datasetDescription"]
    if "ownerInfo" in data:
        import aws_sdk_finspace_data.types.dataset_owner_info

        out["owner_info"] = (
            aws_sdk_finspace_data.types.dataset_owner_info.deserialize_json(
                data["ownerInfo"]
            )
        )
    if "createTime" in data:
        out["create_time"] = data["createTime"]
    else:
        out["create_time"] = 0
    if "lastModifiedTime" in data:
        out["last_modified_time"] = data["lastModifiedTime"]
    else:
        out["last_modified_time"] = 0
    if "schemaDefinition" in data:
        import aws_sdk_finspace_data.types.schema_union

        out["schema_definition"] = (
            aws_sdk_finspace_data.types.schema_union.deserialize_json(
                data["schemaDefinition"]
            )
        )
    if "alias" in data:
        out["alias"] = data["alias"]
    return out
