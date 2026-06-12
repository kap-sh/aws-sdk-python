"""Generated from Smithy shape ``com.amazonaws.emr#HadoopJarStepConfig``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr.types.key_value_list
    import aws_sdk_emr.types.xml_string
    import aws_sdk_emr.types.xml_string_list


class HadoopJarStepConfig(TypedDict):
    properties: NotRequired["aws_sdk_emr.types.key_value_list.KeyValueList"]
    """<p>A list of Java properties that are set when the step runs. You can use these properties to pass key-value pairs to your main function.</p>"""
    jar: NotRequired["aws_sdk_emr.types.xml_string.XmlString"]
    """<p>A path to a JAR file run during the step.</p>"""
    main_class: NotRequired["aws_sdk_emr.types.xml_string.XmlString"]
    """<p>The name of the main class in the specified Java file. If not specified, the JAR file should specify a Main-Class in its manifest file.</p>"""
    args: NotRequired["aws_sdk_emr.types.xml_string_list.XmlStringList"]
    """<p>A list of command line arguments passed to the JAR file's main function when executed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HadoopJarStepConfig) -> dict:
    out: dict = {}
    if "properties" in value:
        import aws_sdk_emr.types.key_value_list

        out["Properties"] = aws_sdk_emr.types.key_value_list.serialize_aws_json_1_1(
            value["properties"]
        )
    if "jar" in value:
        out["Jar"] = value["jar"]
    if "main_class" in value:
        out["MainClass"] = value["main_class"]
    if "args" in value:
        import aws_sdk_emr.types.xml_string_list

        out["Args"] = aws_sdk_emr.types.xml_string_list.serialize_aws_json_1_1(
            value["args"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> HadoopJarStepConfig:
    out: HadoopJarStepConfig = {}  # type: ignore[typeddict-item]
    if "Properties" in data:
        import aws_sdk_emr.types.key_value_list

        out["properties"] = aws_sdk_emr.types.key_value_list.deserialize_aws_json_1_1(
            data["Properties"]
        )
    if "Jar" in data:
        out["jar"] = data["Jar"]
    if "MainClass" in data:
        out["main_class"] = data["MainClass"]
    if "Args" in data:
        import aws_sdk_emr.types.xml_string_list

        out["args"] = aws_sdk_emr.types.xml_string_list.deserialize_aws_json_1_1(
            data["Args"]
        )
    return out
