"""Generated from Smithy shape ``com.amazonaws.glue#JobCommand``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.generic_string
    import aws_sdk_glue.types.python_version_string
    import aws_sdk_glue.types.runtime_name_string
    import aws_sdk_glue.types.script_location_string


class JobCommand(TypedDict, closed=True):
    name: NotRequired["aws_sdk_glue.types.generic_string.GenericString"]
    """<p>The name of the job command. For an Apache Spark ETL job, this must be <code>glueetl</code>. For a Python shell job, it must be <code>pythonshell</code>. For an Apache Spark streaming ETL job, this must be <code>gluestreaming</code>. For a Ray job, this must be <code>glueray</code>.</p>"""
    script_location: NotRequired[
        "aws_sdk_glue.types.script_location_string.ScriptLocationString"
    ]
    """<p>Specifies the Amazon Simple Storage Service (Amazon S3) path to a script that runs a job.</p>"""
    python_version: NotRequired[
        "aws_sdk_glue.types.python_version_string.PythonVersionString"
    ]
    """<p>The Python version being used to run a Python shell job. Allowed values are 2 or 3.</p>"""
    runtime: NotRequired["aws_sdk_glue.types.runtime_name_string.RuntimeNameString"]
    r"""<p>In Ray jobs, Runtime is used to specify the versions of Ray, Python and additional libraries available in your environment. This field is not used in other job types. For supported runtime environment values, see <a href=\"https://docs.aws.amazon.com/glue/latest/dg/ray-jobs-section.html\">Supported Ray runtime environments</a> in the Glue Developer Guide.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: JobCommand) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "script_location" in value:
        out["ScriptLocation"] = value["script_location"]
    if "python_version" in value:
        out["PythonVersion"] = value["python_version"]
    if "runtime" in value:
        out["Runtime"] = value["runtime"]
    return out


def deserialize_aws_json_1_1(data: dict) -> JobCommand:
    out: JobCommand = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "ScriptLocation" in data:
        out["script_location"] = data["ScriptLocation"]
    if "PythonVersion" in data:
        out["python_version"] = data["PythonVersion"]
    if "Runtime" in data:
        out["runtime"] = data["Runtime"]
    return out
