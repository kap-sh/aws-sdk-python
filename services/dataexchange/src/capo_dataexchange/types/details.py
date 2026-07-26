"""Generated from Smithy shape ``com.amazonaws.dataexchange#Details``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dataexchange.types.import_asset_from_signed_url_job_error_details
    import capo_dataexchange.types.list_of_asset_source_entry


class Details(TypedDict, closed=True):
    import_asset_from_signed_url_job_error_details: NotRequired[
        "capo_dataexchange.types.import_asset_from_signed_url_job_error_details.ImportAssetFromSignedUrlJobErrorDetails"
    ]
    """<p>Information about the job error.</p>"""
    import_assets_from_s3_job_error_details: NotRequired[
        "capo_dataexchange.types.list_of_asset_source_entry.ListOfAssetSourceEntry"
    ]
    """<p>Details about the job error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Details) -> dict:
    out: dict = {}
    if "import_asset_from_signed_url_job_error_details" in value:
        import capo_dataexchange.types.import_asset_from_signed_url_job_error_details

        out["ImportAssetFromSignedUrlJobErrorDetails"] = (
            capo_dataexchange.types.import_asset_from_signed_url_job_error_details.serialize_json(
                value["import_asset_from_signed_url_job_error_details"]
            )
        )
    if "import_assets_from_s3_job_error_details" in value:
        import capo_dataexchange.types.list_of_asset_source_entry

        out["ImportAssetsFromS3JobErrorDetails"] = (
            capo_dataexchange.types.list_of_asset_source_entry.serialize_json(
                value["import_assets_from_s3_job_error_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> Details:
    out: Details = {}  # type: ignore[typeddict-item]
    if "ImportAssetFromSignedUrlJobErrorDetails" in data:
        import capo_dataexchange.types.import_asset_from_signed_url_job_error_details

        out["import_asset_from_signed_url_job_error_details"] = (
            capo_dataexchange.types.import_asset_from_signed_url_job_error_details.deserialize_json(
                data["ImportAssetFromSignedUrlJobErrorDetails"]
            )
        )
    if "ImportAssetsFromS3JobErrorDetails" in data:
        import capo_dataexchange.types.list_of_asset_source_entry

        out["import_assets_from_s3_job_error_details"] = (
            capo_dataexchange.types.list_of_asset_source_entry.deserialize_json(
                data["ImportAssetsFromS3JobErrorDetails"]
            )
        )
    return out
