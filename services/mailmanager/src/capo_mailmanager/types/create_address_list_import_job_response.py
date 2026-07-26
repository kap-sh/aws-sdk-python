"""Generated from Smithy shape ``com.amazonaws.mailmanager#CreateAddressListImportJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_mailmanager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mailmanager.types.job_id
    import capo_mailmanager.types.pre_signed_url


class CreateAddressListImportJobResponse(TypedDict, closed=True):
    job_id: "capo_mailmanager.types.job_id.JobId"
    """<p>The identifier of the created import job.</p>"""
    pre_signed_url: "capo_mailmanager.types.pre_signed_url.PreSignedUrl"
    """<p>The pre-signed URL target for uploading the input file.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateAddressListImportJobResponse) -> dict:
    out: dict = {}
    out["JobId"] = value["job_id"]
    out["PreSignedUrl"] = value["pre_signed_url"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateAddressListImportJobResponse:
    out: CreateAddressListImportJobResponse = {}  # type: ignore[typeddict-item]
    if "JobId" in data:
        out["job_id"] = data["JobId"]
    else:
        raise DeserializationError("CreateAddressListImportJobResponse.job_id required")
    if "PreSignedUrl" in data:
        out["pre_signed_url"] = data["PreSignedUrl"]
    else:
        raise DeserializationError(
            "CreateAddressListImportJobResponse.pre_signed_url required"
        )
    return out
