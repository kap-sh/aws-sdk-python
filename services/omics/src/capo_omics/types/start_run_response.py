"""Generated from Smithy shape ``com.amazonaws.omics#StartRunResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_omics.types.configuration_details
    import capo_omics.types.run_arn
    import capo_omics.types.run_id
    import capo_omics.types.run_output_uri
    import capo_omics.types.run_status
    import capo_omics.types.run_uuid
    import capo_omics.types.tag_map


class StartRunResponse(TypedDict, closed=True):
    arn: NotRequired["capo_omics.types.run_arn.RunArn"]
    """<p>Unique resource identifier for the run.</p>"""
    id: NotRequired["capo_omics.types.run_id.RunId"]
    """<p>The run's ID.</p>"""
    status: NotRequired["capo_omics.types.run_status.RunStatus"]
    """<p>The run's status.</p>"""
    tags: NotRequired["capo_omics.types.tag_map.TagMap"]
    """<p>The run's tags.</p>"""
    uuid: NotRequired["capo_omics.types.run_uuid.RunUuid"]
    """<p>The universally unique identifier for a run.</p>"""
    run_output_uri: NotRequired["capo_omics.types.run_output_uri.RunOutputUri"]
    """<p>The destination for workflow outputs.</p>"""
    configuration: NotRequired[
        "capo_omics.types.configuration_details.ConfigurationDetails"
    ]
    """<p>Configuration details for the workflow run.</p>"""
    networking_mode: NotRequired["str"]
    """<p>Networking mode for the workflow run.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartRunResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "id" in value:
        out["id"] = value["id"]
    if "status" in value:
        out["status"] = value["status"]
    if "tags" in value:
        import capo_omics.types.tag_map

        out["tags"] = capo_omics.types.tag_map.serialize_json(value["tags"])
    if "uuid" in value:
        out["uuid"] = value["uuid"]
    if "run_output_uri" in value:
        out["runOutputUri"] = value["run_output_uri"]
    if "configuration" in value:
        import capo_omics.types.configuration_details

        out["configuration"] = capo_omics.types.configuration_details.serialize_json(
            value["configuration"]
        )
    if "networking_mode" in value:
        out["networkingMode"] = value["networking_mode"]
    return out


def deserialize_json(data: dict) -> StartRunResponse:
    out: StartRunResponse = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "id" in data:
        out["id"] = data["id"]
    if "status" in data:
        out["status"] = data["status"]
    if "tags" in data:
        import capo_omics.types.tag_map

        out["tags"] = capo_omics.types.tag_map.deserialize_json(data["tags"])
    if "uuid" in data:
        out["uuid"] = data["uuid"]
    if "runOutputUri" in data:
        out["run_output_uri"] = data["runOutputUri"]
    if "configuration" in data:
        import capo_omics.types.configuration_details

        out["configuration"] = capo_omics.types.configuration_details.deserialize_json(
            data["configuration"]
        )
    if "networkingMode" in data:
        out["networking_mode"] = data["networkingMode"]
    return out
