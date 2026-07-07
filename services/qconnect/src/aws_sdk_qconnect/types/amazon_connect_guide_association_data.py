"""Generated from Smithy shape ``com.amazonaws.qconnect#AmazonConnectGuideAssociationData``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.generic_arn


class AmazonConnectGuideAssociationData(TypedDict, closed=True):
    flow_id: NotRequired["aws_sdk_qconnect.types.generic_arn.GenericArn"]
    """<p> The Amazon Resource Name (ARN) of an Amazon Connect flow. Step-by-step guides are a type of flow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AmazonConnectGuideAssociationData) -> dict:
    out: dict = {}
    if "flow_id" in value:
        out["flowId"] = value["flow_id"]
    return out


def deserialize_json(data: dict) -> AmazonConnectGuideAssociationData:
    out: AmazonConnectGuideAssociationData = {}  # type: ignore[typeddict-item]
    if "flowId" in data:
        out["flow_id"] = data["flowId"]
    return out
