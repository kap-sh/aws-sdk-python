"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ExportingLocation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.s3_exporting_location


class ExportingLocation(TypedDict):
    s3_exporting: NotRequired[
        "aws_sdk_customer_profiles.types.s3_exporting_location.S3ExportingLocation"
    ]
    """<p>Information about the S3 location where Identity Resolution Jobs write result files.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExportingLocation) -> dict:
    out: dict = {}
    if "s3_exporting" in value:
        import aws_sdk_customer_profiles.types.s3_exporting_location

        out["S3Exporting"] = (
            aws_sdk_customer_profiles.types.s3_exporting_location.serialize_json(
                value["s3_exporting"]
            )
        )
    return out


def deserialize_json(data: dict) -> ExportingLocation:
    out: ExportingLocation = {}  # type: ignore[typeddict-item]
    if "S3Exporting" in data:
        import aws_sdk_customer_profiles.types.s3_exporting_location

        out["s3_exporting"] = (
            aws_sdk_customer_profiles.types.s3_exporting_location.deserialize_json(
                data["S3Exporting"]
            )
        )
    return out
