"""Generated from Smithy shape ``com.amazonaws.datazone#AthenaPropertiesPatch``."""

from typing_extensions import NotRequired, TypedDict


class AthenaPropertiesPatch(TypedDict, closed=True):
    workgroup_name: NotRequired["str"]
    """<p>The Amazon Athena workgroup name of a connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AthenaPropertiesPatch) -> dict:
    out: dict = {}
    if "workgroup_name" in value:
        out["workgroupName"] = value["workgroup_name"]
    return out


def deserialize_json(data: dict) -> AthenaPropertiesPatch:
    out: AthenaPropertiesPatch = {}  # type: ignore[typeddict-item]
    if "workgroupName" in data:
        out["workgroup_name"] = data["workgroupName"]
    return out
