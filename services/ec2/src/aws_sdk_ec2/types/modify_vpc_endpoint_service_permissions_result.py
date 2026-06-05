"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyVpcEndpointServicePermissionsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.added_principal_set
    import aws_sdk_ec2.types.boolean


class ModifyVpcEndpointServicePermissionsResult(TypedDict):
    added_principals: NotRequired[
        "aws_sdk_ec2.types.added_principal_set.AddedPrincipalSet"
    ]
    """<p>Information about the added principals.</p>"""
    return_value: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Returns <code>true</code> if the request succeeds; otherwise, it returns an error.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyVpcEndpointServicePermissionsResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "added_principals" in value:
        import aws_sdk_ec2.types.added_principal_set

        aws_sdk_ec2.types.added_principal_set.serialize_ec2_query(
            value["added_principals"], pairs, f"{prefix}.AddedPrincipalSet"
        )
    if "return_value" in value:
        pairs.append((f"{prefix}.Return", "true" if value["return_value"] else "false"))


def deserialize_ec2_query(el: Element) -> ModifyVpcEndpointServicePermissionsResult:
    out: ModifyVpcEndpointServicePermissionsResult = {}  # type: ignore[typeddict-item]
    if el.find("AddedPrincipalSet") is not None:
        import aws_sdk_ec2.types.added_principal_set

        out["added_principals"] = (
            aws_sdk_ec2.types.added_principal_set.deserialize_ec2_query(
                el, "AddedPrincipalSet"
            )
        )
    child_return_value = el.find("Return")
    if child_return_value is not None:
        out["return_value"] = (child_return_value.text or "").lower() == "true"
    return out
