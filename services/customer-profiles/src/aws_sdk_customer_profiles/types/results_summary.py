"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ResultsSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.optional_long


class ResultsSummary(TypedDict):
    updated_records: NotRequired[
        "aws_sdk_customer_profiles.types.optional_long.optionalLong"
    ]
    """<p>The number of records that were updated during the upload job. </p>"""
    created_records: NotRequired[
        "aws_sdk_customer_profiles.types.optional_long.optionalLong"
    ]
    """<p>The number of records that were newly created during the upload job. </p>"""
    failed_records: NotRequired[
        "aws_sdk_customer_profiles.types.optional_long.optionalLong"
    ]
    """<p>The number of records that failed to be processed during the upload job. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResultsSummary) -> dict:
    out: dict = {}
    if "updated_records" in value:
        out["UpdatedRecords"] = value["updated_records"]
    if "created_records" in value:
        out["CreatedRecords"] = value["created_records"]
    if "failed_records" in value:
        out["FailedRecords"] = value["failed_records"]
    return out


def deserialize_json(data: dict) -> ResultsSummary:
    out: ResultsSummary = {}  # type: ignore[typeddict-item]
    if "UpdatedRecords" in data:
        out["updated_records"] = data["UpdatedRecords"]
    if "CreatedRecords" in data:
        out["created_records"] = data["CreatedRecords"]
    if "FailedRecords" in data:
        out["failed_records"] = data["FailedRecords"]
    return out
