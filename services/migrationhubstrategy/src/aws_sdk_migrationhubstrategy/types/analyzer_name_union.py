"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#AnalyzerNameUnion``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_migrationhubstrategy.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_migrationhubstrategy.types.binary_analyzer_name
    import aws_sdk_migrationhubstrategy.types.run_time_analyzer_name
    import aws_sdk_migrationhubstrategy.types.source_code_analyzer_name


class _AnalyzerNameUnion_binaryAnalyzerName(TypedDict):
    binaryAnalyzerName: (
        "aws_sdk_migrationhubstrategy.types.binary_analyzer_name.BinaryAnalyzerName"
    )


class _AnalyzerNameUnion_runTimeAnalyzerName(TypedDict):
    runTimeAnalyzerName: (
        "aws_sdk_migrationhubstrategy.types.run_time_analyzer_name.RunTimeAnalyzerName"
    )


class _AnalyzerNameUnion_sourceCodeAnalyzerName(TypedDict):
    sourceCodeAnalyzerName: "aws_sdk_migrationhubstrategy.types.source_code_analyzer_name.SourceCodeAnalyzerName"


AnalyzerNameUnion: TypeAlias = (
    _AnalyzerNameUnion_binaryAnalyzerName
    | _AnalyzerNameUnion_runTimeAnalyzerName
    | _AnalyzerNameUnion_sourceCodeAnalyzerName
)


# --- restJson1 ser/de ---
def serialize_json(value: AnalyzerNameUnion) -> dict:
    if "binaryAnalyzerName" in value:
        return {"binaryAnalyzerName": value["binaryAnalyzerName"]}
    elif "runTimeAnalyzerName" in value:
        return {"runTimeAnalyzerName": value["runTimeAnalyzerName"]}
    elif "sourceCodeAnalyzerName" in value:
        return {"sourceCodeAnalyzerName": value["sourceCodeAnalyzerName"]}
    else:
        raise SerializationError("AnalyzerNameUnion: no variant present")


def deserialize_json(data: dict) -> AnalyzerNameUnion:
    if "binaryAnalyzerName" in data:
        return {"binaryAnalyzerName": data["binaryAnalyzerName"]}
    elif "runTimeAnalyzerName" in data:
        return {"runTimeAnalyzerName": data["runTimeAnalyzerName"]}
    elif "sourceCodeAnalyzerName" in data:
        return {"sourceCodeAnalyzerName": data["sourceCodeAnalyzerName"]}
    else:
        raise DeserializationError("AnalyzerNameUnion: no recognized variant key")
