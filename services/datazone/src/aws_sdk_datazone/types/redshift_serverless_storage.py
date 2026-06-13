"""Generated from Smithy shape ``com.amazonaws.datazone#RedshiftServerlessStorage``."""

from typing import TypedDict
from aws_sdk_datazone.errors import DeserializationError


class RedshiftServerlessStorage(TypedDict):
    workgroup_name: "str"
    """<p>The name of the Amazon Redshift Serverless workgroup.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RedshiftServerlessStorage) -> dict:
    out: dict = {}
    out["workgroupName"] = value["workgroup_name"]
    return out


def deserialize_json(data: dict) -> RedshiftServerlessStorage:
    out: RedshiftServerlessStorage = {}  # type: ignore[typeddict-item]
    if "workgroupName" in data:
        out["workgroup_name"] = data["workgroupName"]
    else:
        raise DeserializationError("RedshiftServerlessStorage.workgroup_name required")
    return out
