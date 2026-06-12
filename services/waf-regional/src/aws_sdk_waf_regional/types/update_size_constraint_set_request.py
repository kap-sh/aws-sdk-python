"""Generated from Smithy shape ``com.amazonaws.wafregional#UpdateSizeConstraintSetRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_waf_regional.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_waf_regional.types.change_token
    import aws_sdk_waf_regional.types.resource_id
    import aws_sdk_waf_regional.types.size_constraint_set_updates


class UpdateSizeConstraintSetRequest(TypedDict):
    size_constraint_set_id: "aws_sdk_waf_regional.types.resource_id.ResourceId"
    """<p>The <code>SizeConstraintSetId</code> of the <a>SizeConstraintSet</a> that you want to update. <code>SizeConstraintSetId</code> is returned by <a>CreateSizeConstraintSet</a> and by <a>ListSizeConstraintSets</a>.</p>"""
    change_token: "aws_sdk_waf_regional.types.change_token.ChangeToken"
    """<p>The value returned by the most recent call to <a>GetChangeToken</a>.</p>"""
    updates: "aws_sdk_waf_regional.types.size_constraint_set_updates.SizeConstraintSetUpdates"
    """<p>An array of <code>SizeConstraintSetUpdate</code> objects that you want to insert into or delete from a <a>SizeConstraintSet</a>. For more information, see the applicable data types:</p> <ul> <li> <p> <a>SizeConstraintSetUpdate</a>: Contains <code>Action</code> and <code>SizeConstraint</code> </p> </li> <li> <p> <a>SizeConstraint</a>: Contains <code>FieldToMatch</code>, <code>TextTransformation</code>, <code>ComparisonOperator</code>, and <code>Size</code> </p> </li> <li> <p> <a>FieldToMatch</a>: Contains <code>Data</code> and <code>Type</code> </p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateSizeConstraintSetRequest) -> dict:
    out: dict = {}
    out["SizeConstraintSetId"] = value["size_constraint_set_id"]
    out["ChangeToken"] = value["change_token"]
    import aws_sdk_waf_regional.types.size_constraint_set_updates

    out["Updates"] = (
        aws_sdk_waf_regional.types.size_constraint_set_updates.serialize_aws_json_1_1(
            value["updates"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateSizeConstraintSetRequest:
    out: UpdateSizeConstraintSetRequest = {}  # type: ignore[typeddict-item]
    if "SizeConstraintSetId" in data:
        out["size_constraint_set_id"] = data["SizeConstraintSetId"]
    else:
        raise DeserializationError(
            "UpdateSizeConstraintSetRequest.size_constraint_set_id required"
        )
    if "ChangeToken" in data:
        out["change_token"] = data["ChangeToken"]
    else:
        raise DeserializationError(
            "UpdateSizeConstraintSetRequest.change_token required"
        )
    if "Updates" in data:
        import aws_sdk_waf_regional.types.size_constraint_set_updates

        out["updates"] = (
            aws_sdk_waf_regional.types.size_constraint_set_updates.deserialize_aws_json_1_1(
                data["Updates"]
            )
        )
    else:
        raise DeserializationError("UpdateSizeConstraintSetRequest.updates required")
    return out
