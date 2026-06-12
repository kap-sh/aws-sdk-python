"""Generated from Smithy shape ``com.amazonaws.b2bi#TestMappingResponse``."""

from typing import TypedDict

from aws_sdk_b2bi.errors import DeserializationError


class TestMappingResponse(TypedDict):
    mapped_file_content: "str"
    """<p>Returns a string for the mapping that can be used to identify the mapping. Similar to a fingerprint</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TestMappingResponse) -> dict:
    out: dict = {}
    out["mappedFileContent"] = value["mapped_file_content"]
    return out


def deserialize_aws_json_1_0(data: dict) -> TestMappingResponse:
    out: TestMappingResponse = {}  # type: ignore[typeddict-item]
    if "mappedFileContent" in data:
        out["mapped_file_content"] = data["mappedFileContent"]
    else:
        raise DeserializationError("TestMappingResponse.mapped_file_content required")
    return out
