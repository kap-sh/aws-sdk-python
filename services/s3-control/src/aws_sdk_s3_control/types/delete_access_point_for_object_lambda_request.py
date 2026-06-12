"""Generated from Smithy shape ``com.amazonaws.s3control#DeleteAccessPointForObjectLambdaRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.account_id
    import aws_sdk_s3_control.types.object_lambda_access_point_name


class DeleteAccessPointForObjectLambdaRequest(TypedDict):
    account_id: "aws_sdk_s3_control.types.account_id.AccountId"
    """<p>The account ID for the account that owns the specified Object Lambda Access Point.</p>"""
    name: "aws_sdk_s3_control.types.object_lambda_access_point_name.ObjectLambdaAccessPointName"
    """<p>The name of the access point you want to delete.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: DeleteAccessPointForObjectLambdaRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> DeleteAccessPointForObjectLambdaRequest:
    out: DeleteAccessPointForObjectLambdaRequest = {}  # type: ignore[typeddict-item]
    return out
