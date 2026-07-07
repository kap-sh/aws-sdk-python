"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#ListListenersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_global_accelerator.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_global_accelerator.types.generic_string
    import aws_sdk_global_accelerator.types.max_results


class ListListenersRequest(TypedDict, closed=True):
    accelerator_arn: "aws_sdk_global_accelerator.types.generic_string.GenericString"
    """<p>The Amazon Resource Name (ARN) of the accelerator for which you want to list listener objects.</p>"""
    max_results: NotRequired["aws_sdk_global_accelerator.types.max_results.MaxResults"]
    """<p>The number of listener objects that you want to return with this call. The default value is 10.</p>"""
    next_token: NotRequired[
        "aws_sdk_global_accelerator.types.generic_string.GenericString"
    ]
    """<p>The token for the next set of results. You receive this token from a previous call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListListenersRequest) -> dict:
    out: dict = {}
    out["AcceleratorArn"] = value["accelerator_arn"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListListenersRequest:
    out: ListListenersRequest = {}  # type: ignore[typeddict-item]
    if "AcceleratorArn" in data:
        out["accelerator_arn"] = data["AcceleratorArn"]
    else:
        raise DeserializationError("ListListenersRequest.accelerator_arn required")
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
