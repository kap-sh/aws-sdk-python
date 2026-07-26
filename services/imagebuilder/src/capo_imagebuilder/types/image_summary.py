"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ImageSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.build_type
    import capo_imagebuilder.types.date_time
    import capo_imagebuilder.types.date_time_timestamp
    import capo_imagebuilder.types.image_builder_arn
    import capo_imagebuilder.types.image_logging_configuration
    import capo_imagebuilder.types.image_source
    import capo_imagebuilder.types.image_state
    import capo_imagebuilder.types.image_type
    import capo_imagebuilder.types.lifecycle_execution_id
    import capo_imagebuilder.types.non_empty_string
    import capo_imagebuilder.types.os_version
    import capo_imagebuilder.types.output_resources
    import capo_imagebuilder.types.platform
    import capo_imagebuilder.types.resource_name
    import capo_imagebuilder.types.tag_map
    import capo_imagebuilder.types.version_number


class ImageSummary(TypedDict, closed=True):
    arn: NotRequired["capo_imagebuilder.types.image_builder_arn.ImageBuilderArn"]
    """<p>The Amazon Resource Name (ARN) of the image.</p>"""
    name: NotRequired["capo_imagebuilder.types.resource_name.ResourceName"]
    """<p>The name of the image.</p>"""
    type: NotRequired["capo_imagebuilder.types.image_type.ImageType"]
    """<p>Specifies whether this image produces an AMI or a container image.</p>"""
    version: NotRequired["capo_imagebuilder.types.version_number.VersionNumber"]
    """<p>The version of the image.</p>"""
    platform: NotRequired["capo_imagebuilder.types.platform.Platform"]
    """<p>The image operating system platform, such as Linux or Windows.</p>"""
    os_version: NotRequired["capo_imagebuilder.types.os_version.OsVersion"]
    """<p>The operating system version of the instances that launch from this image. For example, Amazon Linux 2, Ubuntu 18, or Microsoft Windows Server 2019.</p>"""
    state: NotRequired["capo_imagebuilder.types.image_state.ImageState"]
    """<p>The state of the image.</p>"""
    owner: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The owner of the image.</p>"""
    date_created: NotRequired["capo_imagebuilder.types.date_time.DateTime"]
    """<p>The date on which Image Builder created this image.</p>"""
    output_resources: NotRequired[
        "capo_imagebuilder.types.output_resources.OutputResources"
    ]
    """<p>The output resources that Image Builder produced when it created this image.</p>"""
    tags: NotRequired["capo_imagebuilder.types.tag_map.TagMap"]
    """<p>The tags that apply to this image.</p>"""
    build_type: NotRequired["capo_imagebuilder.types.build_type.BuildType"]
    """<p>Indicates the type of build that created this image. The build can be initiated in the following ways:</p> <ul> <li> <p> <b>USER_INITIATED</b> – A manual pipeline build request.</p> </li> <li> <p> <b>SCHEDULED</b> – A pipeline build initiated by a cron expression in the Image Builder pipeline, or from EventBridge.</p> </li> <li> <p> <b>IMPORT</b> – A VM import created the image to use as the base image for the recipe.</p> </li> <li> <p> <b>IMPORT_ISO</b> – An ISO disk import created the image.</p> </li> </ul>"""
    image_source: NotRequired["capo_imagebuilder.types.image_source.ImageSource"]
    """<p>The origin of the base image that Image Builder used to build this image.</p>"""
    deprecation_time: NotRequired[
        "capo_imagebuilder.types.date_time_timestamp.DateTimeTimestamp"
    ]
    """<p>The time when deprecation occurs for an image resource. This can be a past or future date.</p>"""
    lifecycle_execution_id: NotRequired[
        "capo_imagebuilder.types.lifecycle_execution_id.LifecycleExecutionId"
    ]
    """<p>Identifies the last runtime instance of the lifecycle policy to take action on the image.</p>"""
    logging_configuration: NotRequired[
        "capo_imagebuilder.types.image_logging_configuration.ImageLoggingConfiguration"
    ]
    """<p>The logging configuration that's defined for the image.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImageSummary) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "type" in value:
        import capo_imagebuilder.types.image_type

        out["type"] = capo_imagebuilder.types.image_type.serialize_json(value["type"])
    if "version" in value:
        out["version"] = value["version"]
    if "platform" in value:
        import capo_imagebuilder.types.platform

        out["platform"] = capo_imagebuilder.types.platform.serialize_json(
            value["platform"]
        )
    if "os_version" in value:
        out["osVersion"] = value["os_version"]
    if "state" in value:
        import capo_imagebuilder.types.image_state

        out["state"] = capo_imagebuilder.types.image_state.serialize_json(
            value["state"]
        )
    if "owner" in value:
        out["owner"] = value["owner"]
    if "date_created" in value:
        out["dateCreated"] = value["date_created"]
    if "output_resources" in value:
        import capo_imagebuilder.types.output_resources

        out["outputResources"] = (
            capo_imagebuilder.types.output_resources.serialize_json(
                value["output_resources"]
            )
        )
    if "tags" in value:
        import capo_imagebuilder.types.tag_map

        out["tags"] = capo_imagebuilder.types.tag_map.serialize_json(value["tags"])
    if "build_type" in value:
        import capo_imagebuilder.types.build_type

        out["buildType"] = capo_imagebuilder.types.build_type.serialize_json(
            value["build_type"]
        )
    if "image_source" in value:
        import capo_imagebuilder.types.image_source

        out["imageSource"] = capo_imagebuilder.types.image_source.serialize_json(
            value["image_source"]
        )
    if "deprecation_time" in value:
        import capo_imagebuilder.types.date_time_timestamp

        out["deprecationTime"] = (
            capo_imagebuilder.types.date_time_timestamp.serialize_json(
                value["deprecation_time"]
            )
        )
    if "lifecycle_execution_id" in value:
        out["lifecycleExecutionId"] = value["lifecycle_execution_id"]
    if "logging_configuration" in value:
        import capo_imagebuilder.types.image_logging_configuration

        out["loggingConfiguration"] = (
            capo_imagebuilder.types.image_logging_configuration.serialize_json(
                value["logging_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> ImageSummary:
    out: ImageSummary = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "name" in data:
        out["name"] = data["name"]
    if "type" in data:
        import capo_imagebuilder.types.image_type

        out["type"] = capo_imagebuilder.types.image_type.deserialize_json(data["type"])
    if "version" in data:
        out["version"] = data["version"]
    if "platform" in data:
        import capo_imagebuilder.types.platform

        out["platform"] = capo_imagebuilder.types.platform.deserialize_json(
            data["platform"]
        )
    if "osVersion" in data:
        out["os_version"] = data["osVersion"]
    if "state" in data:
        import capo_imagebuilder.types.image_state

        out["state"] = capo_imagebuilder.types.image_state.deserialize_json(
            data["state"]
        )
    if "owner" in data:
        out["owner"] = data["owner"]
    if "dateCreated" in data:
        out["date_created"] = data["dateCreated"]
    if "outputResources" in data:
        import capo_imagebuilder.types.output_resources

        out["output_resources"] = (
            capo_imagebuilder.types.output_resources.deserialize_json(
                data["outputResources"]
            )
        )
    if "tags" in data:
        import capo_imagebuilder.types.tag_map

        out["tags"] = capo_imagebuilder.types.tag_map.deserialize_json(data["tags"])
    if "buildType" in data:
        import capo_imagebuilder.types.build_type

        out["build_type"] = capo_imagebuilder.types.build_type.deserialize_json(
            data["buildType"]
        )
    if "imageSource" in data:
        import capo_imagebuilder.types.image_source

        out["image_source"] = capo_imagebuilder.types.image_source.deserialize_json(
            data["imageSource"]
        )
    if "deprecationTime" in data:
        import capo_imagebuilder.types.date_time_timestamp

        out["deprecation_time"] = (
            capo_imagebuilder.types.date_time_timestamp.deserialize_json(
                data["deprecationTime"]
            )
        )
    if "lifecycleExecutionId" in data:
        out["lifecycle_execution_id"] = data["lifecycleExecutionId"]
    if "loggingConfiguration" in data:
        import capo_imagebuilder.types.image_logging_configuration

        out["logging_configuration"] = (
            capo_imagebuilder.types.image_logging_configuration.deserialize_json(
                data["loggingConfiguration"]
            )
        )
    return out
