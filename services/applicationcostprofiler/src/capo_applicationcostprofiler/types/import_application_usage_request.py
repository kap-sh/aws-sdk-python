"""Generated from Smithy shape ``com.amazonaws.applicationcostprofiler#ImportApplicationUsageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_applicationcostprofiler.errors import DeserializationError

if TYPE_CHECKING:
    import capo_applicationcostprofiler.types.source_s3_location


class ImportApplicationUsageRequest(TypedDict, closed=True):
    source_s3_location: (
        "capo_applicationcostprofiler.types.source_s3_location.SourceS3Location"
    )
    """<p>Amazon S3 location to import application usage data from.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImportApplicationUsageRequest) -> dict:
    out: dict = {}
    import capo_applicationcostprofiler.types.source_s3_location

    out["sourceS3Location"] = (
        capo_applicationcostprofiler.types.source_s3_location.serialize_json(
            value["source_s3_location"]
        )
    )
    return out


def deserialize_json(data: dict) -> ImportApplicationUsageRequest:
    out: ImportApplicationUsageRequest = {}  # type: ignore[typeddict-item]
    if "sourceS3Location" in data:
        import capo_applicationcostprofiler.types.source_s3_location

        out["source_s3_location"] = (
            capo_applicationcostprofiler.types.source_s3_location.deserialize_json(
                data["sourceS3Location"]
            )
        )
    else:
        raise DeserializationError(
            "ImportApplicationUsageRequest.source_s3_location required"
        )
    return out
