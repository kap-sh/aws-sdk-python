"""Generated from Smithy shape ``com.amazonaws.emrserverless#Hive``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_emr_serverless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_emr_serverless.types.hive_cli_parameters
    import aws_sdk_emr_serverless.types.init_script_path
    import aws_sdk_emr_serverless.types.query


class Hive(TypedDict):
    query: "aws_sdk_emr_serverless.types.query.Query"
    """<p>The query for the Hive job run.</p>"""
    init_query_file: NotRequired[
        "aws_sdk_emr_serverless.types.init_script_path.InitScriptPath"
    ]
    """<p>The query file for the Hive job run.</p>"""
    parameters: NotRequired[
        "aws_sdk_emr_serverless.types.hive_cli_parameters.HiveCliParameters"
    ]
    """<p>The parameters for the Hive job run.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Hive) -> dict:
    out: dict = {}
    out["query"] = value["query"]
    if "init_query_file" in value:
        out["initQueryFile"] = value["init_query_file"]
    if "parameters" in value:
        out["parameters"] = value["parameters"]
    return out


def deserialize_json(data: dict) -> Hive:
    out: Hive = {}  # type: ignore[typeddict-item]
    if "query" in data:
        out["query"] = data["query"]
    else:
        raise DeserializationError("Hive.query required")
    if "initQueryFile" in data:
        out["init_query_file"] = data["initQueryFile"]
    if "parameters" in data:
        out["parameters"] = data["parameters"]
    return out
