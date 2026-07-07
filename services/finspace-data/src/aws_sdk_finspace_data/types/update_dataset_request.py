"""Generated from Smithy shape ``com.amazonaws.finspacedata#UpdateDatasetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_finspace_data.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_finspace_data.types.alias_string
    import aws_sdk_finspace_data.types.client_token
    import aws_sdk_finspace_data.types.dataset_description
    import aws_sdk_finspace_data.types.dataset_id
    import aws_sdk_finspace_data.types.dataset_kind
    import aws_sdk_finspace_data.types.dataset_title
    import aws_sdk_finspace_data.types.schema_union


class UpdateDatasetRequest(TypedDict, closed=True):
    client_token: NotRequired["aws_sdk_finspace_data.types.client_token.ClientToken"]
    """<p>A token that ensures idempotency. This token expires in 10 minutes.</p>"""
    dataset_id: "aws_sdk_finspace_data.types.dataset_id.DatasetId"
    """<p>The unique identifier for the Dataset to update.</p>"""
    dataset_title: "aws_sdk_finspace_data.types.dataset_title.DatasetTitle"
    """<p>A display title for the Dataset.</p>"""
    kind: "aws_sdk_finspace_data.types.dataset_kind.DatasetKind"
    """<p>The format in which the Dataset data is structured.</p> <ul> <li> <p> <code>TABULAR</code> – Data is structured in a tabular format.</p> </li> <li> <p> <code>NON_TABULAR</code> – Data is structured in a non-tabular format.</p> </li> </ul>"""
    dataset_description: NotRequired[
        "aws_sdk_finspace_data.types.dataset_description.DatasetDescription"
    ]
    """<p>A description for the Dataset.</p>"""
    alias: NotRequired["aws_sdk_finspace_data.types.alias_string.AliasString"]
    """<p>The unique resource identifier for a Dataset.</p>"""
    schema_definition: NotRequired[
        "aws_sdk_finspace_data.types.schema_union.SchemaUnion"
    ]
    """<p>Definition for a schema on a tabular Dataset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDatasetRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    out["datasetTitle"] = value["dataset_title"]
    import aws_sdk_finspace_data.types.dataset_kind

    out["kind"] = aws_sdk_finspace_data.types.dataset_kind.serialize_json(value["kind"])
    if "dataset_description" in value:
        out["datasetDescription"] = value["dataset_description"]
    if "alias" in value:
        out["alias"] = value["alias"]
    if "schema_definition" in value:
        import aws_sdk_finspace_data.types.schema_union

        out["schemaDefinition"] = (
            aws_sdk_finspace_data.types.schema_union.serialize_json(
                value["schema_definition"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateDatasetRequest:
    out: UpdateDatasetRequest = {}  # type: ignore[typeddict-item]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "datasetTitle" in data:
        out["dataset_title"] = data["datasetTitle"]
    else:
        raise DeserializationError("UpdateDatasetRequest.dataset_title required")
    if "kind" in data:
        import aws_sdk_finspace_data.types.dataset_kind

        out["kind"] = aws_sdk_finspace_data.types.dataset_kind.deserialize_json(
            data["kind"]
        )
    else:
        raise DeserializationError("UpdateDatasetRequest.kind required")
    if "datasetDescription" in data:
        out["dataset_description"] = data["datasetDescription"]
    if "alias" in data:
        out["alias"] = data["alias"]
    if "schemaDefinition" in data:
        import aws_sdk_finspace_data.types.schema_union

        out["schema_definition"] = (
            aws_sdk_finspace_data.types.schema_union.deserialize_json(
                data["schemaDefinition"]
            )
        )
    return out
