"""Generated from Smithy shape ``com.amazonaws.s3control#CreateAccessPointForObjectLambdaRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_s3_control._protocol.xml import Element, SubElement
from aws_sdk_s3_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.account_id
    import aws_sdk_s3_control.types.object_lambda_access_point_name
    import aws_sdk_s3_control.types.object_lambda_configuration


class CreateAccessPointForObjectLambdaRequest(TypedDict):
    account_id: "aws_sdk_s3_control.types.account_id.AccountId"
    """<p>The Amazon Web Services account ID for owner of the specified Object Lambda Access Point.</p>"""
    name: "aws_sdk_s3_control.types.object_lambda_access_point_name.ObjectLambdaAccessPointName"
    """<p>The name you want to assign to this Object Lambda Access Point.</p>"""
    configuration: (
        "aws_sdk_s3_control.types.object_lambda_configuration.ObjectLambdaConfiguration"
    )
    """<p>Object Lambda Access Point configuration as a JSON document.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: CreateAccessPointForObjectLambdaRequest, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_s3_control.types.object_lambda_configuration

    aws_sdk_s3_control.types.object_lambda_configuration.serialize_xml(
        value["configuration"], el, "Configuration"
    )


def deserialize_xml(el: Element) -> CreateAccessPointForObjectLambdaRequest:
    out: CreateAccessPointForObjectLambdaRequest = {}  # type: ignore[typeddict-item]
    child_configuration = el.find("Configuration")
    if child_configuration is not None:
        import aws_sdk_s3_control.types.object_lambda_configuration

        out["configuration"] = (
            aws_sdk_s3_control.types.object_lambda_configuration.deserialize_xml(
                child_configuration
            )
        )
    else:
        raise DeserializationError(
            "CreateAccessPointForObjectLambdaRequest.configuration required"
        )
    return out
