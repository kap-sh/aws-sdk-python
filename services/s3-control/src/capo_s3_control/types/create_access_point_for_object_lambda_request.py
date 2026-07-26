"""Generated from Smithy shape ``com.amazonaws.s3control#CreateAccessPointForObjectLambdaRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_s3_control._protocol.xml import Element, SubElement
from capo_s3_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_s3_control.types.account_id
    import capo_s3_control.types.object_lambda_access_point_name
    import capo_s3_control.types.object_lambda_configuration


class CreateAccessPointForObjectLambdaRequest(TypedDict, closed=True):
    account_id: "capo_s3_control.types.account_id.AccountId"
    """<p>The Amazon Web Services account ID for owner of the specified Object Lambda Access Point.</p>"""
    name: "capo_s3_control.types.object_lambda_access_point_name.ObjectLambdaAccessPointName"
    """<p>The name you want to assign to this Object Lambda Access Point.</p>"""
    configuration: (
        "capo_s3_control.types.object_lambda_configuration.ObjectLambdaConfiguration"
    )
    """<p>Object Lambda Access Point configuration as a JSON document.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: CreateAccessPointForObjectLambdaRequest, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import capo_s3_control.types.object_lambda_configuration

    capo_s3_control.types.object_lambda_configuration.serialize_xml(
        value["configuration"], el, "Configuration"
    )


def deserialize_xml(el: Element) -> CreateAccessPointForObjectLambdaRequest:
    out: CreateAccessPointForObjectLambdaRequest = {}  # type: ignore[typeddict-item]
    child_configuration = el.find("Configuration")
    if child_configuration is not None:
        import capo_s3_control.types.object_lambda_configuration

        out["configuration"] = (
            capo_s3_control.types.object_lambda_configuration.deserialize_xml(
                child_configuration
            )
        )
    else:
        raise DeserializationError(
            "CreateAccessPointForObjectLambdaRequest.configuration required"
        )
    return out
