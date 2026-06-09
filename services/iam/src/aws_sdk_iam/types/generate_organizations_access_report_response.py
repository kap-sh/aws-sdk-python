"""Generated from Smithy shape ``com.amazonaws.iam#GenerateOrganizationsAccessReportResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iam._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_iam.types.job_id_type


class GenerateOrganizationsAccessReportResponse(TypedDict):
    job_id: NotRequired["aws_sdk_iam.types.job_id_type.jobIDType"]
    """<p>The job identifier that you can use in the <a href=\"https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetOrganizationsAccessReport.html\">GetOrganizationsAccessReport</a> operation.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GenerateOrganizationsAccessReportResponse,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "job_id" in value:
        pairs.append((f"{prefix}.JobId", str(value["job_id"])))


def deserialize_query(el: Element) -> GenerateOrganizationsAccessReportResponse:
    out: GenerateOrganizationsAccessReportResponse = {}  # type: ignore[typeddict-item]
    child_job_id = el.find("JobId")
    if child_job_id is not None:
        out["job_id"] = str(child_job_id.text or "")
    return out
