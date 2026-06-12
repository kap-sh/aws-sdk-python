"""Generated from Smithy shape ``com.amazonaws.panorama#ListPackageImportJobsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_panorama.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_panorama.types.next_token
    import aws_sdk_panorama.types.package_import_job_list


class ListPackageImportJobsResponse(TypedDict):
    package_import_jobs: (
        "aws_sdk_panorama.types.package_import_job_list.PackageImportJobList"
    )
    """<p>A list of package import jobs.</p>"""
    next_token: NotRequired["aws_sdk_panorama.types.next_token.NextToken"]
    """<p>A pagination token that's included if more results are available.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPackageImportJobsResponse) -> dict:
    out: dict = {}
    import aws_sdk_panorama.types.package_import_job_list

    out["PackageImportJobs"] = (
        aws_sdk_panorama.types.package_import_job_list.serialize_json(
            value["package_import_jobs"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListPackageImportJobsResponse:
    out: ListPackageImportJobsResponse = {}  # type: ignore[typeddict-item]
    if "PackageImportJobs" in data:
        import aws_sdk_panorama.types.package_import_job_list

        out["package_import_jobs"] = (
            aws_sdk_panorama.types.package_import_job_list.deserialize_json(
                data["PackageImportJobs"]
            )
        )
    else:
        raise DeserializationError(
            "ListPackageImportJobsResponse.package_import_jobs required"
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
