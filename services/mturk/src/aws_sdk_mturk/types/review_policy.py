"""Generated from Smithy shape ``com.amazonaws.mturk#ReviewPolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_mturk.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mturk.types.policy_parameter_list
    import aws_sdk_mturk.types.string


class ReviewPolicy(TypedDict, closed=True):
    policy_name: "aws_sdk_mturk.types.string.String"
    """<p> Name of a Review Policy: SimplePlurality/2011-09-01 or ScoreMyKnownAnswers/2011-09-01 </p>"""
    parameters: NotRequired[
        "aws_sdk_mturk.types.policy_parameter_list.PolicyParameterList"
    ]
    """<p>Name of the parameter from the Review policy.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReviewPolicy) -> dict:
    out: dict = {}
    out["PolicyName"] = value["policy_name"]
    if "parameters" in value:
        import aws_sdk_mturk.types.policy_parameter_list

        out["Parameters"] = (
            aws_sdk_mturk.types.policy_parameter_list.serialize_aws_json_1_1(
                value["parameters"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ReviewPolicy:
    out: ReviewPolicy = {}  # type: ignore[typeddict-item]
    if "PolicyName" in data:
        out["policy_name"] = data["PolicyName"]
    else:
        raise DeserializationError("ReviewPolicy.policy_name required")
    if "Parameters" in data:
        import aws_sdk_mturk.types.policy_parameter_list

        out["parameters"] = (
            aws_sdk_mturk.types.policy_parameter_list.deserialize_aws_json_1_1(
                data["Parameters"]
            )
        )
    return out
