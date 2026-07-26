"""Generated from Smithy shape ``com.amazonaws.finspace#CreateEnvironmentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_finspace.types.environment_arn
    import capo_finspace.types.id_type
    import capo_finspace.types.url


class CreateEnvironmentResponse(TypedDict, closed=True):
    environment_id: NotRequired["capo_finspace.types.id_type.IdType"]
    """<p>The unique identifier for FinSpace environment that you created.</p>"""
    environment_arn: NotRequired["capo_finspace.types.environment_arn.EnvironmentArn"]
    """<p>The Amazon Resource Name (ARN) of the FinSpace environment that you created.</p>"""
    environment_url: NotRequired["capo_finspace.types.url.url"]
    """<p>The sign-in URL for the web application of the FinSpace environment you created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateEnvironmentResponse) -> dict:
    out: dict = {}
    if "environment_id" in value:
        out["environmentId"] = value["environment_id"]
    if "environment_arn" in value:
        out["environmentArn"] = value["environment_arn"]
    if "environment_url" in value:
        out["environmentUrl"] = value["environment_url"]
    return out


def deserialize_json(data: dict) -> CreateEnvironmentResponse:
    out: CreateEnvironmentResponse = {}  # type: ignore[typeddict-item]
    if "environmentId" in data:
        out["environment_id"] = data["environmentId"]
    if "environmentArn" in data:
        out["environment_arn"] = data["environmentArn"]
    if "environmentUrl" in data:
        out["environment_url"] = data["environmentUrl"]
    return out
