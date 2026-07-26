"""Generated from Smithy shape ``com.amazonaws.s3control#ObjectLambdaAccessPointAlias``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.object_lambda_access_point_alias_status
    import capo_s3_control.types.object_lambda_access_point_alias_value


class ObjectLambdaAccessPointAlias(TypedDict, closed=True):
    value: NotRequired[
        "capo_s3_control.types.object_lambda_access_point_alias_value.ObjectLambdaAccessPointAliasValue"
    ]
    """<p>The alias value of the Object Lambda Access Point.</p>"""
    status: NotRequired[
        "capo_s3_control.types.object_lambda_access_point_alias_status.ObjectLambdaAccessPointAliasStatus"
    ]
    """<p>The status of the Object Lambda Access Point alias. If the status is <code>PROVISIONING</code>, the Object Lambda Access Point is provisioning the alias and the alias is not ready for use yet. If the status is <code>READY</code>, the Object Lambda Access Point alias is successfully provisioned and ready for use.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ObjectLambdaAccessPointAlias, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "value" in value:
        SubElement(el, "Value").text = str(value["value"])
    if "status" in value:
        import capo_s3_control.types.object_lambda_access_point_alias_status

        capo_s3_control.types.object_lambda_access_point_alias_status.serialize_xml(
            value["status"], el, "Status"
        )


def deserialize_xml(el: Element) -> ObjectLambdaAccessPointAlias:
    out: ObjectLambdaAccessPointAlias = {}  # type: ignore[typeddict-item]
    child_value = el.find("Value")
    if child_value is not None:
        out["value"] = str(child_value.text or "")
    child_status = el.find("Status")
    if child_status is not None:
        import capo_s3_control.types.object_lambda_access_point_alias_status

        out["status"] = (
            capo_s3_control.types.object_lambda_access_point_alias_status.deserialize_xml(
                child_status
            )
        )
    return out
