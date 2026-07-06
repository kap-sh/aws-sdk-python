"""Generated from Smithy shape ``com.amazonaws.gamelift#Script``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.node_js_version
    import aws_sdk_gamelift.types.non_zero_and_max_string
    import aws_sdk_gamelift.types.s3_location
    import aws_sdk_gamelift.types.script_arn
    import aws_sdk_gamelift.types.script_id
    import aws_sdk_gamelift.types.timestamp
    import aws_sdk_gamelift.types.whole_number_long


class Script(TypedDict, closed=True):
    script_id: NotRequired["aws_sdk_gamelift.types.script_id.ScriptId"]
    """<p>A unique identifier for the Realtime script</p>"""
    script_arn: NotRequired["aws_sdk_gamelift.types.script_arn.ScriptArn"]
    r"""<p>The Amazon Resource Name (<a href=\"https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html\">ARN</a>) that is assigned to a Amazon GameLift Servers script resource and uniquely identifies it. ARNs are unique across all Regions. In a GameLift script ARN, the resource ID matches the <i>ScriptId</i> value.</p>"""
    name: NotRequired[
        "aws_sdk_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>A descriptive label that is associated with a script. Script names do not need to be unique.</p>"""
    version: NotRequired[
        "aws_sdk_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>Version information that is associated with a build or script. Version strings do not need to be unique.</p>"""
    size_on_disk: NotRequired[
        "aws_sdk_gamelift.types.whole_number_long.WholeNumberLong"
    ]
    r"""<p>The file size of the uploaded Realtime script, expressed in bytes. When files are uploaded from an S3 location, this value remains at \"0\".</p>"""
    creation_time: NotRequired["aws_sdk_gamelift.types.timestamp.Timestamp"]
    r"""<p>A time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example <code>\"1469498468.057\"</code>).</p>"""
    storage_location: NotRequired["aws_sdk_gamelift.types.s3_location.S3Location"]
    r"""<p>The location of the Amazon S3 bucket where a zipped file containing your Realtime scripts is stored. The storage location must specify the Amazon S3 bucket name, the zip file name (the \"key\"), and a role ARN that allows Amazon GameLift Servers to access the Amazon S3 storage location. The S3 bucket must be in the same Region where you want to create a new script. By default, Amazon GameLift Servers uploads the latest version of the zip file; if you have S3 object versioning turned on, you can use the <code>ObjectVersion</code> parameter to specify an earlier version. </p>"""
    node_js_version: NotRequired["aws_sdk_gamelift.types.node_js_version.NodeJsVersion"]
    r"""<p>The Node.js version used for execution of your Realtime script. The valid values are <code>10.x | 24.x</code>. By default, <code>NodeJsVersion</code> is <code>10.x</code>. This value cannot be updated later. </p> <note> <p>Node.js 10 will reach end of support on September 30, 2026. See more details in the <a href=\"http://aws.amazon.com/gamelift/faq/nodejs10/\">Node.js 10 FAQs</a>. For migration guidance, see <a href=\"https://docs.aws.amazon.com/gamelift/latest/realtimeguide/realtime-script.html#realtime-script-nodejs-migration\"> Migrating from Node.js 10 to 24</a>.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Script) -> dict:
    out: dict = {}
    if "script_id" in value:
        out["ScriptId"] = value["script_id"]
    if "script_arn" in value:
        out["ScriptArn"] = value["script_arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "version" in value:
        out["Version"] = value["version"]
    if "size_on_disk" in value:
        out["SizeOnDisk"] = value["size_on_disk"]
    if "creation_time" in value:
        import aws_sdk_gamelift.types.timestamp

        out["CreationTime"] = aws_sdk_gamelift.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "storage_location" in value:
        import aws_sdk_gamelift.types.s3_location

        out["StorageLocation"] = (
            aws_sdk_gamelift.types.s3_location.serialize_aws_json_1_1(
                value["storage_location"]
            )
        )
    if "node_js_version" in value:
        out["NodeJsVersion"] = value["node_js_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Script:
    out: Script = {}  # type: ignore[typeddict-item]
    if "ScriptId" in data:
        out["script_id"] = data["ScriptId"]
    if "ScriptArn" in data:
        out["script_arn"] = data["ScriptArn"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Version" in data:
        out["version"] = data["Version"]
    if "SizeOnDisk" in data:
        out["size_on_disk"] = data["SizeOnDisk"]
    if "CreationTime" in data:
        import aws_sdk_gamelift.types.timestamp

        out["creation_time"] = (
            aws_sdk_gamelift.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if "StorageLocation" in data:
        import aws_sdk_gamelift.types.s3_location

        out["storage_location"] = (
            aws_sdk_gamelift.types.s3_location.deserialize_aws_json_1_1(
                data["StorageLocation"]
            )
        )
    if "NodeJsVersion" in data:
        out["node_js_version"] = data["NodeJsVersion"]
    return out
