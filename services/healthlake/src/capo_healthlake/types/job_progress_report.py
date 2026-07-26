"""Generated from Smithy shape ``com.amazonaws.healthlake#JobProgressReport``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_healthlake.types.generic_double
    import capo_healthlake.types.generic_long


class JobProgressReport(TypedDict, closed=True):
    total_number_of_scanned_files: NotRequired[
        "capo_healthlake.types.generic_long.GenericLong"
    ]
    """<p>The number of files scanned from the S3 input bucket.</p>"""
    total_size_of_scanned_files_in_mb: NotRequired[
        "capo_healthlake.types.generic_double.GenericDouble"
    ]
    """<p>The size (in MB) of files scanned from the S3 input bucket.</p>"""
    total_number_of_imported_files: NotRequired[
        "capo_healthlake.types.generic_long.GenericLong"
    ]
    """<p>The number of files imported.</p>"""
    total_number_of_resources_scanned: NotRequired[
        "capo_healthlake.types.generic_long.GenericLong"
    ]
    """<p>The number of resources scanned from the S3 input bucket.</p>"""
    total_number_of_resources_imported: NotRequired[
        "capo_healthlake.types.generic_long.GenericLong"
    ]
    """<p>The number of resources imported.</p>"""
    total_number_of_resources_with_customer_error: NotRequired[
        "capo_healthlake.types.generic_long.GenericLong"
    ]
    """<p>The number of resources that failed due to customer error.</p>"""
    total_number_of_files_read_with_customer_error: NotRequired[
        "capo_healthlake.types.generic_long.GenericLong"
    ]
    """<p>The number of files that failed to be read from the S3 input bucket due to customer error.</p>"""
    throughput: NotRequired["capo_healthlake.types.generic_double.GenericDouble"]
    """<p>The transaction rate the import job is processed at.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: JobProgressReport) -> dict:
    out: dict = {}
    if "total_number_of_scanned_files" in value:
        out["TotalNumberOfScannedFiles"] = value["total_number_of_scanned_files"]
    if "total_size_of_scanned_files_in_mb" in value:
        out["TotalSizeOfScannedFilesInMB"] = value["total_size_of_scanned_files_in_mb"]
    if "total_number_of_imported_files" in value:
        out["TotalNumberOfImportedFiles"] = value["total_number_of_imported_files"]
    if "total_number_of_resources_scanned" in value:
        out["TotalNumberOfResourcesScanned"] = value[
            "total_number_of_resources_scanned"
        ]
    if "total_number_of_resources_imported" in value:
        out["TotalNumberOfResourcesImported"] = value[
            "total_number_of_resources_imported"
        ]
    if "total_number_of_resources_with_customer_error" in value:
        out["TotalNumberOfResourcesWithCustomerError"] = value[
            "total_number_of_resources_with_customer_error"
        ]
    if "total_number_of_files_read_with_customer_error" in value:
        out["TotalNumberOfFilesReadWithCustomerError"] = value[
            "total_number_of_files_read_with_customer_error"
        ]
    if "throughput" in value:
        out["Throughput"] = value["throughput"]
    return out


def deserialize_aws_json_1_0(data: dict) -> JobProgressReport:
    out: JobProgressReport = {}  # type: ignore[typeddict-item]
    if "TotalNumberOfScannedFiles" in data:
        out["total_number_of_scanned_files"] = data["TotalNumberOfScannedFiles"]
    if "TotalSizeOfScannedFilesInMB" in data:
        out["total_size_of_scanned_files_in_mb"] = data["TotalSizeOfScannedFilesInMB"]
    if "TotalNumberOfImportedFiles" in data:
        out["total_number_of_imported_files"] = data["TotalNumberOfImportedFiles"]
    if "TotalNumberOfResourcesScanned" in data:
        out["total_number_of_resources_scanned"] = data["TotalNumberOfResourcesScanned"]
    if "TotalNumberOfResourcesImported" in data:
        out["total_number_of_resources_imported"] = data[
            "TotalNumberOfResourcesImported"
        ]
    if "TotalNumberOfResourcesWithCustomerError" in data:
        out["total_number_of_resources_with_customer_error"] = data[
            "TotalNumberOfResourcesWithCustomerError"
        ]
    if "TotalNumberOfFilesReadWithCustomerError" in data:
        out["total_number_of_files_read_with_customer_error"] = data[
            "TotalNumberOfFilesReadWithCustomerError"
        ]
    if "Throughput" in data:
        out["throughput"] = data["Throughput"]
    return out
