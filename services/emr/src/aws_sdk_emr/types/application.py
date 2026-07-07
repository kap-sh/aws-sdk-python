"""Generated from Smithy shape ``com.amazonaws.emr#Application``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_emr.types.string
    import aws_sdk_emr.types.string_list
    import aws_sdk_emr.types.string_map


class Application(TypedDict, closed=True):
    name: NotRequired["aws_sdk_emr.types.string.String"]
    """<p>The name of the application.</p>"""
    version: NotRequired["aws_sdk_emr.types.string.String"]
    """<p>The version of the application.</p>"""
    args: NotRequired["aws_sdk_emr.types.string_list.StringList"]
    """<p>Arguments for Amazon EMR to pass to the application.</p>"""
    additional_info: NotRequired["aws_sdk_emr.types.string_map.StringMap"]
    """<p>This option is for advanced users only. This is meta information about third-party applications that third-party vendors use for testing purposes.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Application) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "version" in value:
        out["Version"] = value["version"]
    if "args" in value:
        import aws_sdk_emr.types.string_list

        out["Args"] = aws_sdk_emr.types.string_list.serialize_aws_json_1_1(
            value["args"]
        )
    if "additional_info" in value:
        import aws_sdk_emr.types.string_map

        out["AdditionalInfo"] = aws_sdk_emr.types.string_map.serialize_aws_json_1_1(
            value["additional_info"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Application:
    out: Application = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Version" in data:
        out["version"] = data["Version"]
    if "Args" in data:
        import aws_sdk_emr.types.string_list

        out["args"] = aws_sdk_emr.types.string_list.deserialize_aws_json_1_1(
            data["Args"]
        )
    if "AdditionalInfo" in data:
        import aws_sdk_emr.types.string_map

        out["additional_info"] = aws_sdk_emr.types.string_map.deserialize_aws_json_1_1(
            data["AdditionalInfo"]
        )
    return out
