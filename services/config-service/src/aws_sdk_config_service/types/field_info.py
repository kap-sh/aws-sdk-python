"""Generated from Smithy shape ``com.amazonaws.configservice#FieldInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_config_service.types.field_name


class FieldInfo(TypedDict, closed=True):
    name: NotRequired["aws_sdk_config_service.types.field_name.FieldName"]
    """<p>Name of the field.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FieldInfo) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FieldInfo:
    out: FieldInfo = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    return out
