"""Generated from Smithy shape ``com.amazonaws.securityhub#StandardsSubscriptionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string
    import capo_securityhub.types.standards_input_parameter_map


class StandardsSubscriptionRequest(TypedDict, closed=True):
    standards_arn: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The ARN of the standard that you want to enable. To view the list of available standards and their ARNs, use the <code>DescribeStandards</code> operation.</p>"""
    standards_input: NotRequired[
        "capo_securityhub.types.standards_input_parameter_map.StandardsInputParameterMap"
    ]
    """<p>A key-value pair of input for the standard.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StandardsSubscriptionRequest) -> dict:
    out: dict = {}
    if "standards_arn" in value:
        out["StandardsArn"] = value["standards_arn"]
    if "standards_input" in value:
        import capo_securityhub.types.standards_input_parameter_map

        out["StandardsInput"] = (
            capo_securityhub.types.standards_input_parameter_map.serialize_json(
                value["standards_input"]
            )
        )
    return out


def deserialize_json(data: dict) -> StandardsSubscriptionRequest:
    out: StandardsSubscriptionRequest = {}  # type: ignore[typeddict-item]
    if "StandardsArn" in data:
        out["standards_arn"] = data["StandardsArn"]
    if "StandardsInput" in data:
        import capo_securityhub.types.standards_input_parameter_map

        out["standards_input"] = (
            capo_securityhub.types.standards_input_parameter_map.deserialize_json(
                data["StandardsInput"]
            )
        )
    return out
