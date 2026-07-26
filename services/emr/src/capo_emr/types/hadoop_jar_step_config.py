"""Generated from Smithy shape ``com.amazonaws.emr#HadoopJarStepConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr.types.key_value_list
    import capo_emr.types.xml_string
    import capo_emr.types.xml_string_list


class HadoopJarStepConfig(TypedDict, closed=True):
    properties: NotRequired["capo_emr.types.key_value_list.KeyValueList"]
    """<p>A list of Java properties that are set when the step runs. You can use these properties to pass key-value pairs to your main function.</p>"""
    jar: NotRequired["capo_emr.types.xml_string.XmlString"]
    """<p>A path to a JAR file run during the step.</p>"""
    main_class: NotRequired["capo_emr.types.xml_string.XmlString"]
    """<p>The name of the main class in the specified Java file. If not specified, the JAR file should specify a Main-Class in its manifest file.</p>"""
    args: NotRequired["capo_emr.types.xml_string_list.XmlStringList"]
    """<p>A list of command line arguments passed to the JAR file's main function when executed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HadoopJarStepConfig) -> dict:
    out: dict = {}
    if "properties" in value:
        import capo_emr.types.key_value_list

        out["Properties"] = capo_emr.types.key_value_list.serialize_aws_json_1_1(
            value["properties"]
        )
    if "jar" in value:
        out["Jar"] = value["jar"]
    if "main_class" in value:
        out["MainClass"] = value["main_class"]
    if "args" in value:
        import capo_emr.types.xml_string_list

        out["Args"] = capo_emr.types.xml_string_list.serialize_aws_json_1_1(
            value["args"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> HadoopJarStepConfig:
    out: HadoopJarStepConfig = {}  # type: ignore[typeddict-item]
    if "Properties" in data:
        import capo_emr.types.key_value_list

        out["properties"] = capo_emr.types.key_value_list.deserialize_aws_json_1_1(
            data["Properties"]
        )
    if "Jar" in data:
        out["jar"] = data["Jar"]
    if "MainClass" in data:
        out["main_class"] = data["MainClass"]
    if "Args" in data:
        import capo_emr.types.xml_string_list

        out["args"] = capo_emr.types.xml_string_list.deserialize_aws_json_1_1(
            data["Args"]
        )
    return out
