"""Generated from Smithy shape ``com.amazonaws.datazone#S3PropertiesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datazone.types.connection_status
    import capo_datazone.types.s3_access_grant_location_id
    import capo_datazone.types.s3_uri


class S3PropertiesOutput(TypedDict, closed=True):
    s3_uri: "capo_datazone.types.s3_uri.S3Uri"
    """<p>The Amazon S3 URI that's part of the Amazon S3 properties of a connection.</p>"""
    s3_access_grant_location_id: NotRequired[
        "capo_datazone.types.s3_access_grant_location_id.S3AccessGrantLocationId"
    ]
    """<p>The Amazon S3 Access Grant location ID that's part of the Amazon S3 properties of a connection.</p>"""
    register_s3_access_grant_location: NotRequired["bool"]
    """<p>Specifies whether to register the Amazon S3 Access Grant location.</p>"""
    status: NotRequired["capo_datazone.types.connection_status.ConnectionStatus"]
    """<p>The status of the Amazon S3 connection.</p>"""
    error_message: NotRequired["str"]
    """<p>The error message that gets displayed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3PropertiesOutput) -> dict:
    out: dict = {}
    out["s3Uri"] = value["s3_uri"]
    if "s3_access_grant_location_id" in value:
        out["s3AccessGrantLocationId"] = value["s3_access_grant_location_id"]
    if "register_s3_access_grant_location" in value:
        out["registerS3AccessGrantLocation"] = value[
            "register_s3_access_grant_location"
        ]
    if "status" in value:
        import capo_datazone.types.connection_status

        out["status"] = capo_datazone.types.connection_status.serialize_json(
            value["status"]
        )
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> S3PropertiesOutput:
    out: S3PropertiesOutput = {}  # type: ignore[typeddict-item]
    if "s3Uri" in data:
        out["s3_uri"] = data["s3Uri"]
    else:
        raise DeserializationError("S3PropertiesOutput.s3_uri required")
    if "s3AccessGrantLocationId" in data:
        out["s3_access_grant_location_id"] = data["s3AccessGrantLocationId"]
    if "registerS3AccessGrantLocation" in data:
        out["register_s3_access_grant_location"] = data["registerS3AccessGrantLocation"]
    if "status" in data:
        import capo_datazone.types.connection_status

        out["status"] = capo_datazone.types.connection_status.deserialize_json(
            data["status"]
        )
    if "errorMessage" in data:
        out["error_message"] = data["errorMessage"]
    return out
