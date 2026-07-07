"""Generated from Smithy shape ``com.amazonaws.workspaces#CreateConnectClientAddInResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.amazon_uuid


class CreateConnectClientAddInResult(TypedDict, closed=True):
    add_in_id: NotRequired["aws_sdk_workspaces.types.amazon_uuid.AmazonUuid"]
    """<p>The client add-in identifier.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateConnectClientAddInResult) -> dict:
    out: dict = {}
    if "add_in_id" in value:
        out["AddInId"] = value["add_in_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateConnectClientAddInResult:
    out: CreateConnectClientAddInResult = {}  # type: ignore[typeddict-item]
    if "AddInId" in data:
        out["add_in_id"] = data["AddInId"]
    return out
