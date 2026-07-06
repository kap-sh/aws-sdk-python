"""Generated from Smithy shape ``com.amazonaws.wafregional#CreateSizeConstraintSetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_waf_regional.types.change_token
    import aws_sdk_waf_regional.types.size_constraint_set


class CreateSizeConstraintSetResponse(TypedDict, closed=True):
    size_constraint_set: NotRequired[
        "aws_sdk_waf_regional.types.size_constraint_set.SizeConstraintSet"
    ]
    """<p>A <a>SizeConstraintSet</a> that contains no <code>SizeConstraint</code> objects.</p>"""
    change_token: NotRequired["aws_sdk_waf_regional.types.change_token.ChangeToken"]
    """<p>The <code>ChangeToken</code> that you used to submit the <code>CreateSizeConstraintSet</code> request. You can also use this value to query the status of the request. For more information, see <a>GetChangeTokenStatus</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateSizeConstraintSetResponse) -> dict:
    out: dict = {}
    if "size_constraint_set" in value:
        import aws_sdk_waf_regional.types.size_constraint_set

        out["SizeConstraintSet"] = (
            aws_sdk_waf_regional.types.size_constraint_set.serialize_aws_json_1_1(
                value["size_constraint_set"]
            )
        )
    if "change_token" in value:
        out["ChangeToken"] = value["change_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateSizeConstraintSetResponse:
    out: CreateSizeConstraintSetResponse = {}  # type: ignore[typeddict-item]
    if "SizeConstraintSet" in data:
        import aws_sdk_waf_regional.types.size_constraint_set

        out["size_constraint_set"] = (
            aws_sdk_waf_regional.types.size_constraint_set.deserialize_aws_json_1_1(
                data["SizeConstraintSet"]
            )
        )
    if "ChangeToken" in data:
        out["change_token"] = data["ChangeToken"]
    return out
