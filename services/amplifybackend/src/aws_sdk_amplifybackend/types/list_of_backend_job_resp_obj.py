"""Generated from Smithy shape ``com.amazonaws.amplifybackend#ListOfBackendJobRespObj``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_amplifybackend.types.backend_job_resp_obj

ListOfBackendJobRespObj: TypeAlias = list[
    "aws_sdk_amplifybackend.types.backend_job_resp_obj.BackendJobRespObj"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfBackendJobRespObj) -> list:
    import aws_sdk_amplifybackend.types.backend_job_resp_obj

    out: list = []
    for item in value:
        out.append(
            aws_sdk_amplifybackend.types.backend_job_resp_obj.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ListOfBackendJobRespObj:
    import aws_sdk_amplifybackend.types.backend_job_resp_obj

    out: ListOfBackendJobRespObj = []
    for item in data:
        out.append(
            aws_sdk_amplifybackend.types.backend_job_resp_obj.deserialize_json(item)
        )
    return out
