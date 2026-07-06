"""Generated from Smithy shape ``com.amazonaws.waf#DeleteSizeConstraintSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_waf.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_waf.types.change_token
    import aws_sdk_waf.types.resource_id


class DeleteSizeConstraintSetRequest(TypedDict, closed=True):
    size_constraint_set_id: "aws_sdk_waf.types.resource_id.ResourceId"
    """<p>The <code>SizeConstraintSetId</code> of the <a>SizeConstraintSet</a> that you want to delete. <code>SizeConstraintSetId</code> is returned by <a>CreateSizeConstraintSet</a> and by <a>ListSizeConstraintSets</a>.</p>"""
    change_token: "aws_sdk_waf.types.change_token.ChangeToken"
    """<p>The value returned by the most recent call to <a>GetChangeToken</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteSizeConstraintSetRequest) -> dict:
    out: dict = {}
    out["SizeConstraintSetId"] = value["size_constraint_set_id"]
    out["ChangeToken"] = value["change_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteSizeConstraintSetRequest:
    out: DeleteSizeConstraintSetRequest = {}  # type: ignore[typeddict-item]
    if "SizeConstraintSetId" in data:
        out["size_constraint_set_id"] = data["SizeConstraintSetId"]
    else:
        raise DeserializationError(
            "DeleteSizeConstraintSetRequest.size_constraint_set_id required"
        )
    if "ChangeToken" in data:
        out["change_token"] = data["ChangeToken"]
    else:
        raise DeserializationError(
            "DeleteSizeConstraintSetRequest.change_token required"
        )
    return out
