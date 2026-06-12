"""Generated from Smithy shape ``com.amazonaws.dataexchange#JobError``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_dataexchange.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_dataexchange.types.__double
    import aws_sdk_dataexchange.types.__string
    import aws_sdk_dataexchange.types.code
    import aws_sdk_dataexchange.types.details
    import aws_sdk_dataexchange.types.job_error_limit_name
    import aws_sdk_dataexchange.types.job_error_resource_types


class JobError(TypedDict):
    code: "aws_sdk_dataexchange.types.code.Code"
    """<p>The code for the job error.</p>"""
    details: NotRequired["aws_sdk_dataexchange.types.details.Details"]
    """<p>The details about the job error.</p>"""
    limit_name: NotRequired[
        "aws_sdk_dataexchange.types.job_error_limit_name.JobErrorLimitName"
    ]
    """<p>The name of the limit that was reached.</p>"""
    limit_value: "aws_sdk_dataexchange.types.__double.__double"
    """<p>The value of the exceeded limit.</p>"""
    message: "aws_sdk_dataexchange.types.__string.__string"
    """<p>The message related to the job error.</p>"""
    resource_id: NotRequired["aws_sdk_dataexchange.types.__string.__string"]
    """<p>The unique identifier for the resource related to the error.</p>"""
    resource_type: NotRequired[
        "aws_sdk_dataexchange.types.job_error_resource_types.JobErrorResourceTypes"
    ]
    """<p>The type of resource related to the error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobError) -> dict:
    out: dict = {}
    out["Code"] = value["code"]
    if "details" in value:
        import aws_sdk_dataexchange.types.details

        out["Details"] = aws_sdk_dataexchange.types.details.serialize_json(
            value["details"]
        )
    if "limit_name" in value:
        out["LimitName"] = value["limit_name"]
    out["LimitValue"] = value.get("limit_value", 0)
    out["Message"] = value["message"]
    if "resource_id" in value:
        out["ResourceId"] = value["resource_id"]
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    return out


def deserialize_json(data: dict) -> JobError:
    out: JobError = {}  # type: ignore[typeddict-item]
    if "Code" in data:
        out["code"] = data["Code"]
    else:
        raise DeserializationError("JobError.code required")
    if "Details" in data:
        import aws_sdk_dataexchange.types.details

        out["details"] = aws_sdk_dataexchange.types.details.deserialize_json(
            data["Details"]
        )
    if "LimitName" in data:
        out["limit_name"] = data["LimitName"]
    if "LimitValue" in data:
        out["limit_value"] = data["LimitValue"]
    else:
        out["limit_value"] = 0
    if "Message" in data:
        out["message"] = data["Message"]
    else:
        raise DeserializationError("JobError.message required")
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    if "ResourceType" in data:
        out["resource_type"] = data["ResourceType"]
    return out
