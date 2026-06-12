"""Generated from Smithy shape ``com.amazonaws.cloudwatch#DashboardValidationMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudwatch.types.data_path
    import aws_sdk_cloudwatch.types.message


class DashboardValidationMessage(TypedDict):
    data_path: NotRequired["aws_sdk_cloudwatch.types.data_path.DataPath"]
    """<p>The data path related to the message.</p>"""
    message: NotRequired["aws_sdk_cloudwatch.types.message.Message"]
    """<p>A message describing the error or warning.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DashboardValidationMessage) -> dict:
    out: dict = {}
    if "data_path" in value:
        out["DataPath"] = value["data_path"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DashboardValidationMessage:
    out: DashboardValidationMessage = {}  # type: ignore[typeddict-item]
    if "DataPath" in data:
        out["data_path"] = data["DataPath"]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: DashboardValidationMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "data_path" in value:
        pairs.append((f"{prefix}.DataPath", str(value["data_path"])))
    if "message" in value:
        pairs.append((f"{prefix}.Message", str(value["message"])))


def deserialize_query(el: Element) -> DashboardValidationMessage:
    out: DashboardValidationMessage = {}  # type: ignore[typeddict-item]
    child_data_path = el.find("DataPath")
    if child_data_path is not None:
        out["data_path"] = str(child_data_path.text or "")
    child_message = el.find("Message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out
