"""Generated from Smithy shape ``com.amazonaws.datasync#UpdateLocationFsxOpenZfsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_datasync.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datasync.types.fsx_protocol
    import capo_datasync.types.location_arn
    import capo_datasync.types.smb_subdirectory


class UpdateLocationFsxOpenZfsRequest(TypedDict, closed=True):
    location_arn: "capo_datasync.types.location_arn.LocationArn"
    """<p>Specifies the Amazon Resource Name (ARN) of the FSx for OpenZFS transfer location that you're updating.</p>"""
    protocol: NotRequired["capo_datasync.types.fsx_protocol.FsxProtocol"]
    subdirectory: NotRequired["capo_datasync.types.smb_subdirectory.SmbSubdirectory"]
    """<p>Specifies a subdirectory in the location's path that must begin with <code>/fsx</code>. DataSync uses this subdirectory to read or write data (depending on whether the file system is a source or destination location).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateLocationFsxOpenZfsRequest) -> dict:
    out: dict = {}
    out["LocationArn"] = value["location_arn"]
    if "protocol" in value:
        import capo_datasync.types.fsx_protocol

        out["Protocol"] = capo_datasync.types.fsx_protocol.serialize_aws_json_1_1(
            value["protocol"]
        )
    if "subdirectory" in value:
        out["Subdirectory"] = value["subdirectory"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateLocationFsxOpenZfsRequest:
    out: UpdateLocationFsxOpenZfsRequest = {}  # type: ignore[typeddict-item]
    if "LocationArn" in data:
        out["location_arn"] = data["LocationArn"]
    else:
        raise DeserializationError(
            "UpdateLocationFsxOpenZfsRequest.location_arn required"
        )
    if "Protocol" in data:
        import capo_datasync.types.fsx_protocol

        out["protocol"] = capo_datasync.types.fsx_protocol.deserialize_aws_json_1_1(
            data["Protocol"]
        )
    if "Subdirectory" in data:
        out["subdirectory"] = data["Subdirectory"]
    return out
