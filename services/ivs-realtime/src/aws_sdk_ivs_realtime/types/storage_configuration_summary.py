"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#StorageConfigurationSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ivs_realtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ivs_realtime.types.s3_storage_configuration
    import aws_sdk_ivs_realtime.types.storage_configuration_arn
    import aws_sdk_ivs_realtime.types.storage_configuration_name
    import aws_sdk_ivs_realtime.types.tags


class StorageConfigurationSummary(TypedDict):
    arn: "aws_sdk_ivs_realtime.types.storage_configuration_arn.StorageConfigurationArn"
    """<p>ARN of the storage configuration.</p>"""
    name: NotRequired[
        "aws_sdk_ivs_realtime.types.storage_configuration_name.StorageConfigurationName"
    ]
    """<p>Name of the storage configuration.</p>"""
    s3: NotRequired[
        "aws_sdk_ivs_realtime.types.s3_storage_configuration.S3StorageConfiguration"
    ]
    """<p>An S3 destination configuration where recorded videos will be stored.</p>"""
    tags: NotRequired["aws_sdk_ivs_realtime.types.tags.Tags"]
    r"""<p>Tags attached to the resource. Array of maps, each of the form <code>string:string (key:value)</code>. See <a href=\"https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html\">Best practices and strategies</a> in <i>Tagging AWS Resources and Tag Editor</i> for details, including restrictions that apply to tags and \"Tag naming limits and requirements\"; Amazon IVS has no constraints on tags beyond what is documented there.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StorageConfigurationSummary) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "s3" in value:
        import aws_sdk_ivs_realtime.types.s3_storage_configuration

        out["s3"] = aws_sdk_ivs_realtime.types.s3_storage_configuration.serialize_json(
            value["s3"]
        )
    if "tags" in value:
        import aws_sdk_ivs_realtime.types.tags

        out["tags"] = aws_sdk_ivs_realtime.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> StorageConfigurationSummary:
    out: StorageConfigurationSummary = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("StorageConfigurationSummary.arn required")
    if "name" in data:
        out["name"] = data["name"]
    if "s3" in data:
        import aws_sdk_ivs_realtime.types.s3_storage_configuration

        out["s3"] = (
            aws_sdk_ivs_realtime.types.s3_storage_configuration.deserialize_json(
                data["s3"]
            )
        )
    if "tags" in data:
        import aws_sdk_ivs_realtime.types.tags

        out["tags"] = aws_sdk_ivs_realtime.types.tags.deserialize_json(data["tags"])
    return out
