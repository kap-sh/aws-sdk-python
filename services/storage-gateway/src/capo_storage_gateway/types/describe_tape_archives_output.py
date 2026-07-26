"""Generated from Smithy shape ``com.amazonaws.storagegateway#DescribeTapeArchivesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_storage_gateway.types.marker
    import capo_storage_gateway.types.tape_archives


class DescribeTapeArchivesOutput(TypedDict, closed=True):
    tape_archives: NotRequired["capo_storage_gateway.types.tape_archives.TapeArchives"]
    """<p>An array of virtual tape objects in the virtual tape shelf (VTS). The description includes of the Amazon Resource Name (ARN) of the virtual tapes. The information returned includes the Amazon Resource Names (ARNs) of the tapes, size of the tapes, status of the tapes, progress of the description, and tape barcode.</p>"""
    marker: NotRequired["capo_storage_gateway.types.marker.Marker"]
    """<p>An opaque string that indicates the position at which the virtual tapes that were fetched for description ended. Use this marker in your next request to fetch the next set of virtual tapes in the virtual tape shelf (VTS). If there are no more virtual tapes to describe, this field does not appear in the response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeTapeArchivesOutput) -> dict:
    out: dict = {}
    if "tape_archives" in value:
        import capo_storage_gateway.types.tape_archives

        out["TapeArchives"] = (
            capo_storage_gateway.types.tape_archives.serialize_aws_json_1_1(
                value["tape_archives"]
            )
        )
    if "marker" in value:
        out["Marker"] = value["marker"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeTapeArchivesOutput:
    out: DescribeTapeArchivesOutput = {}  # type: ignore[typeddict-item]
    if "TapeArchives" in data:
        import capo_storage_gateway.types.tape_archives

        out["tape_archives"] = (
            capo_storage_gateway.types.tape_archives.deserialize_aws_json_1_1(
                data["TapeArchives"]
            )
        )
    if "Marker" in data:
        out["marker"] = data["Marker"]
    return out
