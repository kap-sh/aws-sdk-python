"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateSelfUpgradeResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.self_upgrade_request_detail
    import aws_sdk_quicksight.types.status_code
    import aws_sdk_quicksight.types.string


class UpdateSelfUpgradeResponse(TypedDict, closed=True):
    self_upgrade_request_detail: NotRequired[
        "aws_sdk_quicksight.types.self_upgrade_request_detail.SelfUpgradeRequestDetail"
    ]
    """<p>Details of the updated self-upgrade request.</p>"""
    request_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSelfUpgradeResponse) -> dict:
    out: dict = {}
    if "self_upgrade_request_detail" in value:
        import aws_sdk_quicksight.types.self_upgrade_request_detail

        out["SelfUpgradeRequestDetail"] = (
            aws_sdk_quicksight.types.self_upgrade_request_detail.serialize_json(
                value["self_upgrade_request_detail"]
            )
        )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> UpdateSelfUpgradeResponse:
    out: UpdateSelfUpgradeResponse = {}  # type: ignore[typeddict-item]
    if "SelfUpgradeRequestDetail" in data:
        import aws_sdk_quicksight.types.self_upgrade_request_detail

        out["self_upgrade_request_detail"] = (
            aws_sdk_quicksight.types.self_upgrade_request_detail.deserialize_json(
                data["SelfUpgradeRequestDetail"]
            )
        )
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
