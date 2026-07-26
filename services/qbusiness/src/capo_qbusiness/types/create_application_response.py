"""Generated from Smithy shape ``com.amazonaws.qbusiness#CreateApplicationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.application_arn
    import capo_qbusiness.types.application_id


class CreateApplicationResponse(TypedDict, closed=True):
    application_id: NotRequired["capo_qbusiness.types.application_id.ApplicationId"]
    """<p>The identifier of the Amazon Q Business application.</p>"""
    application_arn: NotRequired["capo_qbusiness.types.application_arn.ApplicationArn"]
    """<p> The Amazon Resource Name (ARN) of the Amazon Q Business application. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateApplicationResponse) -> dict:
    out: dict = {}
    if "application_id" in value:
        out["applicationId"] = value["application_id"]
    if "application_arn" in value:
        out["applicationArn"] = value["application_arn"]
    return out


def deserialize_json(data: dict) -> CreateApplicationResponse:
    out: CreateApplicationResponse = {}  # type: ignore[typeddict-item]
    if "applicationId" in data:
        out["application_id"] = data["applicationId"]
    if "applicationArn" in data:
        out["application_arn"] = data["applicationArn"]
    return out
