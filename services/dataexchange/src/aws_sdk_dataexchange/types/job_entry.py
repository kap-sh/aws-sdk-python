"""Generated from Smithy shape ``com.amazonaws.dataexchange#JobEntry``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_dataexchange.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_dataexchange.types.arn
    import aws_sdk_dataexchange.types.asset_configuration
    import aws_sdk_dataexchange.types.id
    import aws_sdk_dataexchange.types.list_of_job_error
    import aws_sdk_dataexchange.types.response_details
    import aws_sdk_dataexchange.types.state
    import aws_sdk_dataexchange.types.timestamp
    import aws_sdk_dataexchange.types.type


class JobEntry(TypedDict):
    arn: "aws_sdk_dataexchange.types.arn.Arn"
    """<p>The ARN for the job.</p>"""
    asset_configuration: NotRequired[
        "aws_sdk_dataexchange.types.asset_configuration.AssetConfiguration"
    ]
    """<p>The configuration for the asset, including tags applied to assets created by the job.</p>"""
    created_at: "aws_sdk_dataexchange.types.timestamp.Timestamp"
    """<p>The date and time that the job was created, in ISO 8601 format.</p>"""
    details: "aws_sdk_dataexchange.types.response_details.ResponseDetails"
    """<p>Details of the operation to be performed by the job, such as export destination details or import source details.</p>"""
    errors: NotRequired["aws_sdk_dataexchange.types.list_of_job_error.ListOfJobError"]
    """<p>Errors for jobs.</p>"""
    id: "aws_sdk_dataexchange.types.id.Id"
    """<p>The unique identifier for the job.</p>"""
    state: "aws_sdk_dataexchange.types.state.State"
    """<p>The state of the job.</p>"""
    type: "aws_sdk_dataexchange.types.type.Type"
    """<p>The job type.</p>"""
    updated_at: "aws_sdk_dataexchange.types.timestamp.Timestamp"
    """<p>The date and time that the job was last updated, in ISO 8601 format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobEntry) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    if "asset_configuration" in value:
        import aws_sdk_dataexchange.types.asset_configuration

        out["AssetConfiguration"] = (
            aws_sdk_dataexchange.types.asset_configuration.serialize_json(
                value["asset_configuration"]
            )
        )
    import aws_sdk_dataexchange.types.timestamp

    out["CreatedAt"] = aws_sdk_dataexchange.types.timestamp.serialize_json(
        value["created_at"]
    )
    import aws_sdk_dataexchange.types.response_details

    out["Details"] = aws_sdk_dataexchange.types.response_details.serialize_json(
        value["details"]
    )
    if "errors" in value:
        import aws_sdk_dataexchange.types.list_of_job_error

        out["Errors"] = aws_sdk_dataexchange.types.list_of_job_error.serialize_json(
            value["errors"]
        )
    out["Id"] = value["id"]
    out["State"] = value["state"]
    out["Type"] = value["type"]
    import aws_sdk_dataexchange.types.timestamp

    out["UpdatedAt"] = aws_sdk_dataexchange.types.timestamp.serialize_json(
        value["updated_at"]
    )
    return out


def deserialize_json(data: dict) -> JobEntry:
    out: JobEntry = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("JobEntry.arn required")
    if "AssetConfiguration" in data:
        import aws_sdk_dataexchange.types.asset_configuration

        out["asset_configuration"] = (
            aws_sdk_dataexchange.types.asset_configuration.deserialize_json(
                data["AssetConfiguration"]
            )
        )
    if "CreatedAt" in data:
        import aws_sdk_dataexchange.types.timestamp

        out["created_at"] = aws_sdk_dataexchange.types.timestamp.deserialize_json(
            data["CreatedAt"]
        )
    else:
        raise DeserializationError("JobEntry.created_at required")
    if "Details" in data:
        import aws_sdk_dataexchange.types.response_details

        out["details"] = aws_sdk_dataexchange.types.response_details.deserialize_json(
            data["Details"]
        )
    else:
        raise DeserializationError("JobEntry.details required")
    if "Errors" in data:
        import aws_sdk_dataexchange.types.list_of_job_error

        out["errors"] = aws_sdk_dataexchange.types.list_of_job_error.deserialize_json(
            data["Errors"]
        )
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("JobEntry.id required")
    if "State" in data:
        out["state"] = data["State"]
    else:
        raise DeserializationError("JobEntry.state required")
    if "Type" in data:
        out["type"] = data["Type"]
    else:
        raise DeserializationError("JobEntry.type required")
    if "UpdatedAt" in data:
        import aws_sdk_dataexchange.types.timestamp

        out["updated_at"] = aws_sdk_dataexchange.types.timestamp.deserialize_json(
            data["UpdatedAt"]
        )
    else:
        raise DeserializationError("JobEntry.updated_at required")
    return out
