"""Generated from Smithy shape ``com.amazonaws.wafregional#Predicate``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_waf_regional.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_waf_regional.types.negated
    import aws_sdk_waf_regional.types.predicate_type
    import aws_sdk_waf_regional.types.resource_id


class Predicate(TypedDict):
    negated: "aws_sdk_waf_regional.types.negated.Negated"
    """<p>Set <code>Negated</code> to <code>False</code> if you want AWS WAF to allow, block, or count requests based on the settings in the specified <a>ByteMatchSet</a>, <a>IPSet</a>, <a>SqlInjectionMatchSet</a>, <a>XssMatchSet</a>, <a>RegexMatchSet</a>, <a>GeoMatchSet</a>, or <a>SizeConstraintSet</a>. For example, if an <code>IPSet</code> includes the IP address <code>192.0.2.44</code>, AWS WAF will allow or block requests based on that IP address.</p> <p>Set <code>Negated</code> to <code>True</code> if you want AWS WAF to allow or block a request based on the negation of the settings in the <a>ByteMatchSet</a>, <a>IPSet</a>, <a>SqlInjectionMatchSet</a>, <a>XssMatchSet</a>, <a>RegexMatchSet</a>, <a>GeoMatchSet</a>, or <a>SizeConstraintSet</a>. For example, if an <code>IPSet</code> includes the IP address <code>192.0.2.44</code>, AWS WAF will allow, block, or count requests based on all IP addresses <i>except</i> <code>192.0.2.44</code>.</p>"""
    type: "aws_sdk_waf_regional.types.predicate_type.PredicateType"
    """<p>The type of predicate in a <code>Rule</code>, such as <code>ByteMatch</code> or <code>IPSet</code>.</p>"""
    data_id: "aws_sdk_waf_regional.types.resource_id.ResourceId"
    """<p>A unique identifier for a predicate in a <code>Rule</code>, such as <code>ByteMatchSetId</code> or <code>IPSetId</code>. The ID is returned by the corresponding <code>Create</code> or <code>List</code> command.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Predicate) -> dict:
    out: dict = {}
    out["Negated"] = value["negated"]
    import aws_sdk_waf_regional.types.predicate_type

    out["Type"] = aws_sdk_waf_regional.types.predicate_type.serialize_aws_json_1_1(
        value["type"]
    )
    out["DataId"] = value["data_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Predicate:
    out: Predicate = {}  # type: ignore[typeddict-item]
    if "Negated" in data:
        out["negated"] = data["Negated"]
    else:
        raise DeserializationError("Predicate.negated required")
    if "Type" in data:
        import aws_sdk_waf_regional.types.predicate_type

        out["type"] = (
            aws_sdk_waf_regional.types.predicate_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    else:
        raise DeserializationError("Predicate.type required")
    if "DataId" in data:
        out["data_id"] = data["DataId"]
    else:
        raise DeserializationError("Predicate.data_id required")
    return out
