"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ExportingLocation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.s3_exporting_location


class ExportingLocation(TypedDict, closed=True):
    s3_exporting: NotRequired[
        "capo_customer_profiles.types.s3_exporting_location.S3ExportingLocation"
    ]
    """<p>Information about the S3 location where Identity Resolution Jobs write result files.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExportingLocation) -> dict:
    out: dict = {}
    if "s3_exporting" in value:
        import capo_customer_profiles.types.s3_exporting_location

        out["S3Exporting"] = (
            capo_customer_profiles.types.s3_exporting_location.serialize_json(
                value["s3_exporting"]
            )
        )
    return out


def deserialize_json(data: dict) -> ExportingLocation:
    out: ExportingLocation = {}  # type: ignore[typeddict-item]
    if "S3Exporting" in data:
        import capo_customer_profiles.types.s3_exporting_location

        out["s3_exporting"] = (
            capo_customer_profiles.types.s3_exporting_location.deserialize_json(
                data["S3Exporting"]
            )
        )
    return out
