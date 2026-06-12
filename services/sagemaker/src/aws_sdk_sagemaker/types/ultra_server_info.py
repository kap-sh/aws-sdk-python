"""Generated from Smithy shape ``com.amazonaws.sagemaker#UltraServerInfo``."""

from typing import TypedDict

from typing_extensions import NotRequired


class UltraServerInfo(TypedDict):
    id: NotRequired["str"]
    """<p>The unique identifier of the UltraServer.</p>"""
    type: NotRequired["str"]
    """<p>The type of the UltraServer.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UltraServerInfo) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "type" in value:
        out["Type"] = value["type"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UltraServerInfo:
    out: UltraServerInfo = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Type" in data:
        out["type"] = data["Type"]
    return out
