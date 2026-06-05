"""Generated from Smithy shape ``com.amazonaws.ec2#OperatorResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.string


class OperatorResponse(TypedDict):
    managed: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>If <code>true</code>, the resource is managed by a service provider.</p>"""
    principal: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>If <code>managed</code> is <code>true</code>, then the principal is returned. The principal is the service provider that manages the resource.</p>"""
    hidden_by_default: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>If <code>true</code>, the resource is hidden by default based on the managed resource visibility settings for the account.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: OperatorResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "managed" in value:
        pairs.append((f"{prefix}.Managed", "true" if value["managed"] else "false"))
    if "principal" in value:
        pairs.append((f"{prefix}.Principal", str(value["principal"])))
    if "hidden_by_default" in value:
        pairs.append(
            (
                f"{prefix}.HiddenByDefault",
                "true" if value["hidden_by_default"] else "false",
            )
        )


def deserialize_ec2_query(el: Element) -> OperatorResponse:
    out: OperatorResponse = {}  # type: ignore[typeddict-item]
    child_managed = el.find("Managed")
    if child_managed is not None:
        out["managed"] = (child_managed.text or "").lower() == "true"
    child_principal = el.find("Principal")
    if child_principal is not None:
        out["principal"] = str(child_principal.text or "")
    child_hidden_by_default = el.find("HiddenByDefault")
    if child_hidden_by_default is not None:
        out["hidden_by_default"] = (
            child_hidden_by_default.text or ""
        ).lower() == "true"
    return out
