"""Generated from Smithy shape ``com.amazonaws.medialive#DescribeInputDeviceThumbnailResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__long
    import aws_sdk_medialive.types.__string
    import aws_sdk_medialive.types.__timestamp
    import aws_sdk_medialive.types.content_type
    import aws_sdk_medialive.types.input_device_thumbnail


class DescribeInputDeviceThumbnailResponse(TypedDict, closed=True):
    body: "aws_sdk_medialive.types.input_device_thumbnail.InputDeviceThumbnail"
    """The binary data for the thumbnail that the Link device has most recently sent to MediaLive."""
    content_type: NotRequired["aws_sdk_medialive.types.content_type.ContentType"]
    """Specifies the media type of the thumbnail."""
    content_length: NotRequired["aws_sdk_medialive.types.__long.__long"]
    """The length of the content."""
    e_tag: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """The unique, cacheable version of this thumbnail."""
    last_modified: NotRequired["aws_sdk_medialive.types.__timestamp.__timestamp"]
    """The date and time the thumbnail was last updated at the device."""
