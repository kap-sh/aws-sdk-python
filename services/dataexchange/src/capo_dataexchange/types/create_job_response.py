"""Generated from Smithy shape ``com.amazonaws.dataexchange#CreateJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dataexchange.types.arn
    import capo_dataexchange.types.asset_configuration
    import capo_dataexchange.types.id
    import capo_dataexchange.types.list_of_job_error
    import capo_dataexchange.types.response_details
    import capo_dataexchange.types.state
    import capo_dataexchange.types.timestamp
    import capo_dataexchange.types.type


class CreateJobResponse(TypedDict, closed=True):
    arn: NotRequired["capo_dataexchange.types.arn.Arn"]
    """<p>The ARN for the job.</p>"""
    asset_configuration: NotRequired[
        "capo_dataexchange.types.asset_configuration.AssetConfiguration"
    ]
    """<p>The configuration for the asset, including tags applied to assets created by the job.</p>"""
    created_at: NotRequired["capo_dataexchange.types.timestamp.Timestamp"]
    """<p>The date and time that the job was created, in ISO 8601 format.</p>"""
    details: NotRequired["capo_dataexchange.types.response_details.ResponseDetails"]
    """<p>Details about the job.</p>"""
    errors: NotRequired["capo_dataexchange.types.list_of_job_error.ListOfJobError"]
    """<p>The errors associated with jobs.</p>"""
    id: NotRequired["capo_dataexchange.types.id.Id"]
    """<p>The unique identifier for the job.</p>"""
    state: NotRequired["capo_dataexchange.types.state.State"]
    """<p>The state of the job.</p>"""
    type: NotRequired["capo_dataexchange.types.type.Type"]
    """<p>The job type.</p>"""
    updated_at: NotRequired["capo_dataexchange.types.timestamp.Timestamp"]
    """<p>The date and time that the job was last updated, in ISO 8601 format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateJobResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "asset_configuration" in value:
        import capo_dataexchange.types.asset_configuration

        out["AssetConfiguration"] = (
            capo_dataexchange.types.asset_configuration.serialize_json(
                value["asset_configuration"]
            )
        )
    if "created_at" in value:
        import capo_dataexchange.types.timestamp

        out["CreatedAt"] = capo_dataexchange.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "details" in value:
        import capo_dataexchange.types.response_details

        out["Details"] = capo_dataexchange.types.response_details.serialize_json(
            value["details"]
        )
    if "errors" in value:
        import capo_dataexchange.types.list_of_job_error

        out["Errors"] = capo_dataexchange.types.list_of_job_error.serialize_json(
            value["errors"]
        )
    if "id" in value:
        out["Id"] = value["id"]
    if "state" in value:
        out["State"] = value["state"]
    if "type" in value:
        out["Type"] = value["type"]
    if "updated_at" in value:
        import capo_dataexchange.types.timestamp

        out["UpdatedAt"] = capo_dataexchange.types.timestamp.serialize_json(
            value["updated_at"]
        )
    return out


def deserialize_json(data: dict) -> CreateJobResponse:
    out: CreateJobResponse = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "AssetConfiguration" in data:
        import capo_dataexchange.types.asset_configuration

        out["asset_configuration"] = (
            capo_dataexchange.types.asset_configuration.deserialize_json(
                data["AssetConfiguration"]
            )
        )
    if "CreatedAt" in data:
        import capo_dataexchange.types.timestamp

        out["created_at"] = capo_dataexchange.types.timestamp.deserialize_json(
            data["CreatedAt"]
        )
    if "Details" in data:
        import capo_dataexchange.types.response_details

        out["details"] = capo_dataexchange.types.response_details.deserialize_json(
            data["Details"]
        )
    if "Errors" in data:
        import capo_dataexchange.types.list_of_job_error

        out["errors"] = capo_dataexchange.types.list_of_job_error.deserialize_json(
            data["Errors"]
        )
    if "Id" in data:
        out["id"] = data["Id"]
    if "State" in data:
        out["state"] = data["State"]
    if "Type" in data:
        out["type"] = data["Type"]
    if "UpdatedAt" in data:
        import capo_dataexchange.types.timestamp

        out["updated_at"] = capo_dataexchange.types.timestamp.deserialize_json(
            data["UpdatedAt"]
        )
    return out
