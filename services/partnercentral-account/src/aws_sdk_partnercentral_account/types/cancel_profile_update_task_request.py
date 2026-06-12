"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#CancelProfileUpdateTaskRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_partnercentral_account.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_account.types.catalog
    import aws_sdk_partnercentral_account.types.client_token
    import aws_sdk_partnercentral_account.types.partner_identifier
    import aws_sdk_partnercentral_account.types.profile_task_id


class CancelProfileUpdateTaskRequest(TypedDict):
    catalog: "aws_sdk_partnercentral_account.types.catalog.Catalog"
    """<p>The catalog identifier for the partner account.</p>"""
    identifier: (
        "aws_sdk_partnercentral_account.types.partner_identifier.PartnerIdentifier"
    )
    """<p>The unique identifier of the partner account.</p>"""
    client_token: NotRequired[
        "aws_sdk_partnercentral_account.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""
    task_id: "aws_sdk_partnercentral_account.types.profile_task_id.ProfileTaskId"
    """<p>The unique identifier of the profile update task to cancel.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CancelProfileUpdateTaskRequest) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    out["Identifier"] = value["identifier"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    out["TaskId"] = value["task_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CancelProfileUpdateTaskRequest:
    out: CancelProfileUpdateTaskRequest = {}  # type: ignore[typeddict-item]
    if "Catalog" in data:
        out["catalog"] = data["Catalog"]
    else:
        raise DeserializationError("CancelProfileUpdateTaskRequest.catalog required")
    if "Identifier" in data:
        out["identifier"] = data["Identifier"]
    else:
        raise DeserializationError("CancelProfileUpdateTaskRequest.identifier required")
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    if "TaskId" in data:
        out["task_id"] = data["TaskId"]
    else:
        raise DeserializationError("CancelProfileUpdateTaskRequest.task_id required")
    return out
