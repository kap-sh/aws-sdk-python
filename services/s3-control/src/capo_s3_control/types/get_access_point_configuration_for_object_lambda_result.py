"""Generated from Smithy shape ``com.amazonaws.s3control#GetAccessPointConfigurationForObjectLambdaResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.object_lambda_configuration


class GetAccessPointConfigurationForObjectLambdaResult(TypedDict, closed=True):
    configuration: NotRequired[
        "capo_s3_control.types.object_lambda_configuration.ObjectLambdaConfiguration"
    ]
    """<p>Object Lambda Access Point configuration document.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: GetAccessPointConfigurationForObjectLambdaResult, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "configuration" in value:
        import capo_s3_control.types.object_lambda_configuration

        capo_s3_control.types.object_lambda_configuration.serialize_xml(
            value["configuration"], el, "Configuration"
        )


def deserialize_xml(el: Element) -> GetAccessPointConfigurationForObjectLambdaResult:
    out: GetAccessPointConfigurationForObjectLambdaResult = {}  # type: ignore[typeddict-item]
    child_configuration = el.find("Configuration")
    if child_configuration is not None:
        import capo_s3_control.types.object_lambda_configuration

        out["configuration"] = (
            capo_s3_control.types.object_lambda_configuration.deserialize_xml(
                child_configuration
            )
        )
    return out
