"""Generated from Smithy shape ``com.amazonaws.finspacedata#CreateDatasetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_finspace_data.errors import DeserializationError

if TYPE_CHECKING:
    import capo_finspace_data.types.alias_string
    import capo_finspace_data.types.client_token
    import capo_finspace_data.types.dataset_description
    import capo_finspace_data.types.dataset_kind
    import capo_finspace_data.types.dataset_owner_info
    import capo_finspace_data.types.dataset_title
    import capo_finspace_data.types.permission_group_params
    import capo_finspace_data.types.schema_union


class CreateDatasetRequest(TypedDict, closed=True):
    client_token: NotRequired["capo_finspace_data.types.client_token.ClientToken"]
    """<p>A token that ensures idempotency. This token expires in 10 minutes.</p>"""
    dataset_title: "capo_finspace_data.types.dataset_title.DatasetTitle"
    """<p>Display title for a FinSpace Dataset.</p>"""
    kind: "capo_finspace_data.types.dataset_kind.DatasetKind"
    """<p>The format in which Dataset data is structured.</p> <ul> <li> <p> <code>TABULAR</code> – Data is structured in a tabular format.</p> </li> <li> <p> <code>NON_TABULAR</code> – Data is structured in a non-tabular format.</p> </li> </ul>"""
    dataset_description: NotRequired[
        "capo_finspace_data.types.dataset_description.DatasetDescription"
    ]
    """<p>Description of a Dataset.</p>"""
    owner_info: NotRequired[
        "capo_finspace_data.types.dataset_owner_info.DatasetOwnerInfo"
    ]
    """<p>Contact information for a Dataset owner.</p>"""
    permission_group_params: (
        "capo_finspace_data.types.permission_group_params.PermissionGroupParams"
    )
    """<p>Permission group parameters for Dataset permissions.</p>"""
    alias: NotRequired["capo_finspace_data.types.alias_string.AliasString"]
    """<p>The unique resource identifier for a Dataset.</p>"""
    schema_definition: NotRequired["capo_finspace_data.types.schema_union.SchemaUnion"]
    """<p>Definition for a schema on a tabular Dataset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDatasetRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    out["datasetTitle"] = value["dataset_title"]
    import capo_finspace_data.types.dataset_kind

    out["kind"] = capo_finspace_data.types.dataset_kind.serialize_json(value["kind"])
    if "dataset_description" in value:
        out["datasetDescription"] = value["dataset_description"]
    if "owner_info" in value:
        import capo_finspace_data.types.dataset_owner_info

        out["ownerInfo"] = capo_finspace_data.types.dataset_owner_info.serialize_json(
            value["owner_info"]
        )
    import capo_finspace_data.types.permission_group_params

    out["permissionGroupParams"] = (
        capo_finspace_data.types.permission_group_params.serialize_json(
            value["permission_group_params"]
        )
    )
    if "alias" in value:
        out["alias"] = value["alias"]
    if "schema_definition" in value:
        import capo_finspace_data.types.schema_union

        out["schemaDefinition"] = capo_finspace_data.types.schema_union.serialize_json(
            value["schema_definition"]
        )
    return out


def deserialize_json(data: dict) -> CreateDatasetRequest:
    out: CreateDatasetRequest = {}  # type: ignore[typeddict-item]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "datasetTitle" in data:
        out["dataset_title"] = data["datasetTitle"]
    else:
        raise DeserializationError("CreateDatasetRequest.dataset_title required")
    if "kind" in data:
        import capo_finspace_data.types.dataset_kind

        out["kind"] = capo_finspace_data.types.dataset_kind.deserialize_json(
            data["kind"]
        )
    else:
        raise DeserializationError("CreateDatasetRequest.kind required")
    if "datasetDescription" in data:
        out["dataset_description"] = data["datasetDescription"]
    if "ownerInfo" in data:
        import capo_finspace_data.types.dataset_owner_info

        out["owner_info"] = (
            capo_finspace_data.types.dataset_owner_info.deserialize_json(
                data["ownerInfo"]
            )
        )
    if "permissionGroupParams" in data:
        import capo_finspace_data.types.permission_group_params

        out["permission_group_params"] = (
            capo_finspace_data.types.permission_group_params.deserialize_json(
                data["permissionGroupParams"]
            )
        )
    else:
        raise DeserializationError(
            "CreateDatasetRequest.permission_group_params required"
        )
    if "alias" in data:
        out["alias"] = data["alias"]
    if "schemaDefinition" in data:
        import capo_finspace_data.types.schema_union

        out["schema_definition"] = (
            capo_finspace_data.types.schema_union.deserialize_json(
                data["schemaDefinition"]
            )
        )
    return out
