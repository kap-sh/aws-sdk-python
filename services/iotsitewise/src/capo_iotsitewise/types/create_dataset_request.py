"""Generated from Smithy shape ``com.amazonaws.iotsitewise#CreateDatasetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.client_token
    import capo_iotsitewise.types.dataset_source
    import capo_iotsitewise.types.id
    import capo_iotsitewise.types.restricted_description
    import capo_iotsitewise.types.restricted_name
    import capo_iotsitewise.types.tag_map


class CreateDatasetRequest(TypedDict, closed=True):
    dataset_id: NotRequired["capo_iotsitewise.types.id.ID"]
    """<p>The ID of the dataset.</p>"""
    dataset_name: "capo_iotsitewise.types.restricted_name.RestrictedName"
    """<p>The name of the dataset.</p>"""
    dataset_description: NotRequired[
        "capo_iotsitewise.types.restricted_description.RestrictedDescription"
    ]
    """<p>A description about the dataset, and its functionality.</p>"""
    dataset_source: "capo_iotsitewise.types.dataset_source.DatasetSource"
    """<p>The data source for the dataset.</p>"""
    client_token: NotRequired["capo_iotsitewise.types.client_token.ClientToken"]
    """<p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>"""
    tags: NotRequired["capo_iotsitewise.types.tag_map.TagMap"]
    r"""<p>A list of key-value pairs that contain metadata for the access policy. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/tag-resources.html\">Tagging your IoT SiteWise resources</a> in the <i>IoT SiteWise User Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDatasetRequest) -> dict:
    out: dict = {}
    if "dataset_id" in value:
        out["datasetId"] = value["dataset_id"]
    out["datasetName"] = value["dataset_name"]
    if "dataset_description" in value:
        out["datasetDescription"] = value["dataset_description"]
    import capo_iotsitewise.types.dataset_source

    out["datasetSource"] = capo_iotsitewise.types.dataset_source.serialize_json(
        value["dataset_source"]
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "tags" in value:
        import capo_iotsitewise.types.tag_map

        out["tags"] = capo_iotsitewise.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateDatasetRequest:
    out: CreateDatasetRequest = {}  # type: ignore[typeddict-item]
    if "datasetId" in data:
        out["dataset_id"] = data["datasetId"]
    if "datasetName" in data:
        out["dataset_name"] = data["datasetName"]
    else:
        raise DeserializationError("CreateDatasetRequest.dataset_name required")
    if "datasetDescription" in data:
        out["dataset_description"] = data["datasetDescription"]
    if "datasetSource" in data:
        import capo_iotsitewise.types.dataset_source

        out["dataset_source"] = capo_iotsitewise.types.dataset_source.deserialize_json(
            data["datasetSource"]
        )
    else:
        raise DeserializationError("CreateDatasetRequest.dataset_source required")
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "tags" in data:
        import capo_iotsitewise.types.tag_map

        out["tags"] = capo_iotsitewise.types.tag_map.deserialize_json(data["tags"])
    return out
