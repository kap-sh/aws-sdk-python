"""Generated from Smithy shape ``com.amazonaws.clouddirectory#PublishSchemaRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_clouddirectory.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.arn
    import aws_sdk_clouddirectory.types.schema_name
    import aws_sdk_clouddirectory.types.version


class PublishSchemaRequest(TypedDict, closed=True):
    development_schema_arn: "aws_sdk_clouddirectory.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) that is associated with the development schema. For more information, see <a>arns</a>.</p>"""
    version: "aws_sdk_clouddirectory.types.version.Version"
    """<p>The major version under which the schema will be published. Schemas have both a major and minor version associated with them.</p>"""
    minor_version: NotRequired["aws_sdk_clouddirectory.types.version.Version"]
    """<p>The minor version under which the schema will be published. This parameter is recommended. Schemas have both a major and minor version associated with them.</p>"""
    name: NotRequired["aws_sdk_clouddirectory.types.schema_name.SchemaName"]
    """<p>The new name under which the schema will be published. If this is not provided, the development schema is considered.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PublishSchemaRequest) -> dict:
    out: dict = {}
    out["Version"] = value["version"]
    if "minor_version" in value:
        out["MinorVersion"] = value["minor_version"]
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> PublishSchemaRequest:
    out: PublishSchemaRequest = {}  # type: ignore[typeddict-item]
    if "Version" in data:
        out["version"] = data["Version"]
    else:
        raise DeserializationError("PublishSchemaRequest.version required")
    if "MinorVersion" in data:
        out["minor_version"] = data["MinorVersion"]
    if "Name" in data:
        out["name"] = data["Name"]
    return out
