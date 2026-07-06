"""Generated from Smithy shape ``com.amazonaws.waf#GetSizeConstraintSetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_waf.types.size_constraint_set


class GetSizeConstraintSetResponse(TypedDict, closed=True):
    size_constraint_set: NotRequired[
        "aws_sdk_waf.types.size_constraint_set.SizeConstraintSet"
    ]
    """<p>Information about the <a>SizeConstraintSet</a> that you specified in the <code>GetSizeConstraintSet</code> request. For more information, see the following topics:</p> <ul> <li> <p> <a>SizeConstraintSet</a>: Contains <code>SizeConstraintSetId</code>, <code>SizeConstraints</code>, and <code>Name</code> </p> </li> <li> <p> <code>SizeConstraints</code>: Contains an array of <a>SizeConstraint</a> objects. Each <code>SizeConstraint</code> object contains <a>FieldToMatch</a>, <code>TextTransformation</code>, <code>ComparisonOperator</code>, and <code>Size</code> </p> </li> <li> <p> <a>FieldToMatch</a>: Contains <code>Data</code> and <code>Type</code> </p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetSizeConstraintSetResponse) -> dict:
    out: dict = {}
    if "size_constraint_set" in value:
        import aws_sdk_waf.types.size_constraint_set

        out["SizeConstraintSet"] = (
            aws_sdk_waf.types.size_constraint_set.serialize_aws_json_1_1(
                value["size_constraint_set"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetSizeConstraintSetResponse:
    out: GetSizeConstraintSetResponse = {}  # type: ignore[typeddict-item]
    if "SizeConstraintSet" in data:
        import aws_sdk_waf.types.size_constraint_set

        out["size_constraint_set"] = (
            aws_sdk_waf.types.size_constraint_set.deserialize_aws_json_1_1(
                data["SizeConstraintSet"]
            )
        )
    return out
