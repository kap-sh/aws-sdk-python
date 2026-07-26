"""Generated from Smithy shape ``com.amazonaws.sagemaker#EndpointInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.endpoint_name


class EndpointInfo(TypedDict, closed=True):
    endpoint_name: NotRequired["capo_sagemaker.types.endpoint_name.EndpointName"]
    """<p>The name of a customer's endpoint.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EndpointInfo) -> dict:
    out: dict = {}
    if "endpoint_name" in value:
        out["EndpointName"] = value["endpoint_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EndpointInfo:
    out: EndpointInfo = {}  # type: ignore[typeddict-item]
    if "EndpointName" in data:
        out["endpoint_name"] = data["EndpointName"]
    return out
