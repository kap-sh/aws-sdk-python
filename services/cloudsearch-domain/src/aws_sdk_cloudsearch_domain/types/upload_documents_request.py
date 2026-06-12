"""Generated from Smithy shape ``com.amazonaws.cloudsearchdomain#UploadDocumentsRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cloudsearch_domain.types.blob
    import aws_sdk_cloudsearch_domain.types.content_type


class UploadDocumentsRequest(TypedDict):
    documents: "aws_sdk_cloudsearch_domain.types.blob.Blob"
    """<p>A batch of documents formatted in JSON or HTML.</p>"""
    content_type: "aws_sdk_cloudsearch_domain.types.content_type.ContentType"
    """<p>The format of the batch you are uploading. Amazon CloudSearch supports two document batch formats:</p> <ul> <li>application/json</li> <li>application/xml</li> </ul>"""
