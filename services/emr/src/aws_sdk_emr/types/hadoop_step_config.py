"""Generated from Smithy shape ``com.amazonaws.emr#HadoopStepConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr.types.string
    import aws_sdk_emr.types.string_list
    import aws_sdk_emr.types.string_map


class HadoopStepConfig(TypedDict):
    jar: NotRequired["aws_sdk_emr.types.string.String"]
    """<p>The path to the JAR file that runs during the step.</p>"""
    properties: NotRequired["aws_sdk_emr.types.string_map.StringMap"]
    """<p>The list of Java properties that are set when the step runs. You can use these properties to pass key-value pairs to your main function.</p>"""
    main_class: NotRequired["aws_sdk_emr.types.string.String"]
    """<p>The name of the main class in the specified Java file. If not specified, the JAR file should specify a main class in its manifest file.</p>"""
    args: NotRequired["aws_sdk_emr.types.string_list.StringList"]
    """<p>The list of command line arguments to pass to the JAR file's main function for execution.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HadoopStepConfig) -> dict:
    out: dict = {}
    if "jar" in value:
        out["Jar"] = value["jar"]
    if "properties" in value:
        import aws_sdk_emr.types.string_map

        out["Properties"] = aws_sdk_emr.types.string_map.serialize_aws_json_1_1(
            value["properties"]
        )
    if "main_class" in value:
        out["MainClass"] = value["main_class"]
    if "args" in value:
        import aws_sdk_emr.types.string_list

        out["Args"] = aws_sdk_emr.types.string_list.serialize_aws_json_1_1(
            value["args"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> HadoopStepConfig:
    out: HadoopStepConfig = {}  # type: ignore[typeddict-item]
    if "Jar" in data:
        out["jar"] = data["Jar"]
    if "Properties" in data:
        import aws_sdk_emr.types.string_map

        out["properties"] = aws_sdk_emr.types.string_map.deserialize_aws_json_1_1(
            data["Properties"]
        )
    if "MainClass" in data:
        out["main_class"] = data["MainClass"]
    if "Args" in data:
        import aws_sdk_emr.types.string_list

        out["args"] = aws_sdk_emr.types.string_list.deserialize_aws_json_1_1(
            data["Args"]
        )
    return out
