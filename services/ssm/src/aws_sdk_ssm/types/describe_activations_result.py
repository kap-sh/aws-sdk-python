"""Generated from Smithy shape ``com.amazonaws.ssm#DescribeActivationsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm.types.activation_list
    import aws_sdk_ssm.types.next_token


class DescribeActivationsResult(TypedDict, closed=True):
    activation_list: NotRequired["aws_sdk_ssm.types.activation_list.ActivationList"]
    """<p>A list of activations for your Amazon Web Services account.</p>"""
    next_token: NotRequired["aws_sdk_ssm.types.next_token.NextToken"]
    """<p>The token for the next set of items to return. Use this token to get the next set of results. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeActivationsResult) -> dict:
    out: dict = {}
    if "activation_list" in value:
        import aws_sdk_ssm.types.activation_list

        out["ActivationList"] = (
            aws_sdk_ssm.types.activation_list.serialize_aws_json_1_1(
                value["activation_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeActivationsResult:
    out: DescribeActivationsResult = {}  # type: ignore[typeddict-item]
    if "ActivationList" in data:
        import aws_sdk_ssm.types.activation_list

        out["activation_list"] = (
            aws_sdk_ssm.types.activation_list.deserialize_aws_json_1_1(
                data["ActivationList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
