"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#CreateStorageConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ivs_realtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ivs_realtime.types.s3_storage_configuration
    import aws_sdk_ivs_realtime.types.storage_configuration_name
    import aws_sdk_ivs_realtime.types.tags


class CreateStorageConfigurationRequest(TypedDict, closed=True):
    name: NotRequired[
        "aws_sdk_ivs_realtime.types.storage_configuration_name.StorageConfigurationName"
    ]
    """<p>Storage configuration name. The value does not need to be unique.</p>"""
    s3: "aws_sdk_ivs_realtime.types.s3_storage_configuration.S3StorageConfiguration"
    """<p>A complex type that contains a storage configuration for where recorded video will be stored.</p>"""
    tags: NotRequired["aws_sdk_ivs_realtime.types.tags.Tags"]
    r"""<p>Tags attached to the resource. Array of maps, each of the form <code>string:string (key:value)</code>. See <a href=\"https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html\">Best practices and strategies</a> in <i>Tagging AWS Resources and Tag Editor</i> for details, including restrictions that apply to tags and \"Tag naming limits and requirements\"; Amazon IVS has no constraints on tags beyond what is documented there.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateStorageConfigurationRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    import aws_sdk_ivs_realtime.types.s3_storage_configuration

    out["s3"] = aws_sdk_ivs_realtime.types.s3_storage_configuration.serialize_json(
        value["s3"]
    )
    if "tags" in value:
        import aws_sdk_ivs_realtime.types.tags

        out["tags"] = aws_sdk_ivs_realtime.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateStorageConfigurationRequest:
    out: CreateStorageConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "s3" in data:
        import aws_sdk_ivs_realtime.types.s3_storage_configuration

        out["s3"] = (
            aws_sdk_ivs_realtime.types.s3_storage_configuration.deserialize_json(
                data["s3"]
            )
        )
    else:
        raise DeserializationError("CreateStorageConfigurationRequest.s3 required")
    if "tags" in data:
        import aws_sdk_ivs_realtime.types.tags

        out["tags"] = aws_sdk_ivs_realtime.types.tags.deserialize_json(data["tags"])
    return out
