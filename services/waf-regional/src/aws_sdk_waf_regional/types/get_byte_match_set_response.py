"""Generated from Smithy shape ``com.amazonaws.wafregional#GetByteMatchSetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_waf_regional.types.byte_match_set


class GetByteMatchSetResponse(TypedDict, closed=True):
    byte_match_set: NotRequired[
        "aws_sdk_waf_regional.types.byte_match_set.ByteMatchSet"
    ]
    """<p>Information about the <a>ByteMatchSet</a> that you specified in the <code>GetByteMatchSet</code> request. For more information, see the following topics:</p> <ul> <li> <p> <a>ByteMatchSet</a>: Contains <code>ByteMatchSetId</code>, <code>ByteMatchTuples</code>, and <code>Name</code> </p> </li> <li> <p> <code>ByteMatchTuples</code>: Contains an array of <a>ByteMatchTuple</a> objects. Each <code>ByteMatchTuple</code> object contains <a>FieldToMatch</a>, <code>PositionalConstraint</code>, <code>TargetString</code>, and <code>TextTransformation</code> </p> </li> <li> <p> <a>FieldToMatch</a>: Contains <code>Data</code> and <code>Type</code> </p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetByteMatchSetResponse) -> dict:
    out: dict = {}
    if "byte_match_set" in value:
        import aws_sdk_waf_regional.types.byte_match_set

        out["ByteMatchSet"] = (
            aws_sdk_waf_regional.types.byte_match_set.serialize_aws_json_1_1(
                value["byte_match_set"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetByteMatchSetResponse:
    out: GetByteMatchSetResponse = {}  # type: ignore[typeddict-item]
    if "ByteMatchSet" in data:
        import aws_sdk_waf_regional.types.byte_match_set

        out["byte_match_set"] = (
            aws_sdk_waf_regional.types.byte_match_set.deserialize_aws_json_1_1(
                data["ByteMatchSet"]
            )
        )
    return out
