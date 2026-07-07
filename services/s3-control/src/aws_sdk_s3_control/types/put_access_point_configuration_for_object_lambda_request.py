"""Generated from Smithy shape ``com.amazonaws.s3control#PutAccessPointConfigurationForObjectLambdaRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_s3_control._protocol.xml import Element, SubElement
from aws_sdk_s3_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.account_id
    import aws_sdk_s3_control.types.object_lambda_access_point_name
    import aws_sdk_s3_control.types.object_lambda_configuration


class PutAccessPointConfigurationForObjectLambdaRequest(TypedDict, closed=True):
    account_id: "aws_sdk_s3_control.types.account_id.AccountId"
    """<p>The account ID for the account that owns the specified Object Lambda Access Point.</p>"""
    name: "aws_sdk_s3_control.types.object_lambda_access_point_name.ObjectLambdaAccessPointName"
    """<p>The name of the Object Lambda Access Point.</p>"""
    configuration: (
        "aws_sdk_s3_control.types.object_lambda_configuration.ObjectLambdaConfiguration"
    )
    """<p>Object Lambda Access Point configuration document.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: PutAccessPointConfigurationForObjectLambdaRequest, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_s3_control.types.object_lambda_configuration

    aws_sdk_s3_control.types.object_lambda_configuration.serialize_xml(
        value["configuration"], el, "Configuration"
    )


def deserialize_xml(el: Element) -> PutAccessPointConfigurationForObjectLambdaRequest:
    out: PutAccessPointConfigurationForObjectLambdaRequest = {}  # type: ignore[typeddict-item]
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
            "PutAccessPointConfigurationForObjectLambdaRequest.configuration required"
        )
    return out
