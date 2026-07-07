"""Generated from Smithy shape ``com.amazonaws.medicalimaging#GetImageSetMetadataResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medical_imaging.types.image_set_metadata_blob


class GetImageSetMetadataResponse(TypedDict, closed=True):
    image_set_metadata_blob: (
        "aws_sdk_medical_imaging.types.image_set_metadata_blob.ImageSetMetadataBlob"
    )
    """<p>The blob containing the aggregated metadata information for the image set.</p>"""
    content_type: NotRequired["str"]
    """<p>The format in which the study metadata is returned to the customer. Default is <code>text/plain</code>.</p>"""
    content_encoding: NotRequired["str"]
    """<p>The compression format in which image set metadata attributes are returned.</p>"""
