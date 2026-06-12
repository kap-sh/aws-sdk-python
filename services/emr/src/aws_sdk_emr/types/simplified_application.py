"""Generated from Smithy shape ``com.amazonaws.emr#SimplifiedApplication``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr.types.string


class SimplifiedApplication(TypedDict):
    name: NotRequired["aws_sdk_emr.types.string.String"]
    """<p>The returned release label application name. For example, <code>hadoop</code>.</p>"""
    version: NotRequired["aws_sdk_emr.types.string.String"]
    """<p>The returned release label application version. For example, <code>3.2.1</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SimplifiedApplication) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "version" in value:
        out["Version"] = value["version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SimplifiedApplication:
    out: SimplifiedApplication = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Version" in data:
        out["version"] = data["Version"]
    return out
