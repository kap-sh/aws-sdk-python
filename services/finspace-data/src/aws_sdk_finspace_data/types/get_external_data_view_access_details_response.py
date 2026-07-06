"""Generated from Smithy shape ``com.amazonaws.finspacedata#GetExternalDataViewAccessDetailsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_finspace_data.types.aws_credentials
    import aws_sdk_finspace_data.types.s3_location


class GetExternalDataViewAccessDetailsResponse(TypedDict, closed=True):
    credentials: NotRequired[
        "aws_sdk_finspace_data.types.aws_credentials.AwsCredentials"
    ]
    """<p>The credentials required to access the external Dataview from the S3 location.</p>"""
    s3_location: NotRequired["aws_sdk_finspace_data.types.s3_location.S3Location"]
    """<p>The location where the external Dataview is stored.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetExternalDataViewAccessDetailsResponse) -> dict:
    out: dict = {}
    if "credentials" in value:
        import aws_sdk_finspace_data.types.aws_credentials

        out["credentials"] = aws_sdk_finspace_data.types.aws_credentials.serialize_json(
            value["credentials"]
        )
    if "s3_location" in value:
        import aws_sdk_finspace_data.types.s3_location

        out["s3Location"] = aws_sdk_finspace_data.types.s3_location.serialize_json(
            value["s3_location"]
        )
    return out


def deserialize_json(data: dict) -> GetExternalDataViewAccessDetailsResponse:
    out: GetExternalDataViewAccessDetailsResponse = {}  # type: ignore[typeddict-item]
    if "credentials" in data:
        import aws_sdk_finspace_data.types.aws_credentials

        out["credentials"] = (
            aws_sdk_finspace_data.types.aws_credentials.deserialize_json(
                data["credentials"]
            )
        )
    if "s3Location" in data:
        import aws_sdk_finspace_data.types.s3_location

        out["s3_location"] = aws_sdk_finspace_data.types.s3_location.deserialize_json(
            data["s3Location"]
        )
    return out
