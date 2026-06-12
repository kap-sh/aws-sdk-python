"""Generated from Smithy shape ``com.amazonaws.m2#JobIdentifier``."""

from typing import TypeAlias, TypedDict

from aws_sdk_m2.errors import DeserializationError, SerializationError


class _JobIdentifier_fileName(TypedDict):
    fileName: "str"


class _JobIdentifier_scriptName(TypedDict):
    scriptName: "str"


JobIdentifier: TypeAlias = _JobIdentifier_fileName | _JobIdentifier_scriptName


# --- restJson1 ser/de ---
def serialize_json(value: JobIdentifier) -> dict:
    if "fileName" in value:
        return {"fileName": value["fileName"]}
    elif "scriptName" in value:
        return {"scriptName": value["scriptName"]}
    else:
        raise SerializationError("JobIdentifier: no variant present")


def deserialize_json(data: dict) -> JobIdentifier:
    if "fileName" in data:
        return {"fileName": data["fileName"]}
    elif "scriptName" in data:
        return {"scriptName": data["scriptName"]}
    else:
        raise DeserializationError("JobIdentifier: no recognized variant key")
