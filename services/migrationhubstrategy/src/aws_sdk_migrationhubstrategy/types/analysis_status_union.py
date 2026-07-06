"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#AnalysisStatusUnion``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_migrationhubstrategy.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_migrationhubstrategy.types.runtime_analysis_status
    import aws_sdk_migrationhubstrategy.types.src_code_or_db_analysis_status


class _AnalysisStatusUnion_runtimeAnalysisStatus(TypedDict, closed=True):
    runtimeAnalysisStatus: "aws_sdk_migrationhubstrategy.types.runtime_analysis_status.RuntimeAnalysisStatus"


class _AnalysisStatusUnion_srcCodeOrDbAnalysisStatus(TypedDict, closed=True):
    srcCodeOrDbAnalysisStatus: "aws_sdk_migrationhubstrategy.types.src_code_or_db_analysis_status.SrcCodeOrDbAnalysisStatus"


AnalysisStatusUnion: TypeAlias = (
    _AnalysisStatusUnion_runtimeAnalysisStatus
    | _AnalysisStatusUnion_srcCodeOrDbAnalysisStatus
)


# --- restJson1 ser/de ---
def serialize_json(value: AnalysisStatusUnion) -> dict:
    if "runtimeAnalysisStatus" in value:
        return {"runtimeAnalysisStatus": value["runtimeAnalysisStatus"]}
    elif "srcCodeOrDbAnalysisStatus" in value:
        return {"srcCodeOrDbAnalysisStatus": value["srcCodeOrDbAnalysisStatus"]}
    else:
        raise SerializationError("AnalysisStatusUnion: no variant present")


def deserialize_json(data: dict) -> AnalysisStatusUnion:
    if "runtimeAnalysisStatus" in data:
        return {"runtimeAnalysisStatus": data["runtimeAnalysisStatus"]}
    elif "srcCodeOrDbAnalysisStatus" in data:
        return {"srcCodeOrDbAnalysisStatus": data["srcCodeOrDbAnalysisStatus"]}
    else:
        raise DeserializationError("AnalysisStatusUnion: no recognized variant key")
