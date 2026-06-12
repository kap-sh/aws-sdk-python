"""Generated from Smithy shape ``com.amazonaws.datazone#AthenaPropertiesOutput``."""

from typing import TypedDict
from typing_extensions import NotRequired

class AthenaPropertiesOutput(TypedDict):
    workgroup_name: NotRequired["str"]
    """<p>The Amazon Athena workgroup name of a connection.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: AthenaPropertiesOutput) -> dict:
    out: dict = {}
    if "workgroup_name" in value:
        out["workgroupName"] = value["workgroup_name"]
    return out


def deserialize_json(data: dict) -> AthenaPropertiesOutput:
    out: AthenaPropertiesOutput = {}  # type: ignore[typeddict-item]
    if "workgroupName" in data:
        out["workgroup_name"] = data["workgroupName"]
    return out